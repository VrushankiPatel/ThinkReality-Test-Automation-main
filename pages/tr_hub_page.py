from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class TRHubPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "com.lenovo.xr.hub", "com.lenovo.xr.hub.ParentActivity")

    # The checkbox to allow all Lenovo apps to have usage and diagnostics permissions
    @property
    def allow_apps_checkbox(self):
        return self.driver.find_element(by=AppiumBy.ID, value='com.lenovo.xr.hub:id/appsCheckBox')

    # The checkbox to allow all ThinkReality eXtensions to have usage and diagnostics permissions
    @property
    def allow_sdk_checkbox(self):
        return self.driver.find_element(by=AppiumBy.ID, value='com.lenovo.xr.hub:id/sdkCheckBox')

    # The 'continue' button
    @property
    def continue_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/continueButton")

    # The permission button to enable neccesary permissions
    @property
    def permission_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value='com.lenovo.xr.hub:id/permission_button')

    # The 'Display over other apps' column in Snapdragon spaces services
    @property
    def snapdragon_display_permission_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[contains(@text,'Display')]")

    # The button that appear on overlay popup
    @property
    def overlay_permission_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/overlay_perm_settings_button")

    # The button to launch TR Home
    @property
    def open_trhome_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/TRHome_open_btn")

    # The button to launch TR Cast
    @property
    def open_trcast_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/ARCast_open_btn")

    # The top left corner to open the navigation drawer
    @property
    def navigation_drawer(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc='Open navigation drawer']")

    # A3 Firmware Version in the 'about' section
    @property
    def firmware_text(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/a3FirmwareVersionValueText")

    # The ABOUT button in the navigation drawer
    @property
    def about_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[contains(@text,'ABOUT')]")

    # The SIGN OUT button in the navigation drawer to sign out
    @property
    def sign_out_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[contains(@text,'SIGN OUT')]")

    # Navigate up to navigate back to the drawer for sign in
    @property
    def navigate_up_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc='Navigate up']")

    # Sign in button to sign into the TR Hub
    @property
    def sign_in_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/loginButton")

    # Navigate the sign in button to Sign in
    @property
    def navigation_sign_in_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[contains(@text,'SIGN IN')]")

    # 'Continue as guest' to use the TR Hub without sign in
    @property
    def continue_as_guest_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/guestButton")

    # Enter username to sign in
    @property
    def tr_portal_username_input(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[@id='username']")

    # Followed by password to sign in
    @property
    def tr_portal_password_input(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[@id='password']")

    # Login button to login to the portal
    @property
    def tr_portal_login_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[@id='loginForm']/div[1]/div[3]/input")

    # Accept cookies button
    @property
    def tr_portal_accept_cookies_button(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value="//*[@id='acceptBtn']")

    # The given username appear in the navigation drawer
    @property
    def username_text(self):
        self.navigation_drawer.click()
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/username_text").text

    @property
    def firmware_update_dialog_no_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/dialog_no_button")

    @property
    def firmware_update_dialog_yes_button(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/dialog_yes_button")

    @property
    def firmware_download_dialog(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/firmware_download_status_popup")

    @property
    def firmware_download_status_text(self):
        return self.driver.find_element(by=AppiumBy.ID, value="com.lenovo.xr.hub:id/firmware_update_text").text

    # Click the checkboxes to allow usage and diagnostic in the about section
    def agree_usage_and_diagnostics(self):
        self.allow_apps_checkbox.click()
        self.allow_sdk_checkbox.click()
        self.continue_button.click()

    # Enable Snapdragon spaces services permissions
    def grant_snapdragon_space_permissions(self):

        self.permission_button.click()

        # First grant camera access (can be done with adb shell)
        self.grant_camera_permissions(
            package_name="com.qualcomm.qti.spaces.services")

        # "Display over other apps" setting cannot be grant with adb, need to specify steps
        # Sometimes the snapdragon will display popup to ask for "Display over other apps"
        try:
            self.confirm_button.click()
        except NoSuchElementException:
            self.snapdragon_display_permission_button.click()

        self.grant_display_over_other_apps("Snapdragon Spaces Services")

        # back till the TR Hub home page
        self.driver.back()

    # Click TR Home to open it
    def open_a3_home(self):
        self.open_trhome_button.click()

    # Click TR Cast to open it
    def open_tr_cast(self):
        self.open_trcast_button.click()

    # When logging out: Uncheck Agree and Diagnostic, and Permissions
    def logout(self):
        self.agree_usage_and_diagnostics()

        self.permission_button.click()
        self.driver.back()  # Back to main menu

        self.navigation_drawer.click()
        self.sign_out_button.click()
        self.confirm_button.click()

    # While login: username and password are send as a text
    # Accept cookies and click login button
    def login_on_portal(self, username, password):
        self.tr_portal_username_input.send_keys(username)
        self.tr_portal_password_input.send_keys(password)

        self.tr_portal_accept_cookies_button.click()
        self.tr_portal_login_button.click()

    # Click the navigation button on top left corner of TR Hub home page
    # Click About: Displays Firmware version in text
    def get_firmware_display(self):
        self.navigation_drawer.click()

        self.about_button.click()

        return self.firmware_text.text

    # When running with appium, you will need to pass the usage page and snapdragon setting again
    def passthrough_with_appium(self):
        # If TR hub is launched without clearing cache, then these steps will not be necessary
        try:
            try:
                self.continue_as_guest_button.click()
            except NoSuchElementException:
                pass

            self.agree_usage_and_diagnostics()

            try:
                self.permission_button.click()
            except NoSuchElementException:
                pass

            self.driver.back()

        except NoSuchElementException:
            pass
