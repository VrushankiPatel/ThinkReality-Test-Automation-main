
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOlin1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_olin1(self):
    # link entered
    self.driver.get("https://portal-platform.naea1.uds.lenovo.com/a3r6candidatese2ei/portal/think-reality/devices")
    # window size set for recording
    self.driver.set_window_size(1280, 672)
    # click for inserting
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"main-page-search\"]").click()
    # insert serial number to detect the device
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"main-page-search\"]").send_keys("0180")
    # click ENTER to search for the device of given serial number
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"main-page-search\"]").send_keys(Keys.ENTER)
    # click to open the device that appears in first row
    self.driver.find_element(By.CSS_SELECTOR, ".null > .ng-star-inserted:nth-child(5)").click()
    # click to join stream
    self.driver.find_element(By.CSS_SELECTOR, ".stream__action > .btn").click()
    # enter the PIN from Moto to join the stream from cloud portal
    self.driver.find_element(By.ID, "0").send_keys("4")
    self.driver.find_element(By.ID, "1").send_keys("1")
    self.driver.find_element(By.ID, "2").send_keys("5")
    self.driver.find_element(By.ID, "3").send_keys("9")
    self.driver.find_element(By.ID, "4").send_keys("7")
    self.driver.find_element(By.ID, "5").send_keys("4")
    # click to enter the stream on cloud portal
    self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn--primary").click()
    # click and hold to drag the window
    element = self.driver.find_element(By.CSS_SELECTOR, ".modal__header")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".modal__header")
    # click and release to perform the picture taking action
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".modal__header")
    # move to picture btn -> click -> release -> perform action
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".modal__header").click()
    self.driver.find_element(By.CSS_SELECTOR, ".video-player__actions-btn:nth-child(1) svg").click()
    # click pause btn to pause the cloud stream for a while
    self.driver.find_element(By.ID, "Pause_outlined_white").click()
    # click play btn to play back the paused cloud stream
    self.driver.find_element(By.ID, "Play_outlined__white").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".video-player__video--top")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".video-player__video--top")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".video-player__video--top")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".video-player__video--top").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-icon .icon--sm > svg").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-link__label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".tray-overlay").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-icon--remove svg").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"main-page-search\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"main-page-search\"]").send_keys("0180")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"main-page-search\"]").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(4) > .ng-star-inserted > .ng-star-inserted .cell-name__value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".tick-btn > .btn__label").click()
    self.driver.find_element(By.ID, "0").send_keys("4")
    self.driver.find_element(By.ID, "1").send_keys("1")
    self.driver.find_element(By.ID, "2").send_keys("5")
    self.driver.find_element(By.ID, "3").send_keys("9")
    self.driver.find_element(By.ID, "4").send_keys("7")
    self.driver.find_element(By.ID, "5").send_keys("4")
    self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn--primary > .btn__label").click()
