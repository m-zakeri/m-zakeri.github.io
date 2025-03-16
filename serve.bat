pelican content
REM cd output
timeout /t 5
START "" "http://127.0.0.1:8000"
pelican --listen
REM Ctrl-C to quit