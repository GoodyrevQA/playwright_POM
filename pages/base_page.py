from playwright.sync_api import Page, expect



class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com'
    REL_URL = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.REL_URL:
            self.page.goto(f'{self.BASE_URL}{self.REL_URL}')
        else:
            raise NotImplementedError

    def find(self, locator):
        return self.page.locator(locator)
    
    def check_url(self, some_url):
        expect(self.page).to_have_url(some_url)

    def check_text_on_the_page(self, some_text):
        element_with_text = self.page.get_by_text(some_text)
        expect(element_with_text).to_be_visible()

    def clear_cookies(self):
        self.page.context.clear_cookies()

    def press_enter(self):
        self.page.press('Enter')