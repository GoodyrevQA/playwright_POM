from pages.base_page import BasePage
from locators import loc_collections_eco_friendly_page as loc
import allure


class CollectionsEcoFriendly(BasePage):
    REL_URL = '/collections/eco-friendly.html'

    @allure.step('Change sort to price')
    def change_sort_to_price(self):
        sorter = self.find(loc.SORTER).nth(0)
        sorter.select_option('Price')

    @allure.step('Change view to list')
    def change_view_to_list(self):
        self.click_mode_list()
        self.check_part_of_url('product_list_mode=list')

    @allure.step('Check amount of items on the page')
    def check_amount_of_page_items(self, digit):
        all_items = self.get_items_amount()
        self.set_limit(digit)
        items = self.find(loc.PRICES).count()
        assert items == min(all_items, int(digit))

    @allure.step('Check sort by price')
    def check_sort_by_price(self):
        self.change_sort_to_price()
        prices = self.find_all_elements(loc.PRICES)
        prices_lst = [float(prices[i].text_content()[1:]) for i in range(len(prices))]
        sorted_prices_lst = sorted(prices_lst)
        assert prices_lst == sorted_prices_lst, f'''товары не отсортированы по цене. цены на странице:
                                                    {prices_lst}, правильная сортировка: {sorted_prices_lst}'''

    @allure.step('Ckick button to change view on the list')
    def click_mode_list(self):
        mode_list = self.find(loc.MODE_LIST).nth(0)
        mode_list.click()

    @allure.step('Set limit of items on the page')
    def set_limit(self, digit):
        limiter = self.find(loc.LIMITER).nth(-1)
        limiter.select_option(digit)

    @allure.step('Get amount of items on the page')
    def get_items_amount(self):
        amount = self.find(loc.AMOUNT).nth(0)
        int_amount = max(int(i) for i in amount.text_content().split() if i.isdigit())
        return int_amount
    