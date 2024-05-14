import pytest
from steps.support_steps import generate_valid_email

def test_success_create_account(customer_account_create_page):
    random_email = generate_valid_email()
    customer_account_create_page.open()
    customer_account_create_page.success_create_account(random_email)


@pytest.mark.parametrize('pssw, strn', (('Password123', 'Very Strong'),
                                        ('Password1', 'Strong'),
                                        ('Qwerty1!', 'Medium'),
                                        ('password', 'Weak')))
def test_password_strength_meter_label(customer_account_create_page, pssw, strn):
    customer_account_create_page.open()
    customer_account_create_page.check_password_strength_meter_label(pssw, strn)


def test_reply_email(customer_account_create_page):
    random_email = generate_valid_email()
    customer_account_create_page.open()
    customer_account_create_page.success_create_account(random_email)

    customer_account_create_page.clear_cookies()
    
    customer_account_create_page.open()
    customer_account_create_page.create_account(random_email)
    customer_account_create_page.check_text_on_the_page('There is already an account with this email address.\
                                                         If you are sure that it is your email address, ')


