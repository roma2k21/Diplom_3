from selenium.webdriver.common.by import By


class UniversalLocators:
    CLOSE_MODAL_WINDOW = By.XPATH, '//*[contains(@class, "Modal_modal__close")]'
    HISTORY_ORDER_LIST = By.XPATH, '//*[contains(@class, "text_type_digits-default") and contains(text(), "#")]'
