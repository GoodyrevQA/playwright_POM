from pages.base_page import BasePage
from playwright.sync_api import expect
from locators import loc_customer_account_create_page as loc
import allure


class CustomerAccountCreatePage(BasePage):
    REL_URL = '/customer/account/create'

    @allure.step('Check_password_strength_meter_label')
    def check_password_strength_meter_label(self, password, strength):
        self.fill_password(password)
        password_strength_meter_label = self.find(loc.PASSWORD_STRENGTH_METER_LABEL)
        expect(password_strength_meter_label).to_have_text(strength)

    @allure.step('Click create account button')
    def click_create_account_button(self):
        self.find(loc.BUTTON_CREATE_AN_ACCOUNT).click()

    @allure.step('Create new account')
    def create_account(self, email='1@1.com'):
        self.fill_first_name()
        self.fill_last_name()
        self.fill_email(email)
        self.fill_password()
        self.fill_confirm_password()
        self.click_create_account_button()

    @allure.step('Fill confirm password field')
    def fill_confirm_password(self, password='random_password_135$'):
        self.find(loc.CONFIRM_PASSWORD).type(password)

    @allure.step('Fill email field')
    def fill_email(self, email='1@1.com'):
        self.find(loc.EMAIL).type(email)

    @allure.step('Fill first name field')
    def fill_first_name(self, name='Ivan'):
        self.find(loc.FIRST_NAME).type(name)

    @allure.step('Fill last name field')
    def fill_last_name(self, surname='Ivanov'):
        self.find(loc.LAST_NAME).type(surname)

    @allure.step('Fill password field')
    def fill_password(self, password='random_password_135$'):
        self.find(loc.PASSWORD).type(password)

    @allure.step('Create new account and check success result')
    def success_create_account(self, email='1@1.com'):
        self.create_account(email)
        self.check_url(loc.CUSTOMER_ACCOUNT_URL)
        self.check_text_on_the_page(loc.SUCCESS_REGISTERING)
