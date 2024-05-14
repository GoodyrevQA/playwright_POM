from pages.base_page import BasePage
from playwright.sync_api import expect


FIRST_NAME = '#firstname'
LAST_NAME = '#lastname'
EMAIL = '#email_address'
PASSWORD = '#password'
CONFIRM_PASSWORD = '#password-confirmation'
BUTTON_CREATE_AN_ACCOUNT = '.action.submit.primary'
PASSWORD_STRENGTH_METER_LABEL = '#password-strength-meter-label'
ACCOUNT_SWITCHER = '.customer-name.active'

CUSTOMER_ACCOUNT_URL = f'{BasePage.BASE_URL}/customer/account/'


class CustomerAccountCreatePage(BasePage):
    REL_URL = '/customer/account/create'


    def create_account(self, email):
        self.find(FIRST_NAME).fill('Ivan')
        self.find(LAST_NAME).fill('Ivanov')

        self.find(EMAIL).fill(email)

        self.find(PASSWORD).fill('random_password_135$')
        self.find(CONFIRM_PASSWORD).fill('random_password_135$')
        self.find(BUTTON_CREATE_AN_ACCOUNT).click()


    def success_create_account(self, email):
        self.create_account(email)
        self.check_url(CUSTOMER_ACCOUNT_URL)
        self.check_text_on_the_page('Thank you for registering with Main Website Store.')


    def check_password_strength_meter_label(self, password, strength):
        self.find(PASSWORD).type(password)
        password_strength_meter_label = self.find(PASSWORD_STRENGTH_METER_LABEL)
        expect(password_strength_meter_label).to_have_text(strength)
        



