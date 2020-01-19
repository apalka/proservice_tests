from test_helpers import functional_helpers as fh
from pages.base_page import BasePage
import re


mailhog_user = "swinka"
mailhog_pass = "123qweQWE"
mailhog_host = "fintest7.mailhog.devfin24.pl/"
mailhog_url = 'https://{}:{}@{}'.format(mailhog_user, mailhog_pass, mailhog_host)


class MailhogPageClass(BasePage):

    def get_and_confirm_sms_code(self):
        log_list_xpath = '//*[@class="msglist-message row ng-scope"]'
        message_xpath = '//*[@id="preview-plain"]'
        code_input_xpath = '//*[@id="code"]'
        submit_button_xpath = '//*[@id="sendsms"]'

        open_new_card = f"window.open('{mailhog_url}','_blank');"
        self.driver.execute_script(open_new_card)
        self.driver.switch_to_window(self.driver.window_handles[-1])

        fh.wait_for_elements(self.driver, log_list_xpath)
        log_list = self.driver.find_elements_by_xpath(log_list_xpath)
        log_list[0].click()

        fh.wait_for_element(self.driver, message_xpath)
        message = self.driver.find_element_by_xpath(message_xpath).text

        sms_code = re.findall('\d+', message)[0]
        self.driver.switch_to_window(self.driver.window_handles[0])

        fh.wait_for_element(self.driver, code_input_xpath)
        code_input = self.driver.find_element_by_xpath(code_input_xpath)
        code_input.send_keys(sms_code)

        submit_button = self.driver.find_element_by_xpath(submit_button_xpath)
        submit_button.click()
