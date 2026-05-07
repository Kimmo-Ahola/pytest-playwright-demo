from playwright.sync_api import Page, expect

from tests.e2e.pages.login_page import LoginPage

# Första med upprepad kod
# def test_user_can_login(page: Page):
#     page.goto("https://www.saucedemo.com")
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click()

#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#     expect(page.get_by_text("Products")).to_be_visible()

# # Page object model introducerades
# def test_user_can_login_2(page: Page):
#     login = LoginPage(page)
#     login.goto()
#     login.login("standard_user", "secret_sauce")
#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#     expect(page.get_by_text("Products")).to_be_visible()

# def test_locked_out_user_sees_error(page: Page):
#     login = LoginPage(page)
#     login.goto()
#     login.login("locked_out_user", "secret_sauce")
#     login.expect_error("locked out")

# fixture för loginpage
def test_user_can_login_3(login_page: LoginPage):
    login_page.login("standard_user", "secret_sauce")
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(login_page.page.get_by_text("Products")).to_be_visible()



# def test_user_can_add_to_cart(page: Page):
#     page.goto("https://www.saucedemo.com")
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click()

#     item = page.locator(".inventory_item", has_text="Sauce Labs Backpack")
#     item.get_by_role("button", name="Add to cart").click()
#     expect(page.locator(".shopping_cart_badge")).to_have_text("1")

# def test_user_can_add_to_cart_2(page: Page):
#     login = LoginPage(page)
#     login.goto()
#     login.login("standard_user", "secret_sauce")

#     item = page.locator(".inventory_item", has_text="Sauce Labs Backpack")
#     item.get_by_role("button", name="Add to cart").click()
#     expect(page.locator(".shopping_cart_badge")).to_have_text("1")