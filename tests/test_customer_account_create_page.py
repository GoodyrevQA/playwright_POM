import pytest
from steps.support_steps import generate_valid_email
from locators import loc_customer_account_create_page as loc

def test_success_create_account(customer_account_create_page):
    '''
    Test checks create new account and success message
    '''
    random_email = generate_valid_email()
    customer_account_create_page.open()
    customer_account_create_page.success_create_account(random_email)


@pytest.mark.parametrize('pssw, strn', (('Password123', 'Very Strong'),
                                        ('Password1', 'Strong'),
                                        ('Qwerty1!', 'Medium'),
                                        ('password', 'Weak')))
def test_password_strength_meter_label(customer_account_create_page, pssw, strn):
    '''
    Tests check strengths of passwords
    '''
    customer_account_create_page.open()
    customer_account_create_page.check_password_strength_meter_label(pssw, strn)


def test_reply_email(customer_account_create_page):
    '''
    Test checks create new account with replied email and warning message
    '''
    random_email = generate_valid_email()
    customer_account_create_page.open()
    customer_account_create_page.success_create_account(random_email)

    customer_account_create_page.clear_cookies()
    
    customer_account_create_page.open()
    customer_account_create_page.create_account(random_email)
    customer_account_create_page.check_text_on_the_page(loc.FAILED_REGISTERING)
