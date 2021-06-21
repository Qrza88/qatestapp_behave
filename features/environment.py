from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    context.location = "https://qa-task.netlify.app/"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.browser.get(context.location)


def after_scenario(context, scenario):
    context.browser.quit()
