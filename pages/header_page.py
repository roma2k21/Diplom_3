import data
from locators.main_page_locators import MainPageLocators
from locators.personal_account import LKPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def click_lk_page(self):
        self.wait_dissapear_modal_window()
        if data.driver_name == 'chrome':
            self.click_element_with_wait(LKPageLocators.LK_BUTTON)
        else:
            self.click_on_element(LKPageLocators.LK_BUTTON)

    def transfer_to_button_on_lk(self):
        self.check_element_visibility(LKPageLocators.ACCOUNT_TEXT)
        return self.find_element_with_wait(LKPageLocators.ACCOUNT_TEXT)

    def click_constructor_page(self):
        self.wait_dissapear_modal_window()
        if data.driver_name == 'chrome':
            self.click_element_with_wait(LKPageLocators.CONSTRUCTOR_BUTTON)
        else:
            self.click_on_element(LKPageLocators.CONSTRUCTOR_BUTTON)

    def transfer_to_button_constructor(self):
        return self.find_element_with_wait(LKPageLocators.HEADER_ASSEMBLER_BURGER)

    def click_order_feed_page(self):
        self.wait_dissapear_modal_window()
        if data.driver_name == 'chrome':
            self.click_element_with_wait(LKPageLocators.ORDER_FEED_BUTTON)
        else:
            self.click_on_element(LKPageLocators.ORDER_FEED_BUTTON)

    def transfer_to_order_feed(self):
        return self.find_element_with_wait(LKPageLocators.HEADER_ORDER_FEED)

    def wait_dissapear_modal_window(self):
        self.check_element_is_disappear(MainPageLocators.OVERLAY)
