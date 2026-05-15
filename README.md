# Crypto ETL Pipeline

ეს არის მონაცემთა დამუშავების პროექტი, რომელიც იღებს კრიპტოვალუტის მონაცემებს (BTC) API-დან, ამუშავებს Pandas-ით და ინახავს PostgreSQL ბაზაში.

## გამოყენებული ტექნოლოგიები

- Python
- Pandas
- PostgreSQL (Docker)
- SQLAlchemy
- yfinance

## კონფიგურაცია

1. დააკოპირეთ `.env.example` → `.env` და შეავსეთ თქვენი მნიშვნელობები:

```bash
cp .env.example .env
```

2. `.env` ფაილი **არ იტვირთება Git-ში** (`.gitignore`-ში შეტანილია).

## როგორ გავუშვათ

1. დააინსტალირეთ [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. გაუშვით მონაცემთა ბაზა:

```bash
docker-compose up -d
```

3. დააინსტალირეთ ბიბლიოთეკები:

```bash
pip install -r requirements.txt
```

4. გაუშვით სკრიპტი:

```bash
python load_data.py
```
