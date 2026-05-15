import io
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# 1. მონაცემების ჩამოტვირთვა
url = os.getenv("TEST_URL")
print("მონაცემების ჩამოტვირთვა...")
response = requests.get(url, timeout=20)
response.raise_for_status()

# .xlsx ფაილია — read_excel გამოიყენება, არა read_csv
df = pd.read_excel(io.BytesIO(response.content), header=2)

# პირველი სვეტის სახელი → 'year'
df.rename(columns={df.columns[0]: "year"}, inplace=True)

# ცარიელი სტრიქონების გაწმენდა
df.dropna(how="all", inplace=True)

print(df.head())

# 2. მონაცემთა ბაზასთან კავშირი (.env-დან)
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT', '5433')}"
    f"/{os.getenv('POSTGRES_DB')}"
)
engine = create_engine(DATABASE_URL)

# 3. ბაზაში ჩატვირთვა
print("Loading Geostat data to PostgreSQL...")
df.to_sql("geostat_inflation", engine, if_exists="replace", index=False)
print("მონაცემები წარმატებით ჩაიწერა ბაზაში!")
