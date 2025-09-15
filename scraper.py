import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#  CONFIGURATION
SITES = [
    "https://www.bbc.com",
    "https://edition.cnn.com",
    "https://www.theguardian.com/international"
]
OUTPUT_FOLDER = "data"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "headlines.txt")


#  CREATE DATA FOLDER
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


#  SCRAPE FUNCTION
def fetch_headlines():
    all_headlines = []

    for site in SITES:
        try:
            print(f"[INFO] Fetching from: {site}")
            response = requests.get(site, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Collect headlines from <h1>, <h2>, and <title>
            titles = set()
            for tag in soup.find_all(["h1", "h2", "title"]):
                text = tag.get_text(strip=True)
                if text and len(text) > 5:
                    titles.add(text)

            all_headlines.extend(titles)

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to fetch {site}: {e}")

    return all_headlines

#  SAVE TO FILE
def save_headlines(headlines):
    if not headlines:
        print("[WARNING] No headlines found.")
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"Headlines scraped on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n")
        for headline in headlines:
            f.write(f"- {headline}\n")

    print(f"[SUCCESS] Headlines saved to {OUTPUT_FILE}")

#  MAIN EXECUTION
if __name__ == "__main__":
    print("[START] Scraping started...")
    headlines = fetch_headlines()
    save_headlines(headlines)
    print("[DONE] Scraping complete.")
