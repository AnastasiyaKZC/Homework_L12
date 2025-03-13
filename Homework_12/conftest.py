import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach
from dotenv import load_dotenv

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

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

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
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