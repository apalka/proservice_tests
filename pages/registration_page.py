from test_helpers import functional_helpers as fh
from pages.base_page import BasePage


class RegistrationPageClass(BasePage):

    def user_registration(self, firstname, lastname, pesel, email, phone_number, login, password):
        """Register user using given parameters
        :param driver: webdriver instance
        :param firstname: user firstname
        :param lastname: user firstname
        :param pesel: user PESEL number
        :param email: user email adress
        :param phone_nubmer: user phone number
        :param login: user login
        :param password: user password
         ...
         :return: None
        """
        cookies_xpath = '//i[@class="icon ion-md-close"]'
        firstname_xpath = '//input[@id="client-name"]'
        lastname_xpath = '//input[@id="client-surname"]'
        pesel_xpath = '//input[@id="client-pesel"]'
        residence_xpath = '//select[@id="residence"]'
        residence_option_xpath = residence_xpath + '/option[contains(text(),"Rezydent")]'
        email_xpath = '//input[@id="client-email"]'
        prefix_xpath = '//select[@id="client-phone-number-prefix"]'
        prefix_option_xpath = prefix_xpath + '/option[contains(text(),"+61")]'
        phone_xpath = '//input[@id="client-phone-number-number"]'
        country_xpath = '//select[@id="client-country"]'
        country_option_xpath = country_xpath + '/option[contains(text(),"AUSTRALIA")]'
        login_xpath = '//input[@id="client-login"]'
        password_xpath = '//input[@id="client-password"]'
        confirm_password_xpath = '//input[@id="client-password-repeat"]'
        promo_code_xpath = '//input[@id="client-promo-code"]'
        checkmark_xpath = '//i[@class="icon ion-md-checkmark"]'
        next_button_xpath = '//button[@type="submit"]'
        promo_code = '1234'

        """Filling the form"""

        fh.wait_for_element(self.driver, cookies_xpath)
        cookies_modal = self.driver.find_element_by_xpath(cookies_xpath)
        cookies_modal.click()

        fh.wait_for_element(self.driver, firstname_xpath)
        firstname_input = self.driver.find_element_by_xpath(firstname_xpath)
        firstname_input.send_keys(firstname)

        lastname_input = self.driver.find_element_by_xpath(lastname_xpath)
        lastname_input.send_keys(lastname)

        pesel_input = self.driver.find_element_by_xpath(pesel_xpath)
        pesel_input.send_keys(pesel)

        residence_dropdown = self.driver.find_element_by_xpath(residence_xpath)
        residence_dropdown.click()

        fh.wait_for_element(self.driver, residence_option_xpath)
        residence_option_element = self.driver.find_element_by_xpath(residence_option_xpath)
        residence_option_element.click()

        email_input = self.driver.find_element_by_xpath(email_xpath)
        email_input.send_keys(email)

        prefix_dropdown = self.driver.find_element_by_xpath(prefix_xpath)
        prefix_dropdown.click()

        fh.wait_for_element(self.driver, prefix_option_xpath)
        prefix_option = self.driver.find_element_by_xpath(prefix_option_xpath)
        prefix_option.click()

        phone_input = self.driver.find_element_by_xpath(phone_xpath)
        phone_input.send_keys(phone_number)

        country_dropdown = self.driver.find_element_by_xpath(country_xpath)
        country_dropdown.click()

        fh.wait_for_element(self.driver, country_option_xpath)
        country_option = self.driver.find_element_by_xpath(country_option_xpath)
        country_option.click()

        login_input = self.driver.find_element_by_xpath(login_xpath)
        login_input.send_keys(login)

        password_input = self.driver.find_element_by_xpath(password_xpath)
        password_input.send_keys(password)

        confirm_password_input = self.driver.find_element_by_xpath(confirm_password_xpath)
        confirm_password_input.send_keys(password)

        fh.wait_for_element(self.driver, promo_code_xpath)
        promo_code_input = self.driver.find_element_by_xpath(promo_code_xpath)
        promo_code_input.send_keys(promo_code)

        agreement_checkmark = self.driver.find_element_by_xpath(checkmark_xpath)
        agreement_checkmark.click()

        fh.wait_for_element(self.driver, next_button_xpath)
        next_button = self.driver.find_element_by_xpath(next_button_xpath)
        next_button.click()
