import string
from random import choice
import allure


@allure.step('Generate valid email')
def generate_valid_email():
        characters = string.ascii_lowercase + string.digits
        x = ''.join(choice(characters) for _ in range(10))
        return f'{x}@gmail.com'
