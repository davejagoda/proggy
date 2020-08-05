#!/usr/bin/osascript
tell application "Firefox" to return count (every window whose (closeable is true))
