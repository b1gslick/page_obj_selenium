from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocator.ADD_BASKET_BUTTON)

    def should_be_notice_for_add(self):
        assert self.is_element_present(*ProductPageLocator.TITLE_BOOK_ADDED), "can't find element"

    def name_added_book(self):
        assert self.is_element_present(*ProductPageLocator.TITLE_BOOK)
        return self.browser.find_element(*ProductPageLocator.TITLE_BOOK).text

    def should_name_compared_with_notice(self):
        name = self.name_added_book()
        name_notice = self.browser.find_element(*ProductPageLocator.TITLE_BOOK_ADDED).text
        assert name == name_notice, f"name from title {name}, not compared with added book {name_notice}"

    def price_in_desk(self):
        assert self.is_element_present(*ProductPageLocator.PRICE_IN_DESC)
        return self.browser.find_element(*ProductPageLocator.PRICE_IN_DESC).text

    def price_in_basket(self):
        assert self.is_element_present(*ProductPageLocator.PRICE_IN_BASKET)
        return self.browser.find_element(*ProductPageLocator.PRICE_IN_BASKET).text

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocator.ADD_BASKET_BUTTON)
        button.click()

    def should_be_total_price(self):
        assert self.is_element_present(*ProductPageLocator.TOTAL_PRICE)

    def should_total_price_compare_price(self):
        total_price = self.browser.find_element(*ProductPageLocator.TOTAL_PRICE).text
        item_price = self.price_in_basket()
        assert item_price == total_price, f"price for item {item_price} doesn't equal price in total {total_price}"

    def should_price_equal_notice(self):
        price = self.browser.find_element(*ProductPageLocator .PRICE_IN_DESC).text
        price_notice = self.browser.find_element(*ProductPageLocator.NOTICE_PRICE).text
        assert price == price_notice, f"price book {price} doesn't equal price from basket {price_notice}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
