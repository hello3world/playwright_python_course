from playwright.sync_api import Page, expect

def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    # Example assertion
    expect(page).to_have_title("Rahul Shetty Academy")
    context.close()
    browser.close()

def test_playwright_shortcut(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    expect(page).to_have_url("https://rahulshettyacademy.com/loginpagePractise")

def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    # Corrected typo here
    page.get_by_role("button", name="Sign In").click()
    # Example assertion: verify error message appears
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    #Incorrect message
