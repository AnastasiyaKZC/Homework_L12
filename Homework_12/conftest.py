import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from Homework_12.utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # browser = Browser(Config(driver=driver))  # исправлено название переменной
    browser = Browser(Config())
    browser.config.driver = driver  # Назначаем driver отдельно
    yield browser  # фикстура отдаёт browser

    attach.add_screenshot(browser)
    attach.add_logs(browser) # консольные ошибки браузера
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()  # закрытие драйвера после теста