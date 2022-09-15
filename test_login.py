import time

from altunityrunner import By


class TestLoginScreen:
    def __init__(self, appium_driver, alt_driver):
        self.registered_email_text = "testaccount-am1@pso.com"
        self.registered_pass_text = "Welcome20!"
        self.email_obj = alt_driver.wait_for_object(By.ID, "17130")
        self.pass_obj = alt_driver.wait_for_object(By.ID, "25406")
        self.guest_obj = alt_driver.wait_for_object(By.ID, "23742")
        print("objects are found by altunity")

    def guest_login(self):
        self.guest_obj.click()

    def login_happy_path(self):
        # self.email_obj.call_component_method("LocalizedText", "SetKey", [email_text])
        print("username added")
        self.email_obj.set_text(self.registered_email_text)
        time.sleep(5)
        self.pass_obj.set_text(self.registered_pass_text)

        # pass_obj.call_component_method("LocalizedText","SetKey",[pass_text])
        print("password added")
