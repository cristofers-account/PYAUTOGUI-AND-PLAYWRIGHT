import os
import json
import random
import asyncio
from datetime import datetime
import pandas as pd
from playwright.async_api import async_playwright

# Configuration Constants
SESSION_DIR = "whatsapp_session"
EXCEL_INPUT = "contacts.xlsx"

# Dynamically calculate today's date for filename outputs
TODAY_DATE = datetime.now().strftime("%Y-%m-%d")
REPORT_JSON = f"whatsapp_report_{TODAY_DATE}.json"
REPORT_EXCEL = f"whatsapp_report_{TODAY_DATE}.xlsx"

async def human_delay(min_sec=2, max_sec=5):
    """Introduces a random delay to simulate natural human pacing."""
    delay = random.uniform(min_sec, max_sec)
    await asyncio.sleep(delay)

async def check_login_status(page):
    """Waits for the main WhatsApp interface to confirm successful login."""
    print("\n==============================================================")
    print("[Waiting for WhatsApp Web to load]")
    print("👉 ACTION REQUIRED: Please scan the QR code on your monitor screen!")
    print("⏱️ You have 3 minutes to complete the scan.")
    print("==============================================================\n")
    
    try:
        # Increased timeout to 180,000ms (3 minutes) to allow comfortable phone scanning
        # Targets the main conversation search bar or side panel container
        await page.wait_for_selector('div[id="side"]', timeout=180000)
        print("✅ Login successful / Session restored!\n")
        return True
    except Exception:
        print("\n❌ Error: Login timeout reached.")
        print("💡 Tips: Ensure your internet is working, the page loads completely, and scan within 3 minutes.")
        return False

async def run_whatsapp_bot():
    # 1. Initialize input file if it does not exist
    if not os.path.exists(EXCEL_INPUT):
        sample_data = {
            "Name": ["John Doe", "Jane Smith"],
            "Phone": ["+919999999999", "+1234567890"],
            "Message": ["Hello {name}, this is a test message.", "Hi {name}, hope you are doing well!"]
        }
        pd.DataFrame(sample_data).to_excel(EXCEL_INPUT, index=False)
        print(f"📄 Created a sample input file: '{EXCEL_INPUT}'. Please populate it and rerun.")
        return

    # Load contacts to process
    df_contacts = pd.read_excel(EXCEL_INPUT)
    report_data = []

    async with async_playwright() as p:
        # 2. Launch with a persistent context to retain login state
        print("🚀 Launching Google Chrome instance...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=SESSION_DIR,
            headless=False,
            channel="chrome",
            args=["--start-maximized"],
            no_viewport=True
        )
        
        # Correctly unpack pages
        if context.pages:
            page = context.pages[0]
        else:
            page = await context.new_page()

        # Navigate to the official WhatsApp Web App portal
        await page.goto("https://web.whatsapp.com/")

        # 3. Authenticate
        if not await check_login_status(page):
            await context.close()
            return

        # 4. Iterate over each contact row
        for index, row in df_contacts.iterrows():
            name = str(row.get("Name", "")).strip()
            phone = str(row.get("Phone", "")).strip()
            msg_template = str(row.get("Message", "Hello {name}")).strip()
            
            # Personalize message payload
            personalized_msg = msg_template.format(name=name)
            
            print(f"👤 Processing ({index + 1}/{len(df_contacts)}): {name} ({phone})")
            status = "Failed"
            error_reason = "None"
            extracted_messages = []

            try:
                # Target the universal Search input box
                search_box_selector = 'div[contenteditable="true"][data-tab="3"]'
                await page.wait_for_selector(search_box_selector, timeout=15000)
                search_box = page.locator(search_box_selector)
                
                # Clear existing search queries
                await search_box.click()
                await page.keyboard.press("Control+A")
                await page.keyboard.press("Backspace")
                await search_box.fill(phone)
                await page.keyboard.press("Enter")
                await human_delay(4, 6)

                # Validate if contact exists or not found
                if await page.locator('span:has-text("No chats, contacts or messages found")').is_visible():
                    raise Exception("Contact or Phone number not found on WhatsApp.")

                # Locate the chat entry box
                chat_box_selector = 'footer div[contenteditable="true"][data-tab="10"]'
                await page.wait_for_selector(chat_box_selector, timeout=15000)
                chat_box = page.locator(chat_box_selector)
                
                # Type out message and execute send command
                await chat_box.click()
                await chat_box.fill(personalized_msg)
                await human_delay(1, 2)
                await page.keyboard.press("Enter")
                print(f"   ✉️ Message transmitted to {name}")
                await human_delay(3, 5)

                # Capture an operational proof screenshot
                screenshot_filename = f"screenshot_{name.lower().replace(' ', '_')}_{TODAY_DATE}.png"
                await page.screenshot(path=screenshot_filename)
                
                # 5. Smart Data Extraction: Scrape the last 3 visible messages
                msg_selector = 'div.message-in span.selectable-text, div.message-out span.selectable-text'
                all_msgs = page.locator(msg_selector)
                count = await all_msgs.count()
                
                # Pull text from the tail of the conversation stream
                start_idx = max(0, count - 3)
                for i in range(start_idx, count):
                    text = await all_msgs.nth(i).inner_text()
                    if text:
                        extracted_messages.append(text.strip())
                
                status = "Success"
                print(f"   📸 Screenshot captured. Extracted last {len(extracted_messages)} messages.")

            except Exception as e:
                error_reason = str(e)
                print(f"   ⚠️ Skipping {name}: {error_reason}")
                await page.keyboard.press("Escape")
            
            # Record dataset profile entry map
            report_data.append({
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Phone": phone,
                "MessageSent": personalized_msg,
                "Status": status,
                "ErrorReason": error_reason,
                "ExtractedLast3Messages": " | ".join(extracted_messages)
            })
            
            await human_delay(2, 5)

        # 6. Save Dated Operational Activity Logs
        df_report = pd.DataFrame(report_data)
        
        # Save Excel Summary File
        df_report.to_excel(REPORT_EXCEL, index=False)
        
        # Save Full Data Details JSON File
        with open(REPORT_JSON, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)
            
        print(f"\n🏁 Task Completed Successfully!")
        print(f"📁 JSON File Generated: {REPORT_JSON}")
        print(f"📁 Excel File Generated: {REPORT_EXCEL}")
        await context.close()

if __name__ == "__main__":
    asyncio.run(run_whatsapp_bot())
