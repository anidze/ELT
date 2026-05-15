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

excel_file = pd.ExcelFile(io.BytesIO(response.content))
print(f"Sheet-ები: {excel_file.sheet_names}")

# 2. მონაცემთა ბაზასთან კავშირი (.env-დან)
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST', 'localhost')}:{os.getenv('POSTGRES_PORT', '5433')}"
    f"/{os.getenv('POSTGRES_DB')}"
)
engine = create_engine(DATABASE_URL)

# 3. ყველა sheet-ი ბაზაში ჩატვირთვა
for i, sheet in enumerate(excel_file.sheet_names, start=1):
    df = pd.read_excel(excel_file, sheet_name=sheet, header=2)
    df.rename(columns={df.columns[0]: "year"}, inplace=True)
    df.dropna(how="all", inplace=True)
    df["city"] = sheet  # ქალაქის სახელი სვეტად

    table_name = f"test_inflation_{i}"
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"{i}. '{sheet}' → '{table_name}' ({len(df)} სტრიქონი)")

print("ყველა მონაცემი წარმატებით ჩაიწერა ბაზაში!")
