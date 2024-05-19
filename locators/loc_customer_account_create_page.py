from pages.base_page import BasePage


FIRST_NAME = '#firstname'
LAST_NAME = '#lastname'
EMAIL = '#email_address'
PASSWORD = '#password'
CONFIRM_PASSWORD = '#password-confirmation'
BUTTON_CREATE_AN_ACCOUNT = '.action.submit.primary'
PASSWORD_STRENGTH_METER_LABEL = '#password-strength-meter-label'
ACCOUNT_SWITCHER = '.customer-name.active'

CUSTOMER_ACCOUNT_URL = f'{BasePage.BASE_URL}/customer/account/'

SUCCESS_REGISTERING = 'Thank you for registering with Main Website Store. '
FAILED_REGISTERING = 'There is already an account with this email address.\
                        If you are sure that it is your email address, '