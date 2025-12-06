@echo off
echo ================================================================================
echo   VOID DEMO - Automated Tests
echo ================================================================================
echo.
echo This will validate all functionality automatically.
echo.
echo Make sure the server is running first (run START_SERVER.bat in another window).
echo.
echo Tests will run automatically (no user input needed).
echo.
pause

python -c "import sys; sys.argv = ['demo_test_auto.py']; exec(open('demo_test_auto.py').read())"

echo.
echo ================================================================================
echo   Tests Complete
echo ================================================================================
pause
