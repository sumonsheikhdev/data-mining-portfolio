import yaml
from src.scrapers.artcle_scraper import ArticlesScraper
from src.storage.save_data import save_to_csv

with open("config/websites.yaml", "r") as f:
    sites = yaml.safe_load(f)

def main():
    ipl_config = sites["ipl"]
    scraper = ArticlesScraper(
       ipl_config["url"],
    )
    results =  scraper.run()
    save_to_csv(results, "IPL NEWS 2025")

if __name__ == "__main__":
    main()
