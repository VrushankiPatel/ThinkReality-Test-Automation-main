# Abbreviations
# cp: Cloud Portal

import pytest
import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from getgauge.python import step
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from pages.tr_cast_stream_page import TRCastStreamPage

class TRCastStreamTest():
    @step("Launch Cloud Portal")
    def init(self):
        # Initialize Selenium Web Driver
        driver_stream = webdriver.Chrome()
        
        # Implicitly wait for N seconds if the element is not present
        driver_stream.implicitly_wait(3)
        
        driver_stream.get()
        
        self.trcast_stream_page = TRCastStreamPage(driver_stream)
        
    @step('ThinkReality Portal Login: username')
    def cp_login_username(self):
        self.trcast_stream_page.login_portal_username().send_keys("Enter your username")
        
    @step('ThinkReality Portal Login: password')
    def cp_login_password(self):
        self.trcast_stream_page.login_portal_password().send_keys("Enter your password")
    
    @step("Log In button")
    def cp_LogIn(self):
        self.trcast_stream_page.log_in_button().click()
        
    @step("Device Manager: Column on left")
    def cp_device_manager(self):
        self.trcast_stream_page.device_manager_column().click()
    
    @step("Devices: submenu: Device Manager -> Devices")
    def cp_submenu_device(self):
        self.trcast_stream_page.devices().click()
        
    # @step("Search bar for device search")
    # def cp_device_search_bar(self):
    #     self.trcast_stream_page.search_bar().click()
        
    @step("Insert serial number of the device in search bar")
    def cp_serial_no_search_bar(self):
        self.trcast_stream_page.serial_number().click()
        self.trcast_stream_page.serial_number().send_keys("Search")
        self.trcast_stream_page.serial_number().send_keys(Keys.ENTER)

    @step("Selecting the device in the first row of search")
    def cp_select_device(self):
        self.trcast_stream_page.select_appeared_device().click()
    
    @step("User can view the stream on the cloud portal with cloud streaming")
    def cp_join_stream(self):
        self.trcast_stream_page.join_stream().click()
        
    @step("Entering the pin code to join the stream")
    def cp_pin_code(self):
        for i in range(6):
            self.trcast_stream_page.pin_code(i).send_keys()
        
    @step("Join stream button to continue")
    def cp_join_stream_button(self):
        self.trcast_stream_page.join_stream_button().click()
        
    @step("User can take a picture on the cloud portal")
    def cp_screenshot(self):
        self.trcast_stream_page.screenshot_button().click()
        # the screenshot is been downloaded and can be seen in the downloads folder of the device
        
    @step("User can pause the stream on the cloud portal")
    def cp_pause_stream(self):
        self.trcast_stream_page.pause_stream().click()
        
    @step("User can play the stream on the cloud portal")
    def cp_play_stream(self):
        self.trcast_stream_page.play_stream().click()
        
    @step("User can close the stream on the cloud portal")
    def cp_close_stream(self):
        self.trcast_stream_page.close_stream().click()