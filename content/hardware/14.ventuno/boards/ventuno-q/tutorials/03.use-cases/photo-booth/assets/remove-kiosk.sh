#!/bin/bash
# Undo setup-kiosk.sh: put the board back to a normal desktop that does not boot
# into the Photo Booth.
#
# Removes, idempotently:
#   1. the back-end autostart unit (photo-booth-autostart.service)
#   2. the Chromium kiosk launcher + GNOME autostart entries
#   3. the GDM automatic-login lines and any X11 setting changed for the kiosk
#   4. the sleep / idle-blanking overrides
#
# Run on the board:  sudo bash remove-kiosk.sh
#
# It deliberately leaves alone:
#   - the app itself, which stays installed and running (STOP_APP=1 to stop it)
#   - the print server on the host
#   - Chromium (REMOVE_CHROMIUM=1 to uninstall the snap this setup installed)
#
# A kiosk Chromium that is on screen right now keeps running; it is gone after
# the next reboot.

set -euo pipefail

USER_NAME="${KIOSK_USER:-arduino}"
USER_HOME="/home/${USER_NAME}"
UNIT=photo-booth-autostart.service
UNIT_PATH="/etc/systemd/system/${UNIT}"
GDM_CONF=/etc/gdm3/custom.conf
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

removed_any=false

installed_file_is_current() {
    local path="$1" hash_file="$2"
    [ -f "$path" ] && [ -s "$hash_file" ] \
        && [ "$(sha256sum "$path" | cut -d ' ' -f1)" = "$(head -1 "$hash_file")" ]
}

restore_managed_file() {
    local path="$1" backup="$2" missing="$3" hash_file="$4" label="$5"
    if installed_file_is_current "$path" "$hash_file"; then
        if [ -e "$backup" ]; then
            cp -a "$backup" "$path"
            echo "==> Restored the pre-kiosk ${label}"
        elif [ -e "$missing" ]; then
            rm -f "$path"
            echo "==> Removed the kiosk-owned ${label}"
        fi
        removed_any=true
    elif [ -e "$hash_file" ]; then
        echo "==> Preserving the user-managed ${label}"
    fi
    rm -f "$backup" "$missing" "$hash_file"
}

# Bundles published before state snapshots were added can still be removed.
# Their original autologin and sleep state is unknowable, so the legacy path is
# intentionally narrow and runs only when the old kiosk unit is present and no
# autologin snapshot exists.
legacy_install=false
if [ ! -e "$AUTOLOGIN_STATE" ] && [ -f "$UNIT_PATH" ]; then
    legacy_install=true
fi

# --- 1. autostart unit -------------------------------------------------------
unit_owned=false
legacy_unit_owned=false
if [ "$legacy_install" = true ] && [ -f "$UNIT_PATH" ] \
    && grep -qF 'Description=Auto-start the Photo Booth Arduino App on boot' "$UNIT_PATH" \
    && grep -qF 'arduino-app-cli app start user:photo-booth' "$UNIT_PATH"; then
    legacy_unit_owned=true
fi
if [ "$legacy_unit_owned" = true ] || installed_file_is_current "$UNIT_PATH" "$UNIT_HASH"; then
    unit_owned=true
fi

if [ "$unit_owned" = true ]; then
    echo "==> Removing ${UNIT}"
    systemctl disable "$UNIT" >/dev/null 2>&1 || true

    if [ "${STOP_APP:-0}" = "1" ]; then
        # `systemctl stop` runs the unit's ExecStop, which stops the app.
        echo "    STOP_APP=1 — stopping the app as well"
        systemctl stop "$UNIT" >/dev/null 2>&1 || true
    else
        echo "    leaving the app running (STOP_APP=1 to stop it)"
        # The unit is Type=oneshot RemainAfterExit=yes, so it sits "active" and
        # simply deleting the file would leave it loaded as not-found until the
        # next boot. Stop it properly, but neuter ExecStop first so stopping the
        # unit does not stop the app. The drop-in lives in /run, so an
        # interrupted run leaves nothing behind.
        DROPIN="/run/systemd/system/${UNIT}.d"
        mkdir -p "$DROPIN"
        printf '[Service]\nExecStop=\n' > "${DROPIN}/zz-remove-kiosk.conf"
        systemctl daemon-reload
        systemctl stop "$UNIT" >/dev/null 2>&1 || true
        rm -rf "$DROPIN"
    fi

    if [ "$legacy_unit_owned" = true ]; then
        rm -f "$UNIT_PATH"
    else
        restore_managed_file "$UNIT_PATH" "$UNIT_BACKUP" "$UNIT_MISSING" \
            "$UNIT_HASH" "Photo Booth systemd unit"
    fi
    systemctl daemon-reload
    if [ -s "$UNIT_ENABLE_STATE" ] && [ -f "$UNIT_PATH" ]; then
        case "$(head -1 "$UNIT_ENABLE_STATE")" in
            enabled) systemctl enable "$UNIT" >/dev/null 2>&1 || true ;;
            masked) systemctl mask "$UNIT" >/dev/null 2>&1 || true ;;
            *) systemctl disable "$UNIT" >/dev/null 2>&1 || true ;;
        esac
    fi
    rm -f "$UNIT_ENABLE_STATE"
    systemctl reset-failed "$UNIT" >/dev/null 2>&1 || true
    removed_any=true
else
    if [ -e "$UNIT_HASH" ]; then
        restore_managed_file "$UNIT_PATH" "$UNIT_BACKUP" "$UNIT_MISSING" \
            "$UNIT_HASH" "Photo Booth systemd unit"
        rm -f "$UNIT_ENABLE_STATE"
    else
        echo "==> ${UNIT} not present."
    fi
fi

# --- 2. kiosk launcher + GNOME autostart entries -----------------------------
if [ -e "$LAUNCHER_HASH" ]; then
    restore_managed_file "${USER_HOME}/launch-booth-kiosk.sh" \
        "$LAUNCHER_BACKUP" "$LAUNCHER_MISSING" "$LAUNCHER_HASH" "kiosk launcher"
elif [ "$legacy_install" = true ]; then
    legacy_launcher="${USER_HOME}/launch-booth-kiosk.sh"
    if [ -f "$legacy_launcher" ] \
        && grep -qF 'Photo Booth kiosk launcher script.' "$legacy_launcher" \
        && grep -qF -- '--kiosk "http://localhost:$PORT"' "$legacy_launcher"; then
        rm -f "$legacy_launcher"
    fi
fi

if [ -e "$DESKTOP_HASH" ]; then
    restore_managed_file "${USER_HOME}/.config/autostart/photo-booth-kiosk.desktop" \
        "$DESKTOP_BACKUP" "$DESKTOP_MISSING" "$DESKTOP_HASH" "kiosk desktop entry"
elif [ "$legacy_install" = true ]; then
    legacy_desktop="${USER_HOME}/.config/autostart/photo-booth-kiosk.desktop"
    if [ -f "$legacy_desktop" ] \
        && grep -qxF 'Name=Photo Booth Kiosk' "$legacy_desktop" \
        && grep -qF 'launch-booth-kiosk.sh' "$legacy_desktop"; then
        rm -f "$legacy_desktop"
    fi
fi

# Restore the user's update-notifier override if setup replaced one. If there
# was no override before setup, remove only the kiosk-created file.
UPDATE_NOTIFIER="${USER_HOME}/.config/autostart/update-notifier.desktop"
if [ -e "$UPDATE_NOTIFIER_STATE" ] || [ -e "$UPDATE_NOTIFIER_MISSING" ]; then
    if installed_file_is_current "$UPDATE_NOTIFIER" "$UPDATE_NOTIFIER_HASH"; then
        if [ -e "$UPDATE_NOTIFIER_STATE" ]; then
            echo "==> Restoring the previous update-notifier desktop entry"
            mkdir -p "$(dirname "$UPDATE_NOTIFIER")"
            cp -a "$UPDATE_NOTIFIER_STATE" "$UPDATE_NOTIFIER"
        else
            echo "==> Removing the kiosk update-notifier override"
            rm -f "$UPDATE_NOTIFIER"
        fi
        removed_any=true
    elif [ -e "$UPDATE_NOTIFIER_HASH" ]; then
        echo "==> Preserving the user-managed update-notifier desktop entry"
    fi
    rm -f "$UPDATE_NOTIFIER_STATE" "$UPDATE_NOTIFIER_MISSING" "$UPDATE_NOTIFIER_HASH"
elif [ "$legacy_install" = true ] && [ -f "$UPDATE_NOTIFIER" ] \
     && grep -qxF 'Exec=/bin/true' "$UPDATE_NOTIFIER" \
     && grep -qxF 'Hidden=true' "$UPDATE_NOTIFIER" \
     && grep -qxF 'X-GNOME-Autostart-enabled=false' "$UPDATE_NOTIFIER"; then
    echo "==> Removing the legacy kiosk update-notifier override"
    rm -f "$UPDATE_NOTIFIER"
    removed_any=true
fi

# --- 3. GDM autologin --------------------------------------------------------
# Restore the exact active lines saved by setup, but only while the current
# values are still the canonical kiosk values. Preserve any later user change.
if [ -e "$AUTOLOGIN_STATE" ] && [ -f "$GDM_CONF" ]; then
    restore_result="$(python3 - "$GDM_CONF" "$AUTOLOGIN_STATE" "$USER_NAME" <<'PY'
import re, sys
path, state_path, user = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(path).readlines()
active = re.compile(r'^\s*(AutomaticLogin(?:Enable)?)\s*=\s*(.*?)\s*$')
current = []
for line in lines:
    match = active.match(line)
    if match:
        current.append((match.group(1), match.group(2)))

expected = [
    ("AutomaticLoginEnable", "true"),
    ("AutomaticLogin", user),
]
if current != expected:
    print("preserved")
    raise SystemExit

lines = [line for line in lines if not active.match(line)]
saved = open(state_path).readlines()
for index, line in enumerate(lines):
    if line.strip() == "[daemon]":
        lines[index + 1:index + 1] = saved
        break
else:
    raise SystemExit("[daemon] section not found in GDM configuration")
open(path, 'w').writelines(lines)
print("restored")
PY
    )"
    if [ "$restore_result" = "restored" ]; then
        echo "==> Restored the pre-kiosk GDM autologin configuration"
    else
        echo "==> Preserving the current user-managed GDM autologin configuration"
    fi
    rm -f "$AUTOLOGIN_STATE"
    removed_any=true
else
    if [ "$legacy_install" = true ] && [ -f "$GDM_CONF" ]; then
        legacy_result="$(python3 - "$GDM_CONF" "$USER_NAME" <<'PY'
import re, sys
path, user = sys.argv[1], sys.argv[2]
lines = open(path).readlines()
active = re.compile(r'^\s*(AutomaticLogin(?:Enable)?)\s*=\s*(.*?)\s*$')
current = []
for line in lines:
    match = active.match(line)
    if match:
        current.append((match.group(1), match.group(2)))
expected = [("AutomaticLoginEnable", "true"), ("AutomaticLogin", user)]
if current == expected:
    open(path, "w").writelines(line for line in lines if not active.match(line))
    print("removed")
else:
    print("preserved")
PY
        )"
        if [ "$legacy_result" = "removed" ]; then
            echo "==> Removed the legacy kiosk GDM autologin values"
            removed_any=true
        else
            echo "==> Preserving the current user-managed GDM autologin configuration"
        fi
    else
        echo "==> No saved GDM autologin state."
    fi
fi

# Restore an explicit WaylandEnable=false line only when setup-kiosk.sh changed
# it and nobody has since added a new active WaylandEnable setting.
if [ -f "$WAYLAND_STATE" ] && [ -f "$GDM_CONF" ]; then
    restore_result="$(python3 - "$GDM_CONF" "$WAYLAND_STATE" <<'PY'
import re, sys
path, state_path = sys.argv[1], sys.argv[2]
original = open(state_path).read().rstrip("\n")
lines = open(path).readlines()
active = re.compile(r'^[ \t]*WaylandEnable[ \t]*=')
commented_false = re.compile(r'^[ \t]*#[ \t]*WaylandEnable[ \t]*=[ \t]*false[ \t]*$')

if any(active.match(line) for line in lines):
    print("preserved")
else:
    for index, line in enumerate(lines):
        if commented_false.match(line.rstrip("\n")):
            lines[index] = original + "\n"
            break
    else:
        for index, line in enumerate(lines):
            if line.strip() == "[daemon]":
                lines.insert(index + 1, original + "\n")
                break
    open(path, 'w').writelines(lines)
    print("restored")
PY
)"
    if [ "$restore_result" = "restored" ]; then
        echo "==> Restored the pre-kiosk GDM X11 setting"
    else
        echo "==> Preserving the current user-managed WaylandEnable setting"
    fi
    rm -f "$WAYLAND_STATE"
    removed_any=true
fi

# --- 4. sleep / blanking -----------------------------------------------------
# Only undo what setup-kiosk.sh did: restore the sleep-target mask state, drop
# our dconf file and reverse our profile edit.
if [ -f /etc/dconf/db/local.d/00-photo-booth-kiosk ]; then
    echo "==> Re-enabling sleep and idle blanking"
    rm -f /etc/dconf/db/local.d/00-photo-booth-kiosk
    dconf update 2>/dev/null || true
    removed_any=true
fi
# Unmask only targets that setup newly masked. Targets listed in the state file
# were already masked and must remain so.
if [ -e "$SLEEP_STATE" ]; then
    for target in sleep.target suspend.target hibernate.target hybrid-sleep.target; do
        if ! grep -Fxq "$target" "$SLEEP_STATE"; then
            state="$(systemctl is-enabled "$target" 2>/dev/null || true)"
            if [ "$state" = "masked" ]; then
                echo "==> Restoring ${target} to its pre-kiosk unmasked state"
                systemctl unmask "$target" >/dev/null 2>&1 || true
            fi
        fi
    done
    rm -f "$SLEEP_STATE"
    removed_any=true
elif [ "$legacy_install" = true ]; then
    echo "==> Removing legacy kiosk sleep-target masks (no prior state was recorded)"
    for target in sleep.target suspend.target hibernate.target hybrid-sleep.target; do
        state="$(systemctl is-enabled "$target" 2>/dev/null || true)"
        if [ "$state" = "masked" ]; then
            systemctl unmask "$target" >/dev/null 2>&1 || true
        fi
    done
    removed_any=true
fi

# Undo only the profile edit setup made. If the profile was subsequently
# changed, keep it and report that choice instead of overwriting user state.
if [ -e "$DCONF_PROFILE_STATE" ]; then
    profile_action="$(head -1 "$DCONF_PROFILE_STATE")"
    case "$profile_action" in
        created)
            if [ "$(cat /etc/dconf/profile/user 2>/dev/null || true)" = $'user-db:user\nsystem-db:local' ]; then
                rm -f /etc/dconf/profile/user
            else
                echo "==> Preserving the modified dconf user profile"
            fi
            ;;
        appended)
            if [ -f /etc/dconf/profile/user ]; then
                python3 - /etc/dconf/profile/user <<'PY'
import sys
path = sys.argv[1]
lines = open(path).readlines()
removed = False
kept = []
for line in lines:
    if not removed and line.rstrip("\n") == "system-db:local":
        removed = True
        continue
    kept.append(line)
open(path, "w").writelines(kept)
PY
            fi
            ;;
    esac
    rm -f "$DCONF_PROFILE_STATE"
    removed_any=true
fi

# Restore the password-protected login keyring that setup moved aside. Preserve
# any keyring created during kiosk use under a new backup name.
if [ -e "$KEYRING_STATE" ]; then
    keyring_backup="$(head -1 "$KEYRING_STATE")"
    if [ -n "$keyring_backup" ] && [ -f "$keyring_backup" ]; then
        KEYRING_DIR="${USER_HOME}/.local/share/keyrings"
        if [ -f "${KEYRING_DIR}/login.keyring" ]; then
            stamp=$(date +%Y%m%d-%H%M%S)
            kiosk_backup="${KEYRING_DIR}/login.keyring.kiosk-${stamp}"
            mv "${KEYRING_DIR}/login.keyring" "$kiosk_backup"
            echo "==> Preserved the kiosk-session keyring at ${kiosk_backup}"
        fi
        mv "$keyring_backup" "${KEYRING_DIR}/login.keyring"
        chown "${USER_NAME}:${USER_NAME}" "${KEYRING_DIR}/login.keyring"
        echo "==> Restored the pre-kiosk login keyring"
    fi
    rm -f "$KEYRING_STATE"
    removed_any=true
fi

# --- 5. Chromium (opt-in) ----------------------------------------------------
if [ "${REMOVE_CHROMIUM:-0}" = "1" ]; then
    if [ -e "$CHROMIUM_INSTALLED_STATE" ] && snap list chromium >/dev/null 2>&1; then
        echo "==> Removing the Chromium snap installed by setup-kiosk.sh"
        snap remove chromium
        rm -f "$CHROMIUM_INSTALLED_STATE"
        removed_any=true
    elif [ -e "$CHROMIUM_INSTALLED_STATE" ]; then
        rm -f "$CHROMIUM_INSTALLED_STATE"
    elif [ ! -e "$CHROMIUM_INSTALLED_STATE" ]; then
        echo "==> Keeping Chromium: setup-kiosk.sh did not record installing it."
    fi
fi

rmdir "$STATE_DIR" 2>/dev/null || true

echo
if [ "$removed_any" = true ]; then
    echo "==> Kiosk removed. Reboot to come up at the normal login screen:  sudo reboot"
else
    echo "==> Nothing to remove — this board was not configured as a kiosk."
fi
