import logging
from playwright.sync_api import sync_playwright, expect

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://demoqa.com/")
        page.wait_for_load_state("networkidle")

        expect(page.locator("div.home-banner")).to_be_visible()
        print("DemoQA homepage opened.")
        # browser manually close pause
        # input("Press Enter to close browser manually...")
        # browser.close()

        # 2nd page navigation example
        page.goto("https://demoqa.com/books")
        page.wait_for_load_state("networkidle")
        page.locator('#login').click()
        page.locator('#login').wait_for(state="visible")
        page.locator('#userName').fill("test72")
        page.locator('#password').fill("uQyR@rpw9ahb8Xq")
        page.locator('#login').click()
        print("Logged in as test72.")

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