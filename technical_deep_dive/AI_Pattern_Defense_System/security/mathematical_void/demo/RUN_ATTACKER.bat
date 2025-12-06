@echo off
echo ================================================================================
echo   VOID DEMO - Attacker (Model Extraction Attempt)
echo ================================================================================
echo.
echo This will simulate a sophisticated model extraction attack.
echo Make sure the server is running first (run START_SERVER.bat in another window).
echo.
echo WATCH THE SERVER WINDOW to see:
echo   - Detection of systematic patterns
echo   - Threat scoring in action
echo   - Requests routed to decoy model
echo.
pause

python demo_attacker.py

echo.
echo ================================================================================
echo   Demo Complete
echo ================================================================================
pause
