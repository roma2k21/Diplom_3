from pages.base_page import BasePage
from locators.order_feed import OrderFeedLocators
from locators.universal_locators import UniversalLocators


class OrderFeed(BasePage):
    def click_order(self):
        self.find_elements_with_wait(OrderFeedLocators.LIST_NAME_BURGER)[1].click()

    def check_visibility_modal_window(self):
        return self.find_element_with_wait(OrderFeedLocators.TITILE_MODAL_WINDOW)

    def close_modal_window_in_order(self):
        self.click_element_with_wait(UniversalLocators.CLOSE_MODAL_WINDOW)

    def counter_order_all_time(self):
        return self.get_text_from_element(OrderFeedLocators.COUNT_ALL_TIME)

    def counter_order_today(self):
        return self.get_text_from_element(OrderFeedLocators.COUNT_CREATE_ORDER_TODAY)

    def counter_order_today_in_feed_page(self):
        return self.get_text_from_element(OrderFeedLocators.COUNT_IN_WORK)

    def check_if_order_number_is_shown_in_progress(self):
        self.get_text_from_element(OrderFeedLocators.COUNT_IN_WORK)

    def get_number_of_order_in_order_feed(self):
        self.wait_for_element_to_change_text(OrderFeedLocators.COUNT_IN_WORK, 'Все текущие заказы готовы!')
        return self.get_text_from_element(OrderFeedLocators.COUNT_IN_WORK)

    def get_number_order_in_feed_page(self):
        return self.get_number_order(UniversalLocators.HISTORY_ORDER_LIST)
