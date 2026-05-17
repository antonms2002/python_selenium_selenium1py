import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# pytest_addoption - это хук pytest, Он автоматически вызывается при старте, добавляет пользовательские опции cmd
# parser - это экземпляр класса pytest.Parser.
# pytest создаёт его внутри себя на раннем этапе запуска.
def pytest_addoption(parser):
    #  --language - регистрация флага
    # action='store' - что делаем со значением
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")


@pytest.fixture(scope="function")
# request - встроенная фикстура, предоставляющая контекст текущего теста.
# Через request можно получить:
#   - глобальную конфигурацию pytest: request.config,
#   - параметры командной строки: request.config.getoption(),
#   - информацию о текущем тесте (имя, маркеры, параметры параметризации): request.node, request.param.
#      Т.е. можно, например написать в фикстуре ниже print(request.node.name) и
#      при каждом тесте, в который передается фикстура browser (или фикстуры в цепочке)
#      будет выводится имя теста
#   - область видимости и имя самой фикстуры: request.scope, request.fixturename.
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

# Screenshot on failure
# Декоратор говорит, что добавляем код к существующему хуку
@pytest.hookimpl
# Хук pytest_runtest_makereport автоматически вызывается после setup, call, teardown каждого теста и отвечет за отчет
# Передаем item - объект теста и call - детали выполнения теста
def pytest_runtest_makereport(item, call):
    # call.when возвращает какой этой этап теста прошел (setup, call, teardown).
    # call.excinfo - информация был ли exception (тот же AssertionError)
    if call.when == "call" and call.excinfo is not None:
        # Получаем экзепляр браузера в тесте
        browser = item.funcargs.get("browser")
        if browser:
            try:
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name=f"Screenshot on failure: {item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except UnexpectedAlertPresentException:
                allure.attach(
                    "Failed to make screenshot: UnexpectedAlertPresentException",
                    attachment_type=allure.attachment_type.TEXT
                )

@pytest.fixture(scope="function")
def main_page(browser):
    return MainPage(browser)

@pytest.fixture(scope="function")
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture(scope="function")
def product_page(browser):
    return ProductPage(browser)

@pytest.fixture(scope="function")
def cart_page(browser):
    return CartPage(browser)