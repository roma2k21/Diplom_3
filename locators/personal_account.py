from selenium.webdriver.common.by import By


class LKPageLocators:
    LK_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]/parent::a'
    ACCOUNT_TEXT = By.XPATH, './/*[contains(@class, "Account_text")]'
    LIST_NUMBER_ORDER = By.XPATH, './/*[contains(@class, "Account_contentBox__2CPm3")]'
    HEADER_ASSEMBLER_BURGER = By.XPATH, './/*[text() = "Соберите бургер"]'
    HISTORY_BUTTON = By.XPATH, './/a[@href = "/account/order-history"]'
    HISTORY_FORM = By.XPATH, './/div[contains(@class, "Account_contentBox")]'
    EXIT_BUTTON = By.XPATH, './/button[text()="Выход"]'
    INPUT_TITLE = By.XPATH, './/h2[text() = "Вход"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text() = "Конструктор"]'
    ORDER_FEED_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li'
    HEADER_ORDER_FEED = By.XPATH, './/*[contains(@class, "text_type_main-large")]'
    NUMBER_ORDER = By.XPATH, './/*[contains(text(), "#")]'
