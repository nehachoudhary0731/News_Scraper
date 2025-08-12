# News_Scraper
# Web Scraper

A simple Python script that scrapes data from a target website and saves the 
results into a text file.

# Features
- Fetches HTML content from a website
- Extracts required information using BeautifulSoup
- Saves the scraped results to data/headlines.txt
- Easy to run and modify

# Requirements
Install the dependencies before running the script:
pip install requests beautifulsoup4

# Usage
1. Clone or download the project folder.
2. Ensure you have a data folder in the same directory as scraper.py.
3. Run the script:
   python scraper.py
4. The scraped results will be stored in:
   data/headlines.txt

# Customization
- Change the target URL in scraper.py to scrape a different site.
- Update the HTML element selectors in the script to match the structure of your target page.
