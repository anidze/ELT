import os
import webbrowser
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@localhost:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

df = pd.read_sql("SELECT * FROM test_inflation ORDER BY year", engine)

output = "test_view.html"
df.to_html(output, index=False)
webbrowser.open(output)
print(f"ბრაუზერში გაიხსნა: {output}")
