import os
from playwright.sync_api import sync_playwright

def capture_cricbuzz_match():
    output_dir = r"C:\Users\dell\Gen AI program"
    file_name = "latest_match_screenshot.png"
    full_path = os.path.join(output_dir, file_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = context.new_page()

        print("Navigating to Cricbuzz Live Scores...")
        # Fixed line: Ensure the URL and parameters stay on one single line
        page.goto("https://cricbuzz.com", wait_until="domcontentloaded")
        
        page.wait_for_timeout(3000)

        # Target the top live matches slider container on Cricbuzz
        match_card = page.locator("#match_menu_container").first
        
        print(f"Saving screenshot to: {full_path}")
        if match_card.is_visible():
            match_card.screenshot(path=full_path)
        else:
            page.screenshot(path=full_path, full_page=True)

        print("Screenshot successfully captured and saved!")
        browser.close()

if __name__ == "__main__":
    capture_cricbuzz_match()
