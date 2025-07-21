@echo off
cd /d "%~dp0"
powershell -Command "Start-Process python '.\web_blocker.py' -Verb RunAs"
