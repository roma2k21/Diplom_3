from selenium.webdriver.common.by import By


class OrderFeedLocators:
    TITLE_ORDER = By.XPATH, './/p[contains(text(),"Cостав")]'
    NUMBER_OF_ORDER = By.XPATH, './/*[contains(@class, "text_type_digits-large")]'
    COUNT_ALL_TIME = By.XPATH, './/*[text()="Выполнено за все время:"]/following-sibling::p'
    COUNT_CREATE_ORDER_TODAY = By.XPATH, './/*[text()="Выполнено за сегодня:"]/following-sibling::p'
    NUMBER_ORDER_IN_WORK = By.XPATH, './/ul[contains(@class, "OrderFeed_orderListReady")]'
    COUNT_IN_WORK = By.XPATH, './/*[contains(@class, "orderListReady")]/child::li[@class="text text_type_digits-default mb-2"]'
    LIST_NAME_BURGER = By.XPATH, './/*[contains(@class, "text text_type_main-medium mb-2")]'
    TITILE_MODAL_WINDOW = By.XPATH, './/*[@class = "text text_type_main-medium mb-8"]'
