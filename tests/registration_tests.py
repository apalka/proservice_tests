from test_helpers.base_test_class import BaseTestClass
from test_helpers import functional_helpers as fh
from pages.mailhog_page import MailhogPageClass
from pages.registration_page import RegistrationPageClass
import time


class RegistrationPageTests(BaseTestClass):

    def test_correct_registration(self):
        #test data
        firstname = "John"
        lastname = 'Krasinsky'
        pesel = '84021455658'
        email = 'johnkrasinksy@test.com'
        phone_number = '555222333'
        login = 'JKrasinski1'
        password = 'Qwerty123!'

        registration_page = RegistrationPageClass(self.driver)
        mailhog_page = MailhogPageClass(self.driver)

        self.driver.get(self.registration_url)
        registration_page.user_registration(firstname, lastname, pesel, email, phone_number, login, password)
        # mailhog needs more time to load
        time.sleep(3)
        mailhog_page.get_and_confirm_sms_code()

        expected_text = "Rejestracja przebiegła pomyślnie"
        success_message_xpath = '//div[@role="dialog"]//h2'

        fh.wait_for_element(self.driver, success_message_xpath)
        success_message = self.driver.find_element_by_xpath(success_message_xpath).text

        self.assertIn(expected_text, success_message,
                      f'Success message differs from expected - registration failed')
