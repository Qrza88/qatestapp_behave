from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class QaTestHome(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://qa-task.netlify.app/')

    locator_dictionary = {
        "command_input": (By.ID, 'mat-input-0'),
        "execute_button": (By.XPATH, '//BUTTON[@color="primary"]'),
        "error_icon": (By.XPATH, '//MAT-ICON[@role"img"]'),
        "output_window": (By.XPATH, '//PRE'),
    }