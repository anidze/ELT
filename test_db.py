import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5433")
DB_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    
   
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("კავშირი დამყარდა! მონაცემთა ბაზის ვერსია:")
        print(result.fetchone()[0])
        
except Exception as e:
    print(f"შეცდომა კავშირის დროს: {e}")