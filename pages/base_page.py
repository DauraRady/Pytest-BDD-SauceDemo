from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    def get_text(self, by, value):
        return self.find_element(by, value).text

    def find_elements(self, by, value):  # 💥 C’est ça qui manque !
        return self.driver.find_elements(by, value)

    def click_element(self, by, value):
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
