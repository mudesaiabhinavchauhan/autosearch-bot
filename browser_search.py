from playwright.sync_api import sync_playwright
from urllib.parse import quote

def bing_search(query, max_results=5):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Load Bing search results directly
        search_url = f"https://www.bing.com/search?q={quote(query)}"
        page.goto(search_url)

        try:
            page.wait_for_selector("li.b_algo h2", timeout=10000)
        except:
            print("❌ Search results did not load in time.")
            browser.close()
            return []

        results = page.locator("li.b_algo h2")
        links = []

        for i in range(results.count()):
            try:
                title = results.nth(i).inner_text()
                url = results.nth(i).locator("a").get_attribute("href")
                if title and url:
                    links.append((title.strip(), url.strip()))
                if len(links) >= max_results:
                    break
            except:
                continue

        browser.close()
        return links
