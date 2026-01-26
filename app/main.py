from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .config import settings
from .crawler import NewsCrawler
from .database import get_db  
from .crud import create_news_if_not_exists 

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return {"message": "Hello", "status": "System is running"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/crawl-and-save")
async def crawl_and_save(db: AsyncSession = Depends(get_db)):
    crawler = NewsCrawler()
    raw_news = await crawler.get_all_news()
    
    saved_count = 0
    for item in raw_news:
        # Пробуем сохранить каждую новость
        result = await create_news_if_not_exists(db, item)
        if result:
            saved_count += 1
            
    return {
        "found_total": len(raw_news),
        "saved_new": saved_count,
        "status": "Success"
    }