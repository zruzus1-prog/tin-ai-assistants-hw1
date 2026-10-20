@echo off
setlocal
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
set "HW1_PY=..\work\venv\Scripts\python.exe"
if not exist "%HW1_PY%" set "HW1_PY=.venv\Scripts\python.exe"
if not exist "%HW1_PY%" set "HW1_PY=python"
"%HW1_PY%" checks\check.py all
if errorlevel 1 goto fail
"%HW1_PY%" checks\replay_search.py
if errorlevel 1 goto fail
echo.
echo Technical checks passed. Student review is checked separately:
"%HW1_PY%" checks\submission_ready.py
set "HW1_RESULT=%ERRORLEVEL%"
pause
exit /b %HW1_RESULT%
:fail
echo A technical check failed. Read the output above.
pause
exit /b 1
