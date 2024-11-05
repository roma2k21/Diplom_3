import data
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.universal_locators import UniversalLocators


class MainPage(BasePage):
    def click_on_ingredient(self):
        self.click_element_with_wait(MainPageLocators.INRGEDIENT)

    def check_open_modal_window(self):
        return self.find_element_with_wait(MainPageLocators.DETAIL_INGREDIENT)

    def close_modal_window(self):
        if data.driver_name == 'chrome':
            self.click_element_with_wait(UniversalLocators.CLOSE_MODAL_WINDOW)
        else:
            self.click_on_element(UniversalLocators.CLOSE_MODAL_WINDOW)

    def check_close_modal_window(self):
        return self.find_element_with_wait(MainPageLocators.DETAIL_INGREDIENT)

    def add_ingredient_in_order(self):
        if data.driver_name == 'chrome':
            self.drag_and_drop_element(MainPageLocators.INRGEDIENT, MainPageLocators.INGEDIENT_BASKET)
        else:
            self.drag_and_drop_script(MainPageLocators.INRGEDIENT, MainPageLocators.INGEDIENT_BASKET)

    def check_add_ingredient_in_order(self):
        if data.driver_name == 'chrome':
            self.drag_and_drop_element(MainPageLocators.INRGEDIENT, MainPageLocators.INGEDIENT_BASKET)
        else:
            self.drag_and_drop_script(MainPageLocators.INRGEDIENT, MainPageLocators.INGEDIENT_BASKET)
        return self.get_text_from_element(MainPageLocators.COUNTER_BASKET)

    def click_create_order(self):
        if data.driver_name == 'chrome':
            self.click_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
        else:
            self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    def check_create_order(self):
        return self.get_text_from_element(MainPageLocators.TITLE_IDENTIFAIR_ORDER)

    def get_order_number_in_modal_window(self):
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER_IN_MODAL_WINDOW)

    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_to_change_text(MainPageLocators.NUMBER_OF_ORDER_IN_MODAL_WINDOW, '9999')
        return self.get_text_from_element(MainPageLocators.NUMBER_OF_ORDER_IN_MODAL_WINDOW)

    def create_order_and_get_number_of_order_on_modal_window(self):
        self.add_ingredient_in_order()
        self.click_create_order()
        self.get_number_of_order_in_modal_confirmation()
        self.close_modal_window()
