@echo off
chcp 65001 >nul
set /p version=버전명을 입력하세요 (예: 1.0): 

python -m PyInstaller --noconsole --onefile main.py
python make_zip.py %version%

pause
