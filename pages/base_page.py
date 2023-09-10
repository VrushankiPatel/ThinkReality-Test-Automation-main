import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from utils.android import swipe_up


class BasePage:
    def __init__(self, driver, package_name, activity_name):
        self.driver = driver
        self.package_name = package_name
        self.activity_name = activity_name

    # Toggle switch to allow/disallow permission in settings
    @property
    def toggle_switch(self):
        return self.driver.find_element(by=AppiumBy.ID, value="android:id/switch_widget")

    # Confirm button in any popup window
    @property
    def confirm_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="android:id/button1")

    # Always allow TR Hub to access ThinkReality A3
    @property
    def always_use_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="android:id/alwaysUse")

    # Select an app by a click on app name
    def select_app(self, app_name):
        self.driver.find_element(
            by=AppiumBy.XPATH, value=f"//android.widget.TextView[@content-desc='{app_name}']").click()

    # Click Toggle switch
    def tap_switch(self):
        self.toggle_switch.click()
        self.driver.back()

    # back button/click to get to the previous page
    def back_to_previous_page(self):
        self.driver.back()

    # Allow access to display over other apps
    def grant_display_over_other_apps(self, app_name):
        # After enter the app menu, if cannot find, then we need to swipe up to find the app name
        try:
            self.select_app(app_name)
        except NoSuchElementException:
            time.sleep(1)
            swipe_up()
            self.select_app(app_name)

        self.tap_switch()

        self.driver.back()

    # Wait for the N seconds web contexts to appear
    def switch_driver_to_webview(self):
        for _ in range(5):
            if len(self.driver.contexts) < 2:
                time.sleep(1)

        self.driver.switch_to.context(self.driver.contexts[-1])
    
    # After login switch the driver to native/ home page
    def switch_driver_to_native_app(self):
        self.driver.switch_to.context(self.driver.contexts[0])

    # adb execute command
    def adb_shell(self, command, args):
        return self.driver.execute_script("mobile: shell", {
            "command": command,
            'args': args,
            'includeStderr': True,
        })

    # Allow the camera usage permission while running the app
    def grant_camera_permissions(self, package_name=None):
        
        if not package_name:
            package_name = self.package_name
        
        self.driver.execute_script("mobile:changePermissions", {
            'action': "grant", 
            'appPackage': package_name, 
            'permissions': ["android.permission.CAMERA"]
        })

    # Swipe up action
    def swipe_up(self):
        self.adb_shell("input", "swipe 500 1500 0 0")

    # adb command to check current activity
    def check_current_activity(self):
        return self.adb_shell("dumpsys", "activity | grep 'mCurrentFocus'")['stdout']
    
    # adb command to start app activity
    def start_app_activity(self):
        self.adb_shell("am", f"start -n {self.package_name}/{self.activity_name}")

    # adb command to force stop app 
    def force_stop_app(self, package_name=None):
        if not package_name:
            package_name = self.package_name

        self.adb_shell("am", f"kill {package_name}")
