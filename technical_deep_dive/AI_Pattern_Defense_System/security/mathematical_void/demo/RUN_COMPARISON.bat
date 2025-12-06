@echo off
echo ================================================================================
echo   VOID DEMO - Side-by-Side Comparison (BEST DEMO!)
echo ================================================================================
echo.
echo This sends IDENTICAL queries as creator and attacker.
echo You'll see they get DIFFERENT results from the SAME endpoint.
echo.
echo This is the PROOF that void protection works!
echo.
echo Make sure the server is running first (run START_SERVER.bat in another window).
echo.
pause

python demo_comparison.py

echo.
echo ================================================================================
echo   Demo Complete - Check the results above!
echo ================================================================================
pause
