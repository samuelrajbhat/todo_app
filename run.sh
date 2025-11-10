#!/bin/bash

echo "🔧 Running Alembic migrations..."
alembic upgrade head

echo "🚀 Starting Celery worker..."
# Adjust module path as needed (e.g. tasks.task:celery)
celery -A tasks.task worker --loglevel=info &

# Optional: if you use Celery Beat for periodic tasks
# echo "⏰ Starting Celery Beat..."
# celery -A tasks.task beat --loglevel=info &

echo "⚡ Starting FastAPI app..."
uvicorn main:app --reload
