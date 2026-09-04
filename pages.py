from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from decimal import Decimal
import os


class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def element(self, test_id):
        previous_rect = None

        def stable_element(driver):
            nonlocal previous_rect
            try:
                element = driver.find_element(By.CSS_SELECTOR, f'[data-test="{test_id}"]')
                if not element.is_displayed():
                    previous_rect = None
                    return False
                rect = element.rect
                stable = rect == previous_rect
                previous_rect = rect
                return element if stable else False
            except (NoSuchElementException, StaleElementReferenceException):
                previous_rect = None
                return False

        return self.wait.until(stable_element)

    def login(self):
        self.driver.get(os.environ['BASE_URL'])
        self.element('username').send_keys(os.environ['TEST_USER'])
        self.element('password').send_keys(os.environ['TEST_PASSWORD'])
        self.element('login-button').click()
        self.wait.until(EC.url_contains('/inventory.html'))
        self.element('inventory-list')

    def sort(self, value):
        Select(self.element('product-sort-container')).select_by_value(value)

    def prices(self):
        def read_prices(driver):
            try:
                catalog = driver.find_element(By.CSS_SELECTOR, '[data-test="inventory-list"]')
                elements = catalog.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
                return [int(Decimal(element.text.removeprefix('$')) * 100) for element in elements] or False
            except (NoSuchElementException, StaleElementReferenceException):
                return False
        return self.wait.until(read_prices)

    def open_product(self, product_id):
        self.element(f'item-{product_id}-title-link').click()
        self.wait.until(EC.url_contains(f'/inventory-item.html?id={product_id}'))

    def open_cart(self):
        self.element('shopping-cart-link').click()
        self.wait.until(EC.url_contains('/cart.html'))
