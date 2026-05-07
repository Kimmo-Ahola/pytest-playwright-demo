"""Vi skriva ett demo-test som egentligen inte testar något
utan bara visar exempel på locators"""
from playwright.sync_api import Page, expect

def test_demo_locators(page: Page):
    # Navigera till en sida som ska testas
    page.goto("https://www.saucedemo.com")
    
    page.get_by_placeholder("Username").highlight() # highlight är endast för debugging
    # för debuggings skull lägger vi till en manuell wait

    page.get_by_placeholder("Username").fill("Faulty Username")
    page.get_by_placeholder("Password").fill("Faulty Password")

    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Username and password do not match"))