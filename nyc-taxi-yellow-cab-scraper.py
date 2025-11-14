import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# ------------------------------
# Config
# ------------------------------
DOWNLOAD_DIR = "yellow_taxi_2025"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
URL = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

# ------------------------------
# Start Selenium
# ------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")  # headless is fine here
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# ------------------------------
# Scrape page source
# ------------------------------
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Find all Yellow Taxi 2025 links
urls = [
    a["href"]
    for a in soup.find_all("a", href=True)
    if "yellow_tripdata_2025" in a["href"]
]

print(f"Found {len(urls)} Yellow Taxi files:")
for u in urls:
    print(u)

# ------------------------------
# Download files
# ------------------------------
for url in urls:
    filename = url.split("/")[-1]
    path = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.exists(path):
        print(f"{filename} already exists, skipping...")
        continue

    print(f"Downloading {filename}...")
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

print("✅ All files downloaded to", DOWNLOAD_DIR)
