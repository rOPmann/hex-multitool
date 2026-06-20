@echo off
title HEX Installer

color 07

echo ==========================================
echo               HEX INSTALLER
echo ==========================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
color 0C
echo [ERROR] Python was not found on this system.
echo Please install Python and enable "Add Python to PATH".
echo.
pause
exit /b 1
)

echo [INFO] Python detected.
echo.

echo [INFO] Checking required packages...
echo.

pip install -q pystyle py-cpuinfo GPUtil qrcode Pillow phonenumbers python-whois requests pyperclip

if errorlevel 1 (
color 0C
echo.
echo.
echo.
echo.
echo ==========================================
echo ERROR: Package installation failed
echo ==========================================
echo.
pause
exit /b 1
)

color 0A
echo.
echo.
echo.
echo.
echo ==========================================
echo      HEX INSTALLATION COMPLETED
echo ==========================================
echo All required packages are installed.
echo.

pause
