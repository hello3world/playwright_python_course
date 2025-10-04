from playwright.sync_api import Page, expect


def test_ui_checks(page: Page):

    #hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()


    #MouseHover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()


    #FrameHandling
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link",name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

    # Check the price of rice is equal to 37.
    # identify the price column
    # identify rice row
    # extract the price of the rice.
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    price_col_index = None

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            price_col_value = index
            print(f"Price column value is {price_col_value} ")
            break

    if price_col_index is None:
        print("Error: Price column not found")
    else:
        # Find the rice row and verify the price
        rice_row = page.locator("tr").filter(has_text="Rice")

        if rice_row.count() > 0:
            try:
                expect(rice_row.locator("td").nth(price_col_index)).to_have_text("37")
                print("Price verification successful")
            except AssertionError:
                print(f"Assertion Error: Rice price is not 37 in column {price_col_index}")
            except Exception as e:
                print(f"Unexpected error occurred: {e}")
        else:
            print("Error: Rice row not found")































