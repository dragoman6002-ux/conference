@echo off
cls
:menu
echo.
echo ================================================================================
echo                 VOID PROTECTION DEMO - MAIN MENU (Windows)
echo ================================================================================
echo.
echo   Real network demonstration of void-protected API system
echo.
echo ================================================================================
echo   AVAILABLE DEMOS:
echo ================================================================================
echo.
echo   [1] Start Server (do this FIRST!)
echo   [2] Run Legitimate Client (Creator with credentials)
echo   [3] Run Attacker (Model extraction attempt)
echo   [4] Run Side-by-Side Comparison (BEST DEMO!)
echo   [5] Run Automated Tests
echo   [6] Open Dashboard in Browser
echo   [7] View Quick Instructions
echo   [8] Exit
echo.
echo ================================================================================

set /p choice="Enter your choice (1-8): "

if "%choice%"=="1" goto server
if "%choice%"=="2" goto creator
if "%choice%"=="3" goto attacker
if "%choice%"=="4" goto comparison
if "%choice%"=="5" goto tests
if "%choice%"=="6" goto dashboard
if "%choice%"=="7" goto instructions
if "%choice%"=="8" goto end

echo Invalid choice. Please try again.
timeout /t 2 >nul
goto menu

:server
cls
echo.
echo Starting server...
echo.
echo IMPORTANT: This window must stay open!
echo The server will run in this window.
echo.
echo To run demos, open NEW Command Prompt windows and run:
echo   - RUN_COMPARISON.bat (recommended first!)
echo   - RUN_CREATOR.bat
echo   - RUN_ATTACKER.bat
echo.
echo Press Ctrl+C to stop the server when done.
echo.
pause
python demo_server.py
pause
goto end

:creator
cls
python demo_creator.py
pause
goto menu

:attacker
cls
python demo_attacker.py
pause
goto menu

:comparison
cls
python demo_comparison.py
pause
goto menu

:tests
cls
python demo_test_auto.py
pause
goto menu

:dashboard
cls
echo.
echo Opening dashboard in your default browser...
echo.
echo If it doesn't open automatically, navigate to:
echo   http://localhost:8000
echo.
start http://localhost:8000
timeout /t 3 >nul
goto menu

:instructions
cls
echo.
echo ================================================================================
echo   QUICK INSTRUCTIONS
echo ================================================================================
echo.
echo STEP 1: Start the Server
echo   - Choose option [1] from the main menu
echo   - Server starts on http://localhost:8000
echo   - Keep this window open!
echo.
echo STEP 2: Open Dashboard (Optional)
echo   - Open browser: http://localhost:8000
echo   - See live statistics updating
echo.
echo STEP 3: Run Demonstrations
echo   - Open NEW Command Prompt windows
echo   - Run this script again (RUN_DEMO.bat)
echo   - Or double-click individual batch files:
echo     * RUN_COMPARISON.bat (recommended first!)
echo     * RUN_CREATOR.bat
echo     * RUN_ATTACKER.bat
echo     * RUN_TESTS.bat
echo.
echo BEST DEMO SEQUENCE:
echo   1. Start server (option 1)
echo   2. Open dashboard in browser (option 6)
echo   3. Run comparison (option 4) - Shows proof!
echo   4. Run attacker (option 3) - Shows detection!
echo   5. Run tests (option 5) - Validates everything!
echo.
echo WHAT YOU'LL SEE:
echo   - Server window: Detection logs in real-time
echo   - Client windows: Query results
echo   - Dashboard: Live statistics
echo.
echo ================================================================================
echo.
pause
goto menu

:end
cls
echo.
echo Thank you for using the Void Protection Demo!
echo.
timeout /t 2 >nul
exit /b
