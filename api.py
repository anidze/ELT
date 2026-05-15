import os
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# კავშირი ბაზასთან
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT', '5433')}"
    f"/{os.getenv('POSTGRES_DB')}"
)
engine = create_engine(DATABASE_URL)

@app.get("/inflation")
def get_inflation_data():
    df = pd.read_sql("SELECT * FROM geostat_inflation", engine)
    # NaN → None, რომ JSON-ით გადაიცეს
    df = df.where(pd.notna(df), other=None)
    return df.to_dict(orient="records")