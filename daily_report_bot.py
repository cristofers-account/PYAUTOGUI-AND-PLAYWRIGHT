import os
import time
from datetime import datetime
import pyautogui

def run_daily_report_bot():
    print("🚀 Starting Daily Report Bot...")
    print("⏳ Please keep your hands off the mouse and keyboard during execution.")
    time.sleep(3)
    
    # 1. Open Excel using the Windows Run dialog
    print("⌨️ Launching Microsoft Excel...")
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('excel', interval=0.05)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for Excel to fully load
    
    # 2. Select Blank Workbook (Press Enter on Excel splash screen)
    pyautogui.press('enter') 
    time.sleep(3)

    # 3. Generate dynamic Date and Time details automatically at run time
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    
    # 4. Write Data into active cells using keystroke simulation
    print("✍️ Writing automated row data...")
    
    # Column A: Date
    pyautogui.write(current_date, interval=0.05)
    pyautogui.press('tab')
    
    # Column B: Time
    pyautogui.write(current_time, interval=0.05)
    pyautogui.press('tab')
    
    # Column C: Report Status
    pyautogui.write("Automated Daily Report Successfully Created", interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)

    # 5. Save the Excel file dynamically incorporating the current date
    print("💾 Saving the Excel document...")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    
    filename = f"daily_report_{current_date}.xlsx"
    absolute_save_path = os.path.abspath(filename)
    
    # Input full file path to ensure it saves in your active folder workspace
    pyautogui.write(absolute_save_path, interval=0.05)
    pyautogui.press('enter')
    time.sleep(3)
    
    # 6. Capture a screenshot of the completed spreadsheet workspace
    print("📸 Taking a snapshot of the final worksheet view...")
    screenshot_filename = f"daily_report_{current_date}.png"
    
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_filename)
    
    print(f"✅ Excel Document Saved: {absolute_save_path}")
    print(f"✅ Sheet Snapshot Saved: {os.path.abspath(screenshot_filename)}")

if __name__ == "__main__":
    try:
        run_daily_report_bot()
    except Exception as error:
        print(f"❌ Automation routine halted: {error}")
