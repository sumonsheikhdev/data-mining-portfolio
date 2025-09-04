from bs4 import BeautifulSoup

def parse_article(html):
    soup = BeautifulSoup(html, "html.parser")
    all_article = []
    selected_article = soup.find_all("div", class_ = "latest-slider-main")

    for latest in selected_article:
        article = Article(
            title= latest.find("a").get("data-title"),
            sub_title= latest.find("li", class_ = "textTwoLine justify-content-start text-start").get_text(),
            thumnail_link= latest.find("img").get("src"),
            article_link= latest.find("a").get("href"),
            news_category= latest.find("a").get("data-type"),
            published_date= latest.find("span", class_ ="d-flex").get_text().strip()
        )
        all_article.append(article.toDic())

    return all_article


class Article ():
    def __init__(self, title, sub_title, thumnail_link, article_link, news_category, published_date):
        self.title = title
        self.sub_title = sub_title
        self.thumnail_link = thumnail_link
        self.article_link = article_link
        self.news_category = news_category
        self.published_date = published_date
    
    def toDic(self):
        return {
            "title":  self.title,
            "sub_title": self.sub_title,
            "thumnail_link": self.thumnail_link,
            "article_link": self.article_link,
            "news_category" :self.news_category,
           "published_date" :self.published_date 
           }

