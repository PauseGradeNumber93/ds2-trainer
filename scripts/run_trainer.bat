@echo off
setlocal
if not exist ".venv\Scripts\python.exe" (
    echo [ds2-trainer] creating venv...
    python -m venv .venv
    .venv\Scripts\python.exe -m pip install -r requirements.txt
)
.venv\Scripts\python.exe -m ds2_trainer.bootstrap
endlocal