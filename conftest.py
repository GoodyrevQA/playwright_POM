from playwright.sync_api import Page
from pages.customer_account_create_page import CustomerAccountCreatePage
from pages.sale_page import SalePage
from pages.collections_eco_friendly_page import CollectionsEcoFriendly
import pytest



@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    yield page


@pytest.fixture()
def customer_account_create_page(page):
    return CustomerAccountCreatePage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def collections_eco_friendly_page(page) -> CollectionsEcoFriendly:
    return CollectionsEcoFriendly(page)

