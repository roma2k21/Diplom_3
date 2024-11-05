from selenium.webdriver.common.by import By


class MainPageLocators:
    INRGEDIENT = By.XPATH, './/img[@alt = "Флюоресцентная булка R2-D3"]'
    DETAIL_INGREDIENT = By.XPATH, './/h2[text() = "Детали ингредиента"]'
    INGEDIENT_BASKET = By.XPATH, './/*[contains(@class, "constructor-element_pos_top")]'
    COUNTER_BASKET = By.XPATH, './/*[contains(@class, "text_type_digits-medium")]'
    CREATE_ORDER_BUTTON = By.XPATH, './/*[contains(@class, "button_button__33qZ0")]'
    TITLE_IDENTIFAIR_ORDER = By.XPATH, './/*[@class = "undefined text text_type_main-medium mb-15"]'
    OVERLAY = By.XPATH, './/div[@class = "Modal_modal_overlay__x2ZCr"]'
    ORDER_NUMBER_IN_MODAL_WINDOW = By.XPATH, './/*[contains(@class, "Modal_modal__title_shadow__3ikwq")]'
    NUMBER_OF_ORDER_IN_MODAL_WINDOW = By.XPATH, './/section[contains(@class, "Modal_modal_opened")]//h2'
