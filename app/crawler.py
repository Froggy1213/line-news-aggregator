import feedparser
from datetime import datetime
from email.utils import parsedate_to_datetime

class NewsCrawler:
    def __init__(self):
        # List of sources (TODO: move to DB or config later)
        self.sources = {
            "TechCrunch": "https://techcrunch.com/feed/",
            "YCombinator": "https://news.ycombinator.com/rss",
            "DeNA Engineering": "https://engineering.dena.com/index.xml" # DeNA Blog!
        }

    def fetch_feed(self, source_name: str, url: str):
        """Downloads and parses a single RSS feed."""
        print(f"⏳ Downloading {source_name}...")
        feed = feedparser.parse(url)
        
        news_list = []
        
        # Iterate through feed posts (taking the first 5 for testing)
        for entry in feed.entries[:5]:
            # Attempt to retrieve publication date
            published_at = datetime.now()
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                # Convert complex RSS date to python datetime
                # (using struct_time from feedparser)
                try:
                    published_at = datetime(*entry.published_parsed[:6])
                except:
                    pass

            news_item = {
                "title": entry.title,
                "url": entry.link,
                "source": source_name,
                "published_at": published_at,
                "raw_content": entry.get('summary', '') or entry.get('description', '')
            }
            news_list.append(news_item)
            
        print(f"✅ {source_name}: Found {len(news_list)} news items")
        return news_list

    async def get_all_news(self):
        """Iterates through all sources."""
        all_news = []
        for name, url in self.sources.items():
            # feedparser is a synchronous library. In the future, we can wrap this 
            # in run_in_executor, but we'll keep it simple for now.
            news = self.fetch_feed(name, url)
            all_news.extend(news)
        
        return all_news