import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .components.navbar import Navbar
import logging


class BasePage:
    base_url = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)
        self.navbar = Navbar(browser)
        self.logger = logging.getLogger(__name__)

    # Common methods for other pages
    def open(self, path = "") -> None:
        url = f"{self.base_url}{path}"
        self.logger.info(f"Opening {url}")
        with allure.step(f"Open page {url}"):
            self.browser.get(url)

    def get_url(self) -> str:
        self.logger.info("Getting current page URL")
        return self.browser.current_url

    def find_element(self, locator) -> WebElement:
        self.logger.info(f"Finding element by locator: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_list_of_elements(self, locator, timeout=5) -> list:
        self.logger.info(f"Getting list of elements by locator: {locator}")
        try:
            wait = WebDriverWait(self.browser, timeout=timeout)
            elements = wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            elements = []
        return elements

    def click_element(self, locator) -> None:
        self.logger.info(f"Clicking element by locator: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator) -> str:
        self.logger.info(f"Getting text from element by locator: {locator}")
        element = self.find_element(locator)
        return element.text

    def enter_text(self, locator: tuple, text: str) -> None:
        self.logger.info(f"Entering text: '{text}' in field: '{locator}'")
        field = self.find_element(locator)
        field.clear()
        field.send_keys(text)

    def is_element_present(self, locator) -> bool:
        self.logger.info(f"Checking if element is present by locator: {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # Method to check that element is NOT appearing on page during timeout(3s)
    def is_not_element_present(self, locator, timeout=3) -> bool:
        self.logger.info(f"Checking if element is NOT present by locator: {locator}")
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    # visibility_of_element_located - is element visible
    # presence_of_element_located  - is element in DOM
    # Method to check that element disappearing from page
    def is_element_disappeared(self, locator, timeout=3) -> bool:
        self.logger.info(f"Checking if element disappeared by locator: {locator}")
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    '''
    WebDriverWait(driver, timeout, poll_frequency: float = 0.5, ignored_exceptions: tuple)
        
      - ignored_exceptions: Iterable (tuple in python) structure of exception classes ignored
        during calls. By default, it contains NoSuchElementException only.
        
    Explict wait list: https://selenium-python.readthedocs.io/waits.html 
    
    .until(method): 
    Ожидает, пока предоставленный method вернет что-либо, кроме False.
    Т.е. ждет, когда EC вернет True 
    Если method продолжает возвращать False до истечения времени ожидания, 
    будет вызвано исключение TimeoutException.

    .until_not(method): 
    Ожидает, пока предоставленный method не вернет False. 
     Т.е. ждет, когда EC вернет False
    Если метод не вернет False до истечения времени ожидания, 
    будет вызвано исключение TimeoutException.
    
    К слову, судя по всему явные ожадания из EC (e.g visibility_of_element_located
    это НЕ метод. Это класс с магическим методом __call__.
    __call__() позволяет вызывать экземпляр класса как функцию.
    ПРИ ЭТОМ ЭКЗЕМЛЯР КЛАССА ПЕРЕДАЕТСЯ В метод until, где вызывается как ФУНКЦИЯ.
    Т.е. если создавать класс с __call__, нужно сначала создать экземпляр этого класса. 
    При этом в __call__(self, some_params) можно передавать параметры 
    при вызове через экземпляр класса. - проверить
     '''



