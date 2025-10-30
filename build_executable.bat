@echo off
echo ========================================
echo Building Weather App Executable
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
echo Checking for PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: Failed to install PyInstaller!
        pause
        exit /b 1
    )
)

echo.
echo Creating executable...
echo This may take a few moments...
echo.

REM Build the executable (onefile = single exe, windowed = no console window)
pyinstaller --onefile --windowed --name "WeatherApp" app.py weather.py

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    echo Check the error messages above.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build Complete! SUCCESS!
echo ========================================
echo.
echo Your standalone executable is ready:
echo   dist\WeatherApp.exe
echo.
echo ========================================
echo HOW TO SHARE WITH FRIENDS:
echo ========================================
echo.
echo Step 1: IMPORTANT - Set your API key in app.py first!
echo          Open app.py and replace "YOUR_API_KEY_HERE" 
echo          with your actual API key (line 7)
echo          Get free API key from: https://openweathermap.org/api
echo.
echo Step 2: Build again after setting your API key
echo.
echo Step 3: Share the WeatherApp.exe file - that's all you need!
echo          Just send the .exe file to your friends.
echo          They just double-click to run - no setup needed!
echo.
echo NOTE: Your friends do NOT need:
echo       - Python installed
echo       - API key setup
echo       - Any other files
echo       Just the .exe file!
echo.
echo ========================================
pause

