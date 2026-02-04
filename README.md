# LINE News Aggregator 🤖

A robust, asynchronous news aggregation bot built for the LINE messaging platform. This project crawls technical news sources (RSS) and delivers updates via a LINE Bot interface.

Designed with a modern "Environment First" approach using Docker and Python 3.11+.

## 🛠 Tech Stack

* **Core:** Python 3.11, FastAPI
* **Database:** PostgreSQL (AsyncPG), SQLAlchemy 2.0 (Modern styling)
* **Migrations:** Alembic
* **Infrastructure:** Docker & Docker Compose
* **Parsing:** Feedparser
* **External API:** LINE Messaging API SDK v3

## 🚀 Features

* **Asynchronous Architecture:** Fully async database connections and request handling.
* **Automated Crawler:** Fetches news from sources like TechCrunch, YCombinator, and DeNA Engineering Blog.
* **Duplicate Prevention:** Checks existing URLs in the database to avoid spam.
* **LINE Integration:** Webhook handling with signature verification and auto-reply capabilities.
* **Containerized:** Ready to deploy anywhere via Docker.

## ⚙️ Installation & Setup

### Prerequisites
* Docker & Docker Compose (or OrbStack on macOS)

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/line-news-aggregator.git](https://github.com/YOUR_USERNAME/line-news-aggregator.git)
cd line-news-aggregator
```
### 2. Configure Environment
Create a .env file in the root directory:

Ini, TOML
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/news_db
PROJECT_NAME=LineNewsAggregator

# LINE API Keys
LINE_CHANNEL_SECRET=your_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=your_access_token
### 3. Run with Docker
Bash
docker-compose up --build
### 4. Apply Database Migrations
Initialize the database schema:

```bash
docker-compose exec web alembic upgrade head
🕷 Usage
Check Health: Go to http://localhost:8000/health

Trigger Manual Crawl: Go to http://localhost:8000/crawl-and-save to fetch latest news and save them to PostgreSQL.

LINE Bot: The bot listens for webhooks at /callback. (Requires ngrok or public IP for local testing).
```

# 📂 Project Structure
Plaintext
```bash
.
├── app
│   ├── main.py          # Entry point
│   ├── models.py        # SQLAlchemy 2.0 Models
│   ├── crud.py          # Database operations
│   ├── crawler.py       # RSS Parsing logic
│   ├── line_bot.py      # LINE Webhook handler
│   └── ...
├── alembic              # Migration scripts
├── docker-compose.yml
└── requirements.txt
```