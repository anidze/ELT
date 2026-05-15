import os
import math
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

CITIES = {
    1: "საქართველო",
    2: "თბილისი",
    3: "ქუთაისი",
    4: "ბათუმი",
    5: "გორი",
    6: "თელავი",
}

@app.get("/inflation")
def list_cities():
    """Returns the list of available city numbers and names."""
    return [{"id": k, "city": v} for k, v in CITIES.items()]

@app.get("/inflation/{city_id}")
def get_inflation_data(city_id: int):
    if city_id not in CITIES:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"City {city_id} not found. Valid: 1-{len(CITIES)}")
    df = pd.read_sql(f"SELECT * FROM test_inflation_{city_id}", engine)
    records = df.to_dict(orient="records")
    cleaned = [
        {k: (None if isinstance(v, float) and math.isnan(v) else v) for k, v in row.items()}
        for row in records
    ]
    return {"city_id": city_id, "city": CITIES[city_id], "data": cleaned}