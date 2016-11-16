@echo off
rem http://stackoverflow.com/questions/7727114/batch-command-date-and-time-in-file-name/7730453#7730453
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /format:list') do set datetime=%%I
echo %datetime%
