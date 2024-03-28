#!/usr/bin/osascript

set output to ""
tell application "Google Chrome"
        set numWindows to count of windows
        repeat with i from 1 to numWindows
                set numTabs to count of tabs of window i
                repeat with j from 1 to numTabs
                        set tabUrl to get URL of tab j of window i
                        set output to output & tabUrl & "\n"
                end repeat
        end repeat
end tell
copy output to stdout
