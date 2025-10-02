from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page:Page):
    #iphone X, Nokia Edge -> verify 2 items are showing in cart.
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_child_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page_info:
        page.get_by_role("link", name = "Free Access to InterviewQues/ResumeAssistance/Material").click()  # new page
        child_page = new_page_info.value
        text = child_page.locator(".red").text_content()
        print(text) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at") #0 -> Please email us ,  1->mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].strip().split(" ")[0]    #0->mentor@rahulshettyacademy.com 1->
        assert email == "mentor@rahulshettyacademy.com"















