@echo off
REM Activate venv then run uvicorn (adjust path if needed)
call .venv\Scripts\activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
