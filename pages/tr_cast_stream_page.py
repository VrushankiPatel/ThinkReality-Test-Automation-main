from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class TRCastStreamPage():
    def __init__(self, driver):
        self.driver = driver

    # Cloud Portal Login: username, locate by ID
    @property
    def login_portal_username(self):
        return self.driver.find_element(By.ID, "username")

    # Cloud Portal Login: password, locate by ID
    @property
    def login_portal_password(self):
        return self.driver.find_element(By.ID, "password")

    # Log in button, locate by NAME
    @property
    def log_in_button(self):
        return self.driver.find_element(By.NAME, "login")

    # Select device manager from the column on left by CSS_SELECTOR
    @property
    def device_manager_column(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .menu-item .menu-item__text")

    # Select the submenu of device manager i.e devices, by CSS_SELECTOR
    @property
    def devices(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".expand .submenu-item:nth-child(2) .submenu-item__link-text")

   
    # Locate the search bar by CLASS_NAME
    # Enter serial number in search bar to look for the device
    # Apply SEND.KEYS to search the device with the entered serial number
    @property
    def device_search_bar(self):
        return self.driver.find_element(By.CLASS_NAME, "search-input")

    # Find the first device appeared after entering serial number in the search bar
    @property
    def select_appeared_device(self):
        return self.driver.find_element(By.CLASS_NAME, "pill")

    # Once the device informtion is opened and if the device seems online, click on the JOIN STREAM button
    @property
    def join_stream(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".tick-btn > .btn__label")

    # Pop up pincode window -> Will receive the pin code from Moto phone (present in the TR cast)
    @property
    def pin_code_input(self):
        return [self.driver.find_element(By.ID, i) for i in range(6)]


    # After entering the pincode, click the 'JOIN STREAM' button to join the TR cast on cloud portal
    @property
    def join_stream_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn--primary > .btn__label")

    # The 'camera' icon on the stream page to capture the screenshot
    @property
    def screenshot_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".video-player__actions-btn:nth-child(1) svg")

    # The 'pause' button to pause the cloud stream
    @property
    def pause_stream_button(self):
        return self.driver.find_element(By.ID, "Pause_outlined_white")

    # The 'resume' button to resume the cloud stream
    @property
    def resume_stream_button(self):
        return self.driver.find_element(By.ID, "Play_outlined__white")

    # The 'close' button on the top right corner to close the stream on portal
    @property
    def close_stream_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn-icon .icon--sm path")

    def input_pin_code(self, pin_code):
        for i, item in enumerate(self.pin_code_input):
            item.send_keys(pin_code[i])

    def refresh_page(self):
        self.driver.refresh()

    # User cannot re-join the stream once close the stream on the cloud portal
    # User needs to repeat the steps of finding device -> Click Join Stream Button -> Enter pin code -> Stream visible
