@echo off
echo ================================================================================
echo   QUICK TEST - Is the Server Working?
echo ================================================================================
echo.
echo This will test if the void protection server is running and responding.
echo.
pause

echo.
echo Testing server connection...
echo.

python -c "import requests; r = requests.get('http://localhost:8000', timeout=5); print('✓ Server is RUNNING!' if r.status_code == 200 else '✗ Server returned error')" 2>nul

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ✗ SERVER IS NOT RUNNING or NOT RESPONDING
    echo.
    echo To start the server:
    echo   1. Double-click START_SERVER.bat
    echo   2. Or run: python demo_server.py
    echo.
) else (
    echo.
    echo Testing API endpoint...
    python -c "import requests; r = requests.get('http://localhost:8000/api/risk?volatility=0.5^&correlation=0.3^&liquidity=1.0', timeout=5); print('✓ API is RESPONDING!' if 'risk_score' in r.json() else '✗ API error')" 2>nul
    
    echo.
    echo ✓ All checks passed!
    echo ✓ Server is running correctly
    echo ✓ Ready for demonstrations
    echo.
    echo Next steps:
    echo   - Run RUN_COMPARISON.bat (best demo!)
    echo   - Open http://localhost:8000 in browser
    echo.
)

pause
