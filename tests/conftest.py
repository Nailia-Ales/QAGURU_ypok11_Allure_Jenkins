import os
from datetime import datetime
from urllib.parse import quote_plus

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

#from utils.allure_attach import add_html
#import attach
import utils.allure_attach as attach

load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"

    # Настройка опций для браузера
    options = Options()
    options.page_load_strategy = "eager"
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    # Получаем логин, пароль и URL из .env
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")
    encoded_pass = quote_plus(selenoid_pass)

    # Подключаем удалённый WebDriver через авторизацию
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{encoded_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    # Применяем настройки к selene
    browser.config.driver = driver
    browser.config.type_by_js = True
    browser.config.window_height = 2500
    browser.config.window_width = 1400

    yield

    # Прикрепляем артефакты после выполнения теста
    print(attach.__file__)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope="function")
def today_date():
    return datetime.now().strftime("%d %B, %Y")