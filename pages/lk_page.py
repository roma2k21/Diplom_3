from pages.base_page import BasePage
from locators.personal_account import LKPageLocators
from locators.universal_locators import UniversalLocators
import data


class PersonalAccountPage(BasePage):
    # переход в личный кабинет
    def click_history_page(self):
        if data.driver_name == 'chrome':
            self.click_element_with_wait(LKPageLocators.HISTORY_BUTTON)
        else:
            self.click_on_element(LKPageLocators.HISTORY_BUTTON)

    def transfer_to_history_page(self):
        return self.find_element_with_wait(LKPageLocators.LIST_NUMBER_ORDER)

    def click_exit_from_account(self):
        if data.driver_name == 'chrome':
            self.click_element_with_wait(LKPageLocators.EXIT_BUTTON)
        else:
            self.click_on_element(LKPageLocators.EXIT_BUTTON)

    def exit_from_account(self):
        return self.find_elements_with_wait(LKPageLocators.INPUT_TITLE)

    def get_number_order_lk_page(self):
        return self.get_number_order(UniversalLocators.HISTORY_ORDER_LIST)
