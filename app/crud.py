from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import NewsItem

async def create_news_if_not_exists(db: AsyncSession, news_data: dict):
    result = await db.execute(
        select(NewsItem).where(NewsItem.url == news_data['url'])
    )
    existing_news = result.scalar_one_or_none()

    if existing_news:
        return None 
    
    new_item = NewsItem(
        title=news_data["title"],
        url=news_data["url"],
        source=news_data["source"],
        published_at=news_data["published_at"],
        raw_content=news_data["raw_content"]
    )

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item