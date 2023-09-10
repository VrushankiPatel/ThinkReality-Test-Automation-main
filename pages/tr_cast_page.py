from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class TRCastPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "com.lenovo.xr.trcast", ".ui.activity.LauncherActivity")

    # Cloud stream radio button in the inital setup of TR CAST
    @property
    def cloud_stream_radio_button(self):
        return self.driver.find_element(AppiumBy.ID, value="com.lenovo.xr.trcast:id/cloud_streaming_pref")

    # 'Continue button' after user click cloud stream (appears when select cloud stream for first time)
    @property
    def continue_button(self):
        return self.driver.find_element(AppiumBy.ID, value="com.lenovo.xr.trcast:id/continue_button")

    # 'START STREAM' button to start the TR CAST
    @property
    def start_stream_button(self):
        return self.driver.find_element(AppiumBy.ID, value="com.lenovo.xr.trcast:id/start_stream")

    # 'STOP STREAM' button to stop the TR CAST streaming
    @property
    def stop_stream_button(self):
        return self.driver.find_element(AppiumBy.ID, value="com.lenovo.xr.trcast:id/stop_stream")

    # 'Screenshot' button to capture the TR CAST before streaming (Cannot take screenshot on phone during streaming)
    @property
    def screen_shot_button(self):
        return self.driver.find_element(AppiumBy.ID, value="com.lenovo.xr.trcast:id/screenshot")

    # The pincode displayed on TR CAST
    @property
    def pin_code(self):
        return self.driver.find_element(AppiumBy.ID, value="com.lenovo.xr.trcast:id/txt_pin_value").text
