import requests
url='https://example.com/data'
response = requests.get(url)
data = response.content
print(data)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://example.com')
    content = page.content()
    print(content)
    browser.close()