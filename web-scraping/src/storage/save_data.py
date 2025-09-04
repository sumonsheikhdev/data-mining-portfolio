import pandas as pd
import os
from datetime import datetime

def save_to_csv(data, site_name):
    os.makedirs("data/processed", exist_ok=True)
    path = f"data/processed/{site_name}.csv"
    df = pd.DataFrame(data)
    df["scraped_at"] = datetime.now()
    df.to_csv(path, index=False)
    print(f"[✓] Data saved → {path}")
