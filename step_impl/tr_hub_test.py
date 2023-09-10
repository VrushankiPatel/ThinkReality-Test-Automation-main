import os
import time
from appium import webdriver
from getgauge.python import step
from utils.util import load_appium_driver_setting, countdown
from pages.tr_hub_page import TRHubPage
from selenium.common.exceptions import NoSuchElementException


class TRHubTest():
    @step("Launch TR Hub")
    def init(self):
        driver = webdriver.Remote("http://localhost:4723", load_appium_driver_setting(
            "com.lenovo.xr.hub", "com.lenovo.xr.hub.ParentActivity", enable_web_debugging=True))
        # Implicitly wait for N seconds if the element is not present
        driver.implicitly_wait(5)

        self.trhub_page = TRHubPage(driver)

    @step("Display OOBE on the first launch of TR Hub")
    def oobe_display(self):
        retries = 3

        for _ in range(retries):
            try:
                # Modify system settings
                self.trhub_page.tap_switch()
                break
            except NoSuchElementException:
                self.allow_tr_hub_access_a3()  # This can pop up anytime

        for _ in range(retries):
            try:
                # Display over other apps
                self.trhub_page.overlay_permission_button.click()
                self.trhub_page.grant_display_over_other_apps("TR Hub")
                break
            except NoSuchElementException:
                self.allow_tr_hub_access_a3()  # This can pop up anytime

        try:
            self.trhub_page.continue_as_guest_button.click()
        except NoSuchElementException:
            pass

        self.trhub_page.agree_usage_and_diagnostics()
        self.trhub_page.grant_snapdragon_space_permissions()

    @step("User can login TR portal")
    def login_trhub(self):

        self.trhub_page.sign_in_button.click()
        self.trhub_page.switch_driver_to_webview()
        self.trhub_page.login_on_portal(
            os.getenv('PORTAL_USERNAME'), os.getenv('PORTAL_PASSWORD'))

        self.trhub_page.switch_driver_to_native_app()

    @step("User can launch TR Home")
    def open_tr_home(self):
        self.trhub_page.passthrough_with_appium()
        self.trhub_page.open_trhome_button.click()

        # Wait for some time to launch the app
        time.sleep(10)

        # Ensure the app is launched
        assert "com.lenovo.xr.trhome" in self.trhub_page.check_current_activity()

        self.trhub_page.force_stop_app(package_name="com.lenovo.xr.trhome")

    @step("User can launch TR Cast")
    def open_tr_cast(self):
        self.trhub_page.passthrough_with_appium()
        self.trhub_page.open_trcast_button.click()

        # Wait for some time to launch the app
        time.sleep(5)

        # Ensure the app is launched
        assert "com.lenovo.xr.trcast" in self.trhub_page.check_current_activity()

        self.trhub_page.force_stop_app(package_name="com.lenovo.xr.trcast")

    @step("User can log out of TR Hub")
    def logout(self):
        self.trhub_page.agree_usage_and_diagnostics()

        self.trhub_page.permission_button.click()
        self.trhub_page.back_to_previous_page()

        self.trhub_page.navigation_drawer.click()
        self.trhub_page.sign_out_button.click()
        self.trhub_page.confirm_button.click()

    @step("Glass firmware is properly displayed in the 'About' section and is updated to the latest version")
    def get_glass_firmware(self):
        self.trhub_page.passthrough_with_appium()

        firmware = self.trhub_page.get_firmware_display()

        assert firmware.startswith(
            f"A3_user_S{os.getenv('LATEST_GLASS_FIRMWARE_VERSION')}")

    def allow_tr_hub_access_a3(self):
        # Always allow TR Hub to access ThinkReality A3
        self.trhub_page.always_use_button.click()
        self.trhub_page.confirm_button.click()

    @step("Launch TR Hub and check login status")
    def init_without_reset(self):
        driver = webdriver.Remote("http://localhost:4723", load_appium_driver_setting(
            "com.lenovo.xr.hub", "com.lenovo.xr.hub.ParentActivity", no_reset=True))

        # Implicitly wait for N seconds if the element is not present
        driver.implicitly_wait(5)

        self.trhub_page = TRHubPage(driver)

        self.trhub_page.start_app_activity()

        if self.trhub_page.username_text != "Guest Mode":
            print("The TR hub is logged in")
            assert True

        else:
            print("The TR hub is not logged in")
            assert False

    @step("Launch TR Hub without clear cache")
    def init_without_reset_cache(self):
        driver = webdriver.Remote("http://localhost:4723", load_appium_driver_setting(
            "com.lenovo.xr.hub", "com.lenovo.xr.hub.ParentActivity", no_reset=True))
        # Implicitly wait for N seconds if the element is not present
        driver.implicitly_wait(5)

        self.trhub_page = TRHubPage(driver)

        self.trhub_page.start_app_activity()

    @step("Select <option> on updating A3 glasses firmware")
    def update_a3_glasses_firmware_version(self, option):
        # If the glass firmware update is not required for the test, then just consider pass
        if os.getenv('TEST_GLASS_FW_UPDATE').lower() != "true":
            assert True
            return


        # Explicit wait for five more seconds to show firmware update window
        second = 30
        time.sleep(5)

        if option == "No":
            self.trhub_page.firmware_update_dialog_no_button.click()

            try:  # Sometimes "no" button appear twice
                self.trhub_page.firmware_update_dialog_no_button.click()
            except NoSuchElementException:
                pass

        elif option == "Yes":
            self.trhub_page.firmware_update_dialog_yes_button.click()

            try:
                self.trhub_page.continue_as_guest_button.click()
            except NoSuchElementException:
                pass

            self.trhub_page.passthrough_with_appium()

            # If we choose to update the firmware, then the firmware download dialog should appear in the main page of TR Hub
            assert self.trhub_page.firmware_download_dialog is not None

            # We need to wait for the update to run. To achieve that, we check if the status message have reached 100 percent
            while "100" not in self.trhub_page.firmware_download_status_text:
                time.sleep(1)

            print(f"Wait {second} seconds for update to be fully effective")
            countdown(second) # Wait for the update to be fully effective
            self.trhub_page.force_stop_app()
    
    @step("Wait for user to re-plug the A3 glasses and check firmware information")
    def wait_for_user_to_replug_glasses(self):
        # If the glass firmware update is not required for the test, then just consider pass
        if os.getenv('TEST_GLASS_FW_UPDATE').lower() != "true":
            assert True
            return

        # Give user N times of retry to get the correct firmware version
        # If it still don't work => Fail
        retries = 3
        second = 30

        for i in range(retries):
            try:
                # Take timed input using inputimeout() function
                print(f"Please use {second} seconds to replug the glasses...")
                countdown(second)

                self.get_glass_firmware()
                break # If did not assert error => pass the test
            
            except (AssertionError, NoSuchElementException):
                # Declare the timeout statement
                if i != retries - 1:
                    print("Try again!!!")
                    continue
                    
                else:
                    assert False