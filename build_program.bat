@echo off
cls
color 02
echo Building...
timeout /t 1 /nobreak > NUL
cls
color 04
echo Debug Messages:
color 08
"C:\Program Files (x86)\Python37-32\python.exe" setup.py bdist_msi
cls
color 02
echo Complete.
pause