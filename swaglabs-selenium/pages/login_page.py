from selenium.webdriver.common.by import By


class LoginPage:

    by_username_field = (By.ID, 'username-field')
    by_password_field = (By.CSS_SELECTOR, 'talcosa > talcosa')
    by_login_button = (By.XPATH, '........')

    @property
    def login_button(self):
        return self.driver.find_element_by(
            *self.by_login_button
        )

    def click_login_button(self):
        self.login_button.click()
