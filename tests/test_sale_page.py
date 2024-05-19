from locators import loc_sale_page as loc


def test_go_home(sale_page):
    sale_page.open()
    sale_page.click_home()
    sale_page.check_url(f'{sale_page.BASE_URL}/')


def test_go_shop_women(sale_page):
    sale_page.open()
    sale_page.click_women()
    sale_page.check_url(f'{sale_page.BASE_URL}/promotions/women-sale.html')


def test_text_20_on_the_page(sale_page):
    sale_page.open()
    sale_page.check_text_on_the_page(loc.TEXT_20)
