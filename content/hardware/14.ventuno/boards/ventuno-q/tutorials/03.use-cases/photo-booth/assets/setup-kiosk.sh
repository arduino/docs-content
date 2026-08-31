#!/bin/bash
# Configure the VENTUNO Q to boot straight into the Photo Booth kiosk.
#
# Installs / configures, idempotently:
#   1. Chromium (snap) if no chromium binary is present
#   2. GDM automatic login for the `arduino` user
#   3. Back-end autostart systemd unit (waits for the arduino-app-cli daemon,
#      then `arduino-app-cli app start`)
#   4. Chromium kiosk launcher + GNOME autostart entry
#   5. Suppression of the dialogs an unattended session would otherwise show
#   6. Sleep, idle blanking and screen lock disabled
#
# This script does the kiosk and nothing else. Install the app first — easiest
# through the App Lab UI — then run this last:
#
#   sudo bash setup-kiosk.sh
#
# It finds the installed Photo Booth app itself. Override if you need to:
#
#   APP_ID=user:photo-booth-20260728-230522 sudo -E bash setup-kiosk.sh
#
# Undo everything with remove-kiosk.sh.

set -euo pipefail

USER_NAME="${KIOSK_USER:-arduino}"
USER_HOME="/home/${USER_NAME}"
PORT="${PORT:-7000}"
APPS_DIR="${USER_HOME}/ArduinoApps"
STATE_DIR="/var/lib/photo-booth-kiosk"
WAYLAND_STATE="${STATE_DIR}/gdm-wayland-disabled-line"
AUTOLOGIN_STATE="${STATE_DIR}/gdm-autologin-lines"
UPDATE_NOTIFIER_STATE="${STATE_DIR}/update-notifier.desktop"
UPDATE_NOTIFIER_MISSING="${STATE_DIR}/update-notifier-was-missing"
KEYRING_STATE="${STATE_DIR}/login-keyring-backup-path"
SLEEP_STATE="${STATE_DIR}/preexisting-masked-sleep-targets"
DCONF_PROFILE_STATE="${STATE_DIR}/dconf-profile-action"
CHROMIUM_INSTALLED_STATE="${STATE_DIR}/chromium-installed-by-setup"
UNIT_BACKUP="${STATE_DIR}/unit.backup"
UNIT_MISSING="${STATE_DIR}/unit.was-missing"
UNIT_HASH="${STATE_DIR}/unit.installed-sha256"
UNIT_ENABLE_STATE="${STATE_DIR}/unit.original-enabled-state"
LAUNCHER_BACKUP="${STATE_DIR}/launcher.backup"
LAUNCHER_MISSING="${STATE_DIR}/launcher.was-missing"
LAUNCHER_HASH="${STATE_DIR}/launcher.installed-sha256"
DESKTOP_BACKUP="${STATE_DIR}/desktop.backup"
DESKTOP_MISSING="${STATE_DIR}/desktop.was-missing"
DESKTOP_HASH="${STATE_DIR}/desktop.installed-sha256"
UPDATE_NOTIFIER_HASH="${STATE_DIR}/update-notifier.installed-sha256"

if [ "$(id -u)" -ne 0 ]; then echo "Please run with sudo." >&2; exit 1; fi

# --- 0. Which app are we booting into? ---------------------------------------
# Importing through the App Lab UI gives the app a timestamped id
# (user:photo-booth-20260728-230522), so the id cannot be hard-coded. Find it
# instead, and let APP_ID override when there is more than one candidate.
if [ -z "${APP_ID:-}" ]; then
    echo "==> Looking for an installed Photo Booth app..."
    # Must run as the kiosk user: apps are resolved from that user's home, so
    # `arduino-app-cli app list` returns nothing at all under sudo/root.
    mapfile -t CANDIDATES < <(
        runuser -u "$USER_NAME" -- arduino-app-cli app list --format json 2>/dev/null | python3 -c '
import base64, json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
rows = d if isinstance(d, list) else d.get("apps", d)
for r in rows:
    if r.get("example"):
        continue
    rid = r.get("id", "")
    try:  # the json id is unpadded base64 of the real id ("user:photo-booth")
        rid = base64.b64decode(rid + "=" * (-len(rid) % 4)).decode()
    except Exception:
        continue
    if rid.startswith("user:photo-booth"):
        print(rid)
' || true
    )
    case "${#CANDIDATES[@]}" in
        0)
            echo "!! No Photo Booth app is installed on this board." >&2
            echo "   Import it first through the App Lab UI (My Apps ->" >&2
            echo "   Create new app -> Import app), then re-run this script." >&2
            exit 1
            ;;
        1)
            APP_ID="${CANDIDATES[0]}"
            echo "    Found: ${APP_ID}"
            ;;
        *)
            echo "!! More than one Photo Booth app is installed:" >&2
            printf '     %s\n' "${CANDIDATES[@]}" >&2
            echo "   Re-run naming the one to boot into, e.g.:" >&2
            echo "     APP_ID=${CANDIDATES[0]} sudo -E bash $0" >&2
            exit 1
            ;;
    esac
fi

APP_DIR="${APPS_DIR}/${APP_ID#user:}"
if [ ! -f "${APP_DIR}/app.yaml" ]; then
    echo "!! ${APP_DIR}/app.yaml not found — is ${APP_ID} really installed?" >&2
    exit 1
fi

# The kiosk's systemd unit owns autostart; prevent a daemon default app from
# starting alongside it and competing for ports or hardware.
runuser -u "$USER_NAME" -- arduino-app-cli properties set default none

install -d -m 0700 "$STATE_DIR"

snapshot_file_once() {
    local path="$1" backup="$2" missing="$3"
    if [ ! -e "$backup" ] && [ ! -e "$missing" ]; then
        if [ -L "$path" ]; then
            echo "!! Refusing to replace symbolic link: ${path}" >&2
            exit 1
        fi
        if [ -e "$path" ]; then
            cp -a "$path" "$backup"
        else
            touch "$missing"
        fi
    fi
}

record_installed_hash() {
    sha256sum "$1" | cut -d ' ' -f1 > "$2"
}

# Validate the login configuration before installing or changing anything.
GDM_CONF=/etc/gdm3/custom.conf
if [ ! -f "$GDM_CONF" ]; then
    echo "!! ${GDM_CONF} not found; cannot configure the kiosk login." >&2
    exit 1
fi
if ! grep -qE '^[[:space:]]*\[daemon\][[:space:]]*$' "$GDM_CONF"; then
    echo "!! [daemon] section not found in ${GDM_CONF}; cannot configure the kiosk login." >&2
    exit 1
fi

# --- 1. Chromium -------------------------------------------------------------
# Not part of the board image. On the Ubuntu-based image it is a snap:
# `apt install chromium` has no candidate at all.
if command -v chromium >/dev/null 2>&1 || [ -x /snap/bin/chromium ]; then
    echo "==> Chromium already present."
else
    echo "==> Installing Chromium (snap; this can take several minutes)..."
    snap install chromium
    touch "$CHROMIUM_INSTALLED_STATE"
fi

# --- 2. GDM autologin --------------------------------------------------------
# The stock image ships a commented example under [daemon]; we must add ACTIVE
# lines and not be fooled by the commented ones.
# Chromium's kiosk mode remains a decorated window on this image when GDM is
# explicitly forced to X11. Restore GDM's default Wayland session, but remember
# the exact previous line so remove-kiosk.sh can put it back.
if grep -qE '^[[:space:]]*WaylandEnable[[:space:]]*=[[:space:]]*false[[:space:]]*$' "$GDM_CONF"; then
    echo "==> Enabling GDM's default Wayland session for kiosk mode."
    if [ ! -f "$WAYLAND_STATE" ]; then
        grep -m1 -E '^[[:space:]]*WaylandEnable[[:space:]]*=[[:space:]]*false[[:space:]]*$' \
            "$GDM_CONF" > "$WAYLAND_STATE"
    fi
    python3 - "$GDM_CONF" <<'PY'
import re, sys
path = sys.argv[1]
lines = open(path).readlines()
pattern = re.compile(r'^[ \t]*WaylandEnable[ \t]*=[ \t]*false[ \t]*$')
updated = [f"#{line}" if pattern.match(line.rstrip("\n")) else line for line in lines]
open(path, 'w').writelines(updated)
PY
fi

# Save the exact active autologin lines before the first setup. The file is
# intentionally created even when there were none, so a later setup run cannot
# replace the original state with the kiosk state.
if [ ! -e "$AUTOLOGIN_STATE" ]; then
    python3 - "$GDM_CONF" "$AUTOLOGIN_STATE" <<'PY'
import re, sys
path, state_path = sys.argv[1], sys.argv[2]
active = re.compile(r'^\s*AutomaticLogin(?:Enable)?\s*=')
with open(state_path, 'w') as state:
    for line in open(path):
        if active.match(line):
            state.write(line)
PY
fi

# Normalize the active values instead of only looking for one true line. This
# handles disabled entries, another autologin user and duplicate keys safely.
echo "==> Enabling GDM autologin for '${USER_NAME}'."
python3 - "$GDM_CONF" "$USER_NAME" <<'PY'
import re, sys
path, user = sys.argv[1], sys.argv[2]
lines = open(path).readlines()
active = re.compile(r'^\s*AutomaticLogin(?:Enable)?\s*=')
lines = [line for line in lines if not active.match(line)]
for index, line in enumerate(lines):
    if line.strip() == "[daemon]":
        lines[index + 1:index + 1] = [
            "AutomaticLoginEnable=true\n",
            f"AutomaticLogin={user}\n",
        ]
        break
else:
    raise SystemExit("[daemon] section not found in GDM configuration")
open(path, 'w').writelines(lines)
PY

# --- 3. Back-end autostart systemd unit -------------------------------------
# The Photo Booth pulls a container but needs no downloaded model, so waiting
# for the arduino-app-cli daemon socket is guard enough.
echo "==> Installing back-end autostart unit."
snapshot_file_once /etc/systemd/system/photo-booth-autostart.service \
    "$UNIT_BACKUP" "$UNIT_MISSING"
if [ ! -e "$UNIT_ENABLE_STATE" ]; then
    systemctl is-enabled photo-booth-autostart.service > "$UNIT_ENABLE_STATE" 2>/dev/null \
        || printf 'not-enabled\n' > "$UNIT_ENABLE_STATE"
fi
cat > /etc/systemd/system/photo-booth-autostart.service <<UNIT
[Unit]
Description=Auto-start the Photo Booth Arduino App on boot
After=arduino-app-cli.service docker.service network-online.target
Wants=arduino-app-cli.service docker.service network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
User=${USER_NAME}
Group=${USER_NAME}
# Wait for the arduino-app-cli daemon socket to be listening.
ExecStartPre=/bin/sh -c "until ss -ltn sport = :8800 | grep -q LISTEN; do sleep 1; done"
# Start the app; treat "already running" as success.
ExecStart=/bin/sh -c "arduino-app-cli app start ${APP_ID} || arduino-app-cli app list | grep -Eq \"${APP_ID}[[:space:]].*running\""
ExecStop=/usr/bin/arduino-app-cli app stop ${APP_ID}

[Install]
WantedBy=multi-user.target
UNIT
record_installed_hash /etc/systemd/system/photo-booth-autostart.service "$UNIT_HASH"
systemctl daemon-reload
systemctl enable photo-booth-autostart.service
systemctl reset-failed photo-booth-autostart.service 2>/dev/null || true

# --- 4. Chromium kiosk launcher ---------------------------------------------
echo "==> Installing kiosk launcher + GNOME autostart entry."
snapshot_file_once "${USER_HOME}/launch-booth-kiosk.sh" \
    "$LAUNCHER_BACKUP" "$LAUNCHER_MISSING"
cat > "${USER_HOME}/launch-booth-kiosk.sh" <<'LAUNCHER'
#!/bin/bash
# Photo Booth kiosk launcher script.
# Waits for the back-end application on port 7000, then opens Chromium full-screen.

# Inherit the desktop session's display when launched from GNOME autostart,
# which is the normal path. The session is not guaranteed to be :0, so only
# fall back to it when nothing is set, e.g. when run by hand from a TTY.
: "${DISPLAY:=:0}"
export DISPLAY
PORT=__PORT__

echo "Waiting for the Photo Booth back-end on port $PORT..."
while ! timeout 1 bash -c "echo > /dev/tcp/localhost/$PORT" 2>/dev/null; do
    sleep 2
done

# Wait for the window manager. GNOME autostart can fire before the compositor
# is ready, and a Chromium window mapped that early is not sized to the screen
# even with --kiosk.
for _ in $(seq 1 30); do
    pgrep -u "$(id -u)" gnome-shell >/dev/null 2>&1 && break
    sleep 1
done
sleep 3


echo "Back-end ready. Launching Chromium in kiosk mode..."
exec chromium \
    --kiosk "http://localhost:$PORT" \
    --no-first-run \
    --noerrdialogs \
    --disable-infobars \
    --disable-session-crashed-bubble \
    --disable-features=TranslateUI \
    --password-store=basic \
    --check-for-update-interval=31536000 \
    --autoplay-policy=no-user-gesture-required
LAUNCHER
sed -i "s/__PORT__/${PORT}/" "${USER_HOME}/launch-booth-kiosk.sh"
chmod +x "${USER_HOME}/launch-booth-kiosk.sh"
chown "${USER_NAME}:${USER_NAME}" "${USER_HOME}/launch-booth-kiosk.sh"
record_installed_hash "${USER_HOME}/launch-booth-kiosk.sh" "$LAUNCHER_HASH"

# --- 5. GNOME autostart entry ------------------------------------------------
mkdir -p "${USER_HOME}/.config/autostart"
chown "${USER_NAME}:${USER_NAME}" "${USER_HOME}/.config" \
    "${USER_HOME}/.config/autostart"
snapshot_file_once "${USER_HOME}/.config/autostart/photo-booth-kiosk.desktop" \
    "$DESKTOP_BACKUP" "$DESKTOP_MISSING"
cat > "${USER_HOME}/.config/autostart/photo-booth-kiosk.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Photo Booth Kiosk
Comment=Launch Chromium full-screen once the Photo Booth back-end is ready
Exec=${USER_HOME}/launch-booth-kiosk.sh
X-GNOME-Autostart-enabled=true
NoDisplay=false
Hidden=false
EOF
chown "${USER_NAME}:${USER_NAME}" \
    "${USER_HOME}/.config/autostart/photo-booth-kiosk.desktop"
record_installed_hash "${USER_HOME}/.config/autostart/photo-booth-kiosk.desktop" "$DESKTOP_HASH"

# --- 5b. No interactive dialogs on an unattended session ---------------------
# Autologin (step 2) creates a problem of its own: the login keyring is
# encrypted with the user's password, and with autologin no password is ever
# typed, so pam_gnome_keyring cannot unlock it. GNOME then puts up
# "The login keyring did not get unlocked when you logged into your computer"
# — a modal dialog on top of the kiosk, on every boot, forever.
#
# Moving the keyring makes PAM recreate it with an empty password at the next
# autologin, which unlocks silently. The original is recorded so
# remove-kiosk.sh can restore it. The kiosk browser does not need it: Chromium
# runs with --password-store=basic.
KEYRING_DIR="${USER_HOME}/.local/share/keyrings"
if [ ! -e "$KEYRING_STATE" ] && [ -f "${KEYRING_DIR}/login.keyring" ]; then
    stamp=$(date +%Y%m%d-%H%M%S)
    backup="${KEYRING_DIR}/login.keyring.bak-${stamp}"
    echo "==> Clearing the login keyring so autologin can unlock it"
    echo "    (backed up to ${backup})"
    mv "${KEYRING_DIR}/login.keyring" "$backup"
    chown "${USER_NAME}:${USER_NAME}" "$backup"
    printf '%s\n' "$backup" > "$KEYRING_STATE"
elif [ ! -e "$KEYRING_STATE" ]; then
    # Empty means there was no login keyring to restore before setup.
    : > "$KEYRING_STATE"
fi

# update-notifier runs a pkexec helper on login, which raises a polkit password
# dialog of its own. An unattended screen has nobody to answer it.
UPDATE_NOTIFIER="${USER_HOME}/.config/autostart/update-notifier.desktop"
if [ ! -e "$UPDATE_NOTIFIER_STATE" ] && [ ! -e "$UPDATE_NOTIFIER_MISSING" ]; then
    if [ -L "$UPDATE_NOTIFIER" ]; then
        echo "!! Refusing to replace symbolic link: ${UPDATE_NOTIFIER}" >&2
        exit 1
    elif [ -e "$UPDATE_NOTIFIER" ]; then
        cp -a "$UPDATE_NOTIFIER" "$UPDATE_NOTIFIER_STATE"
    else
        touch "$UPDATE_NOTIFIER_MISSING"
    fi
fi
mkdir -p "${USER_HOME}/.config/autostart"
cat > "${USER_HOME}/.config/autostart/update-notifier.desktop" <<'EOF'
[Desktop Entry]
Type=Application
Name=Update Notifier
Exec=/bin/true
Hidden=true
X-GNOME-Autostart-enabled=false
EOF
chown "${USER_NAME}:${USER_NAME}" "${USER_HOME}/.config/autostart/update-notifier.desktop"
record_installed_hash "$UPDATE_NOTIFIER" "$UPDATE_NOTIFIER_HASH"
echo "==> Suppressed update-notifier's polkit prompt for '${USER_NAME}'."

# --- 6. Never sleep, never blank ---------------------------------------------
# A booth that suspends or blanks after 5 minutes is not a booth. Two layers,
# because either one alone leaves a hole: systemd can still suspend the board
# even when GNOME is told not to idle, and GNOME will blank the screen even on a
# board that never suspends.
echo "==> Disabling sleep, idle blanking and screen lock."

# Layer 1: the machine must never suspend or hibernate.
if [ ! -e "$SLEEP_STATE" ]; then
    for target in sleep.target suspend.target hibernate.target hybrid-sleep.target; do
        state="$(systemctl is-enabled "$target" 2>/dev/null || true)"
        if [ "$state" = "masked" ]; then
            printf '%s\n' "$target" >> "$SLEEP_STATE"
        fi
    done
    # Preserve an empty original state as well.
    touch "$SLEEP_STATE"
fi
systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target \
    >/dev/null 2>&1 || true

# Layer 2: GNOME. Written as a system-wide dconf default rather than gsettings,
# because gsettings needs a live session bus for the target user and there is no
# session yet when this script runs.
mkdir -p /etc/dconf/db/local.d
cat > /etc/dconf/db/local.d/00-photo-booth-kiosk <<'DCONF'
# Installed by the Photo Booth bundle (setup-kiosk.sh). Removed by remove-kiosk.sh.
[org/gnome/desktop/session]
idle-delay=uint32 0

[org/gnome/desktop/screensaver]
lock-enabled=false
idle-activation-enabled=false

[org/gnome/settings-daemon/plugins/power]
sleep-inactive-ac-type='nothing'
sleep-inactive-battery-type='nothing'
idle-dim=false
DCONF

# The local db is only consulted if the user profile references it.
if [ ! -f /etc/dconf/profile/user ]; then
    if [ ! -e "$DCONF_PROFILE_STATE" ]; then printf 'created\n' > "$DCONF_PROFILE_STATE"; fi
    printf 'user-db:user\nsystem-db:local\n' > /etc/dconf/profile/user
elif ! grep -q '^system-db:local$' /etc/dconf/profile/user; then
    if [ ! -e "$DCONF_PROFILE_STATE" ]; then printf 'appended\n' > "$DCONF_PROFILE_STATE"; fi
    printf 'system-db:local\n' >> /etc/dconf/profile/user
elif [ ! -e "$DCONF_PROFILE_STATE" ]; then
    printf 'unchanged\n' > "$DCONF_PROFILE_STATE"
fi
dconf update 2>/dev/null || true

echo
echo "==> Kiosk configured."
echo "    App           : ${APP_ID}"
echo "    Back-end unit : photo-booth-autostart.service (enabled)"
echo "    Desktop       : Wayland kiosk session"
echo "    Sleep/blanking: disabled (sleep targets masked, GNOME idle off)"
echo
echo "    The Photo Booth also needs the print server running on the host;"
echo "    see print-server/README.md if you have not installed it yet."
echo "    Reboot to verify the full kiosk comes up hands-off:  sudo reboot"
