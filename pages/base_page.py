from playwright.sync_api import Page, expect
import allure
import re


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com'
    REL_URL = None

    def __init__(self, page: Page):
        self.page = page
    
    @allure.step('Check part of URL')
    def check_part_of_url(self, part_of_url):
        expect(self.page).to_have_url(re.compile(part_of_url))

    @allure.step('Check text on the page')
    def check_text_on_the_page(self, some_text):
        element_with_text = self.page.get_by_text(some_text)
        expect(element_with_text).to_be_visible()

    @allure.step('Check URL')
    def check_url(self, some_url):
        expect(self.page).to_have_url(some_url)

    @allure.step('Clear cookies')
    def clear_cookies(self):
        self.page.context.clear_cookies()

    @allure.step('Find element by locator')
    def find(self, locator):
        return self.page.locator(locator)
    
    @allure.step('Find all elements')
    def find_all_elements(self, locator):
        return self.page.query_selector_all(locator)
    
    @allure.step('Find element by role')
    def find_by_role(self, by_role_locator):
        return self.page.get_by_role(by_role_locator[0], name=by_role_locator[1])

    @allure.step('Open the page')
    def open(self):
        if self.REL_URL:
            self.page.goto(f'{self.BASE_URL}{self.REL_URL}')
        else:
            raise NotImplementedError

    @allure.step('Press Enter')
    def press_enter(self):
        self.page.press('Enter')
