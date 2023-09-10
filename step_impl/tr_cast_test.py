import os
import time
import appium
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from getgauge.python import step
from utils.util import load_appium_driver_setting
from pages.tr_cast_page import TRCastPage
from pages.tr_cast_stream_page import TRCastStreamPage


class TRCastTest():
    @step("Launch TR Cast")
    def init(self):
        # Initialize Appium driver
        driver = appium.webdriver.Remote("http://localhost:4723", load_appium_driver_setting(
            "com.lenovo.xr.trcast", ".ui.activity.LauncherActivity", no_reset=True))

        # Implicitly wait for N seconds if the element is not present
        driver.implicitly_wait(3)

        self.trcast_page = TRCastPage(driver)
        self.trcast_page.grant_camera_permissions()

        # When you use no_reset=True, then you need to open app by adb commands
        self.trcast_page.start_app_activity()

    @step("Launch TR Portal")
    def init_tr_portal(self):
        # Initialize Selenium driver
        webdriver = selenium.webdriver.Chrome()
        webdriver.implicitly_wait(3)

        webdriver.get(
            "https://portal-platform.naea1.uds.lenovo.com/a3r6candidatese2ei/portal/think-reality/devices")
        self.trportal_page = TRCastStreamPage(webdriver)

    @step("Display OOBE on the first launch of TR Cast")
    def oobe_display(self):
        self.trcast_page.grant_display_over_other_apps("TR Cast")

    @step("Select cloud streaming")
    def select_cloud_streaming(self):
        # Sometimes it will just enter cloud streaming screen
        try:
            self.trcast_page.cloud_stream_radio_button.click()
            self.trcast_page.continue_button.click()
        except NoSuchElementException:
            pass

    @step("User can start a stream on the app")
    def start_stream_on_app(self):
        self.current_pin_code = self.trcast_page.pin_code
        self.trcast_page.start_stream_button.click()

        try:
            self.trcast_page.confirm_button.click()
        except NoSuchElementException:
            pass

        time.sleep(5)

    @step("User can stop a stream on the app")
    def stop_stream_on_app(self):
        self.trcast_page.stop_stream_button.click()

    @step("User can view the stream on the cloud portal with cloud streaming")
    def view_stream_on_portal(self):
        self.trportal_page.join_stream.click()

        # Change self.current_pin_code to actual code for testing purpose
        self.trportal_page.input_pin_code(self.current_pin_code)

        self.trportal_page.join_stream_button.click()

        # Wait for the stream to open
        time.sleep(2)

    @step("User can take a screenshot on the cloud portal")
    def screenshot_on_portal(self):
        self.trportal_page.screenshot_button.click()

    @step("User can pause the stream on the cloud portal")
    def pause_stream_on_portal(self):
        # Wait for few seconds then pause the stream
        time.sleep(2)
        self.trportal_page.pause_stream_button.click()

    @step("User can resume the stream on the cloud portal")
    def resume_stream_on_portal(self):
        # Wait for few seconds then resume the stream
        time.sleep(2)
        self.trportal_page.resume_stream_button.click()

    @step("User can close the stream on the cloud portal")
    def close_stream_on_portal(self):
        self.trportal_page.close_stream_button.click()

    @step("User can rejoin the stream on the cloud portal")
    def rejoin_stream_on_portal(self):
        # work as a refresh button
        self.trportal_page.refresh_page()
        # search bar and selecting appeared device
        self.find_and_select_device_on_tr_portal()
        # JOIN STREAM
        self.view_stream_on_portal()
        # Screenshot on cloud portal
        self.screenshot_on_portal()
        # pause stream  button on cloud portal
        self.pause_stream_on_portal()
        # resume stream button on cloud portal
        self.resume_stream_on_portal()
        # close stream button on cloud portal
        self.close_stream_on_portal()
        
    
    @step("User can take a screenshot on the app")
    def screenshot_on_app(self):
        self.trcast_page.screen_shot_button.click()

        try:
            self.trcast_page.confirm_button.click()
        except NoSuchElementException:
            pass

        # TODO: Also check if the screenshot actually exist in the storage


    @step("Launch another user TR Portal")
    # Another user on a different browser can join the stream if it is closed on the first browser by another user
    def init_another_tr_portal(self):
        # Initialize Selenium driver
        webdriver2 = selenium.webdriver.Chrome()
        webdriver2.implicitly_wait(3)

        webdriver2.get(
            "https://portal-platform.naea1.uds.lenovo.com/a3r6candidatese2ei/portal/think-reality/devices")
        self.trportal_page = TRCastStreamPage(webdriver2)


    @step("Login into the TR Portal with <choice> account")
    def login_tr_portal(self, choice):
        username, password = "", ""

        # Assign the username and password based on spec
        if choice == "main":
            username = os.getenv('PORTAL_MAIN_USERNAME')
            password = os.getenv('PORTAL_MAIN_PASSWORD')
        
        elif choice == "second":
            username = os.getenv('PORTAL_SECOND_USERNAME')
            password = os.getenv('PORTAL_SECOND_PASSWORD')

        # It is possible that the portal is already login
        try:
            self.trportal_page.login_portal_username.send_keys(username)
            self.trportal_page.login_portal_password.send_keys(password)
            self.trportal_page.log_in_button.click()

            # Wait the page to load
            time.sleep(3)
        except NoSuchElementException:
            pass

    @step("Find and select the current device on TR Portal")
    def find_and_select_device_on_tr_portal(self):
        self.trportal_page.device_search_bar.click()
        self.trportal_page.device_search_bar.send_keys(
            os.getenv("DEVICE_SERIAL_NUMBER"))
        self.trportal_page.device_search_bar.send_keys(Keys.ENTER)

        # Wait for the result to load
        time.sleep(1)
        self.trportal_page.select_appeared_device.click()
