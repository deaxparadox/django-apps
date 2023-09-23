# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.webdriver import WebDriver


# class MySeleniumTests(StaticLiveServerTestCase):
#     # fixtures = ["user-data.json"]

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_login(self):
#         self.selenium.get(f"{self.live_server_url}/login/")
#         username_input = self.selenium.find_element(By.NAME, "username")
#         username_input.send_keys("myuser")
#         password_input = self.selenium.find_element(By.NAME, "password")
#         password_input.send_keys("secret")
#         self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()