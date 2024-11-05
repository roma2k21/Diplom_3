from pages.base_page import BasePage
from locators.repair_password import RepairPasswordLocators


class RepairPassword(BasePage):
    # переход на страницу восстановления пароля по ĸнопĸе «Восстановить пароль»
    def transfer_to_repair_page(self):
        self.click_element_with_wait(RepairPasswordLocators.REPAIR_PASSWORD_BUTTON)
        return self.find_element_with_wait(RepairPasswordLocators.HEADER_REPAIR_PASSWORD)

    def input_email_and_click_button_repair(self, authorization_user):
        self.add_text_to_element(RepairPasswordLocators.INPUT_EMAIL, authorization_user[1])
        self.click_element_with_wait(RepairPasswordLocators.REPAIR_BUTTON)
        return self.find_element_with_wait(RepairPasswordLocators.HEADER_REPAIR_PASSWORD)

    def click_show_password(self):
        self.click_element_with_wait(RepairPasswordLocators.SHOW_PASSWORD)
        return self.find_element_with_wait(RepairPasswordLocators.PASSWORD_VEIW)

    def check_button_visibility(self):
        self.check_element_visibility(RepairPasswordLocators.ENTER_BUTTON)
        return self.find_element_with_wait(RepairPasswordLocators.ENTER_BUTTON)
