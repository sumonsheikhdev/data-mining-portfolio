
from src.core.base_scraper import BaseScraper
from src.utils.parser import parse_article
from src.utils.fetcher import save_raw

class ArticlesScraper(BaseScraper):
    def run(self):
        articles = []
        html = self.fetchUrl()
        save_raw(html, "ipl_articles")
        data = parse_article(html)
        articles.extend(data)
        return articles




    


