from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        target = self.driver.find_element(*locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def add_text_to_element(self, locator, text):
        return self.find_element_with_wait(locator).send_keys(text)

    def check_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def check_element_is_disappear(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, value))

    def drag_and_drop_element(self, locator_1, locator_2):
        draggable = self.find_element_with_wait(locator_1)
        droppable = self.find_element_with_wait(locator_2)
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, droppable).perform()

    def drag_and_drop_script(self, source, target):
        source_element = self.find_element_with_wait(source)
        target_element = self.find_element_with_wait(target)
        script = """
                    function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                        var dataTransfer = new DataTransfer();
                        var dragStartEvent = new DragEvent('dragstart', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragStartEvent);
    
                        var dropEvent = new DragEvent('drop', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        destinationNode.dispatchEvent(dropEvent);
    
                        var dragEndEvent = new DragEvent('dragend', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragEndEvent);
                    }
                    simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                    """
        self.driver.execute_script(script, source_element, target_element)

    def get_number_order(self, locator):
        elements = self.find_elements_with_wait(locator)
        text_element = elements[0].text
        return text_element.replace('#', '')