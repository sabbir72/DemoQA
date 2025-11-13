import pytest
from playwright.sync_api import sync_playwright, expect

def test_HomePage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://demoqa.com/", timeout=60000)
        page.wait_for_load_state("networkidle")
        expect(page.locator("div.home-banner")).to_be_visible()
        print("DemoQA homepage opened.")
        
    #getbyText example
        page.get_by_text('Elements').click()
        text = page.locator("text=Please select an item from left to start practice.")
        assert text.is_visible(), "Text not found!"
        print("Text verified using get_by_text.")