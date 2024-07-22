from bs4 import BeautifulSoup
import time
import random
from ChromeDriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException


class ExtractOptionScraper:

    def __init__(self):

        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        ]


    def start_driver(self):
        self.driver = WebDriver.start_driver(self)
        return self.driver

    def main(self, username, password):
        try:
            driver = self.start_driver()
            driver.get("https://app.expertoption.com/login?login=1")

            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Email"]'))
            )
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
            )
            email_input.send_keys(username)
            password_input.send_keys(password)

            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="at_login_button"]'))
            )
            login_button.click()

        except Exception as e:
            print(e)
            time.sleep(5)
            driver.quit()

if '__main__' == __name__:
    app = ExtractOptionScraper()
    app.main('no5510425@gmail.com', 'civil hacker')