from selenium.webdriver.common.by import By


class RepairPasswordLocators:
    REPAIR_PASSWORD_BUTTON = By.XPATH, ".//*[contains(text(), 'Восстановить пароль')]"
    HEADER_REPAIR_PASSWORD = By.XPATH, ".//h2[text() = 'Восстановление пароля']"
    REPAIR_BUTTON = By.XPATH, ".//*[text() = 'Восстановить']"
    SHOW_PASSWORD = By.XPATH, ".//div[@class = 'input__icon input__icon-action']"
    PASSWORD_VEIW = By.XPATH, ".//*[contains (@class, 'input_status_active')]"
    INPUT_NAME = By.XPATH, './/*[text()="Имя"]/following-sibling::input'
    INPUT_EMAIL = By.XPATH, './/*[text()="Email"]/following-sibling::input'
    INPUT_PASSWORD = By.XPATH, './/*[text()="Пароль"]/following-sibling::input'
    ENTER_BUTTON = By.XPATH, './/*[contains (@class, "button_button")]'
