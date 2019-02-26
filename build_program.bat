@echo off
cls
color 02
echo Building...
timeout /t 1 /nobreak > NUL
cls
color 04
echo Debug Messages:
color 08
python setup.py bdist_msi
cls
color 02
echo Complete.
pause