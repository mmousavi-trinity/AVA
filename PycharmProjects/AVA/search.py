import sys
import time
import pyautogui
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



def googleSearch(string):

    ##Opens chrome browser using selenium module and searches

    chrome_driver_binary = r"/Applications/Python 3.6/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary)

    options = webdriver.ChromeOptions()
    options.binary_location = r"/Applications/Google Chrome.app"
    driver.get('https://google.com')
    time.sleep(3)
    search = driver.find_element_by_name('q')
    search.send_keys(string)
    time.sleep(2)
    search.submit()
    time.sleep(2)
    sys.exit(0)

##chrome()

def goToSite(string):

    ##Opens chrome browser using selenium module and searches

    chrome_driver_binary = r"/Applications/Python 3.6/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary)

    options = webdriver.ChromeOptions()
    options.binary_location = r"/Applications/Google Chrome.app"
    driver.get(string)
    time.sleep(5)
    sys.exit(0)

