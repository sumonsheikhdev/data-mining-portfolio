import os

def save_raw(html, site_name):
    raw_dir = f"data/raw/{site_name}"
    os.makedirs(raw_dir, exist_ok= True)
    path = f"{raw_dir}/site.html"

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
