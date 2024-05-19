import pytest


def test_change_view_to_list(collections_eco_friendly_page):
    '''
    Test checks change view to list
    '''
    collections_eco_friendly_page.open()
    collections_eco_friendly_page.change_view_to_list()


def test_check_sort_by_price(collections_eco_friendly_page):
    '''
    Test checks sorting items by ascending price 
    '''
    collections_eco_friendly_page.open()
    collections_eco_friendly_page.check_sort_by_price()


@pytest.mark.parametrize('dgt', ('12', '24', '36'))
def test_check_amount_of_page_items(collections_eco_friendly_page, dgt):
    '''
    Tests check amount items on the page
    '''
    collections_eco_friendly_page.open()
    collections_eco_friendly_page.check_amount_of_page_items(dgt)
