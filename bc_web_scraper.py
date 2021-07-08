"""
# Data to scrape - data from python.org
"""
# import statements
from selenium import webdriver  # automation package; this will open our web browser for us
import configparser
from bs4 import BeautifulSoup  # html parser package; will parse through tags in Elements section of Inspect tool
import pandas as pd  # page used to read and manipulate our data

# creating a config variable that will read from config file can store variables here for something more secure than
# hard coding also limits changes to only the config file and reduces changes to source code if variable info needs
# to be added or changed main function in this file is ran by calling the main function from the caller.py file; uses
# logger created in the main function of that file; logger is created once and reused throughout the whole program

config = configparser.ConfigParser()
config.read('./config.ini')

# creating firefox driver var for selenium webdriver to use the Firefox geckodriver to open a firefox browser
# automatically

f_driver = webdriver.firefox.webdriver.WebDriver(executable_path=config['Firefox']['exe_file'])

# creating chrome driver var for selenium webdriver to use the Chrome chromedriver to open a chrome browser
# automatically
c_driver = webdriver.chrome.webdriver.WebDriver(executable_path=config['Chrome']['exe_file'])

# functions created

def openFirefox(logger):
    logger.info(f'Open a firefox browser and go to python.org')
    f_driver.get("http://www.python.org")
    assert "Python" in f_driver.title
    logger.info(f'Firefox opened python.org successfully.')


def openChrome(logger):
    logger.info(f'Open a chrome browser and go to python.org')
    c_driver.get("http://www.python.org")
    assert "Python" in c_driver.title
    logger.info(f'Chrome opened python.org successfully.')


def main(logger):
    try:
        logger.info(f'Opening Firefox page...')
        openFirefox(logger)
        logger.info(f'Opening Firefox complete.')

        logger.info(f'Opening Chrome page...')
        openChrome(logger)
        logger.info(f'Opening Chrome complete.')

    except Exception as e:
        logger.error(f'Issue opening python.org in browser.')
        logger.error(f'Please see exception raised: \n{e}')  # will write exception and stack in log on new line
        raise e  # raise exception to stop program

# web scraping
products = []  # List to store scrapped data later
