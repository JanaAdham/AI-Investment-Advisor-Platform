import requests
from bs4 import BeautifulSoup


url = "https://www.egx.com.eg/ar/NewsSearch.aspx"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
# }

# try:
#     response = requests.get(
#         url,
#         headers=headers,
#         timeout=20
#     )

#     # print(response.status_code)
#     # print(response.url)
#     # print(response.text[:500])

# except requests.exceptions.RequestException as e:
#     print("Request failed:")
#     print(e)

# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.title)
# print(soup.get_text(" ", strip=True)[:1000])

from playwright.sync_api import sync_playwright

url = "https://www.egx.com.eg/ar/NewsSearch.aspx"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url, wait_until="networkidle")

    print(page.title())
    print(page.locator("body").inner_text())

    browser.close()