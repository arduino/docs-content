#!/bin/bash
# Smart Mirror kiosk launcher script.
# Waits for the back-end application on port 7000, then opens Chromium full-screen.

# Inherit the desktop session's display when launched from GNOME autostart,
# which is the normal path. The session is not guaranteed to be :0, so only
# fall back to it when nothing is set, e.g. when run by hand from a TTY.
: "${DISPLAY:=:0}"
export DISPLAY
PORT=7000

echo "Waiting for the Smart Mirror back-end on port $PORT..."
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
