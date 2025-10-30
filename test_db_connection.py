import os
import sys
from database import get_db
from core.config import settings

def test_database_connection():
    print("Testing database connection...")
    print("Database URL:", settings.DATABASE_URL)

    try:
        # Get a database session
        db_generator = get_db()
        db = next(db_generator)
        
        # Try a simple query to verify connection
        result = db.execute("SELECT 1")
        print("Database connection successful!")
        print("Test query result:", result.scalar())
        
        # Close the connection properly
        try:
            next(db_generator)
        except StopIteration:
            pass
        
    except Exception as e:
        print("Error connecting to database:", str(e))

if __name__ == "__main__":
    test_database_connection()