# pyrefly: ignore [missing-import]
from playwright.sync_api import sync_playwright
from datetime import datetime
import pyautogui
import time


print("Playwright example")
# Chromium -> cricbuzz -> Scorecard of current match -> notepad
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com", timeout=60000)
    print(page.title())

    # Extract current match status
    match_status = page.inner_text("IND")
    print(match_status)
    
    page.screenshot(path="google.png")
    browser.close() 
    #paste this in notepad
    pyautogui.hotkey('win', 'r')  # Open the Run dialog
    time.sleep(1)  # Wait for the Run dialog to open
    pyautogui.typewrite('notepad\n')  # Type 'notepad' and press Enter
    time.sleep(2)  # Wait for Notepad to open 



