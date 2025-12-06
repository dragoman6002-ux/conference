@echo off
echo ================================================================================
echo   VOID DEMO - Legitimate Client (Creator)
echo ================================================================================
echo.
echo This will run the legitimate client with creator credentials.
echo Make sure the server is running first (run START_SERVER.bat in another window).
echo.
pause

python demo_creator.py

echo.
echo ================================================================================
echo   Demo Complete
echo ================================================================================
pause
