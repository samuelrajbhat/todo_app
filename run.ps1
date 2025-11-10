Write-Host "🔧 Running Alembic migrations..."
.venv\Scripts\alembic upgrade head

Write-Host "🚀 Starting Celery worker..."
Start-Process -NoNewWindow -FilePath ".venv\Scripts\celery.exe" -ArgumentList "-A tasks.task:celery_app worker --loglevel=info -P solo"

Write-Host "⚡ Starting FastAPI app..."
.venv\Scripts\uvicorn main:app --reload
