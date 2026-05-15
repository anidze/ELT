# Crypto ETL Pipeline

A data processing project that fetches cryptocurrency data (BTC) from an API, processes it with Pandas, and stores it in a PostgreSQL database.

## Tech Stack

- Python
- Pandas
- PostgreSQL (Docker)
- SQLAlchemy
- yfinance

## Configuration

1. Copy `.env.example` → `.env` and fill in your values:

```bash
cp .env.example .env
```

2. The `.env` file is **excluded from Git** (listed in `.gitignore`) — credentials are never committed.

## How to Run

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Start the database:

```bash
docker-compose up -d
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python load_data.py
```
