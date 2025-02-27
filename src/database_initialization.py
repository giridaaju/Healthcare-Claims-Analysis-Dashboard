import sqlite3
import os

def create_database(db_path="healthcare_claims.db"):

    try:
        
        if os.path.exists(db_path):
            print(f"Database already exists at {db_path}")
            return False
        
    
    except Exception as e:
        print(f"Error creating database: {e}")
        return False