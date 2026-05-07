from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_contain_text(text)