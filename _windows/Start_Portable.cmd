@echo off
SET __COMPAT_LAYER=WINXPSP3
set __COMPAT_LAYER=RunAsInvoker
call :check_Permissions
if "%ADMIN%"=="FAIL" goto :EOF


TASKKILL /im pulsar.exe /f
tskill pulsar.exe
TASKKILL /im Kodi.exe /f
tskill Kodi.exe
TASKKILL /im XBMC.exe /f
tskill XBMC.exe

start Kodi.exe -p



:check_Permissions
   :: net session >nul 2>&1
   :: sfc 2>&1 | find /i "/SCANNOW"
    fsutil dirty query %systemdrive% >nul
    if not errorLevel 1 (
        echo Administrative permissions confirmed.
    ) else (
        echo Sorry - you need to run as Administrator [use right-click - Run as administrator].
		echo.
	color cf
	pause
	Set ADMIN=FAIL
    )
goto :eof

