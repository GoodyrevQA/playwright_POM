from pages.base_page import BasePage
from locators import loc_sale_page as loc
import allure


class SalePage(BasePage):
    REL_URL = '/sale.html'

    @allure.step('Click link Home')
    def click_home(self):
        self.find_by_role(loc.BR_HOME).click()

    @allure.step("Click link Shop Women's Deals")
    def click_women(self):
        self.find_by_role(loc.BR_SHOP_WOMEN).click()
