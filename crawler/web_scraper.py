# web_scraper.py
from playwright.sync_api import sync_playwright

def scraper(query:str,max_results=5):
    with sync_playwright() as pw:
        browser=pw.chromium.launch()
        page=browser.new_page()
        page.goto(f"https://www.google.com/search?q={query.replace(' ', '+')}")

        page.wait_for_selector("div#search")
        results = []
        for result in page.query_selector_all("div.tF2Cxc")[:max_results]:
            title_el = result.query_selector("h3")
            link_el = result.query_selector("a")
            snippet_el = result.query_selector(".VwiC3b")

            title = title_el.inner_text() if title_el else "No Title"
            link = link_el.get_attribute("href") if link_el else "No Link"
            snippet = snippet_el.inner_text() if snippet_el else "No Snippet"

            results.append({
                "title": title,
                "link": link,
                "snippet": snippet
            })

        browser.close()
        return results

if __name__=="__main__":
    query="how to perform a proper backflip?"
    results=scraper(query,3)
    print(results)
