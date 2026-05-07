import pytest
from playwright.sync_api import Page
from tests.e2e.pages.login_page import LoginPage
from pathlib import Path


def pytest_collection_modifyitems(config, items):
    for item in items:
        test_path = Path(str(item.fspath))

        if "e2e" in test_path.parts: # e2e är namnet på mappen
            item.add_marker(pytest.mark.e2e)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.goto()
    return login

@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    return page