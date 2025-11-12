import pytest
from playwright.sync_api import sync_playwright, expect

def test_HomePage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://demoqa.com/")
        page.wait_for_load_state("networkidle")
        expect(page.locator("div.home-banner")).to_be_visible()
        print("DemoQA homepage opened.")
        # browser manually close pause
        input("Press Enter to close browser manually...")
        browser.close()

        # Login test
def test_Login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://demoqa.com/books")
        page.wait_for_load_state("networkidle")
        page.locator('#login').click()
        page.locator('#login').wait_for(state="visible")
        page.locator('#userName').fill("test72")
        page.locator('#password').fill("uQyR@rpw9ahb8Xq")
        page.locator('#login').click()
        print("Logged in as test72.")
        browser.close()

def test_BookPage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://demoqa.com/books")
        page.wait_for_load_state("networkidle")

        expect(page.locator("div.books-wrapper")).to_be_visible()
        books = page.locator(".rt-tbody .rt-tr-group")
        count = books.count()
        assert count > 0, "No books found!"
        print(f"📚 Total books found: {count}")

        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)
        targetBook = page.locator("text=Understanding ECMAScript 6")
        targetBook.scroll_into_view_if_needed() 
        print("Scrolled to 'Understanding ECMAScript 6' book.") 
        expect(targetBook).to_be_visible()
        expect(targetBook).to_have_text("Understanding ECMAScript 6")
        expect(targetBook).to_have_count(1)
      
        #  Print all book titles
        for i in range(books.count()):
            title = books.nth(i).locator(".rt-td:nth-child(2)").inner_text()
            print(f"{i+1}. {title}")
        # 6️⃣ Click on the target book 
        page.locator('div.books-wrapper').screenshot(path='books_page.png')
        page.locator('div.books-wrapper').wait_for(state="visible")
        targetBook.click()
        browser.close()







#  browser one time open for all tests================================

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_homepage(page):
    page.goto("https://demoqa.com/")
    expect(page.locator("div.home-banner")).to_be_visible()
    print("✅ Homepage opened")

def test_books_page(page):
    page.goto("https://demoqa.com/books")
    expect(page.locator("div.books-wrapper")).to_be_visible()
    print("✅ Books page opened")

def test_login(page):
    page.goto("https://demoqa.com/books")
    page.locator('#login').click()
    page.locator('#userName').fill("test72")
    page.locator('#password').fill("uQyR@rpw9ahb8Xq")
    page.locator('#login').click()
    print("✅ Logged in as test72")
