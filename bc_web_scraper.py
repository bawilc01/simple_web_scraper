"""
# Data to scrape - data from python.org
"""
# import statements
from selenium import webdriver  # automation package; this will open our web browser for us
import configparser
from bs4 import BeautifulSoup  # html parser package; will parse through tags in Elements section of Inspect tool
import pandas as pd  # page used to read and manipulate our data
import requests
import csv

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
# c_driver = webdriver.chrome.webdriver.WebDriver(executable_path=config['Chrome']['exe_file'])

# functions created

def openFirefox(logger):
    # browser automation: opening a browser for python.org
    logger.info(f'Open a firefox browser and go to python.org')

    # wait five seconds
    f_driver.implicitly_wait(5000)

    # maximize with maximize_window()
    f_driver.maximize_window()

    f_driver.get("http://www.python.org")
    assert "Python" in f_driver.title

    logger.info(f'Geckodriver opened python.org in firefox successfully.')
    logger.info(f'Geckodriver going to jobs page on python.org...')

    f_driver.implicitly_wait(5000)

    # scroll down (X, Y)
    # Y is the height (on a fullhd monitor it's 1080)
    # f_driver.execute_script("window.scrollTo(0, 1080)")

    # find and navigate to the jobs link
    l = f_driver.find_element_by_link_text("jobs.python.org")

    # click the page
    l.click()

    logger.info(f'Geckodriver navigated to python.org jobs page in firefox successfully.')

    logger.info(f'minimizing window')
    f_driver.implicitly_wait(100000)

    # minimize window
    f_driver.minimize_window()

    # print the page raw html to scrape using requests package; log html to console on new line
    URL = "https://www.python.org/jobs/"
    r = requests.get(URL)

    # use beautiful soup package
    #     r.content : It is the raw HTML content.
    #     html5lib : Specifying the HTML parser we want to use.

    soup = BeautifulSoup(r.content, 'html5lib')

    # array to store python.org jobs; will be scraped from website
    python_jobs = []

    # use inspect too on firefox page that opened to find the downloads area in the doc tree

    jobs = soup.find_all('section', attrs={'class': 'main-content with-right-sidebar', 'role': 'main'})
    # logger.info(jobs.prettify())  # jobs in html on python.org/jobs to be parsed and scraped
    for job in jobs:
        company_element = job.find('a')
        location_element = job.find('span', attrs={'class': 'listing-location'})

        logger.info(f'\nJob Title: {company_element.text.strip()}, \nLocation: {location_element.text.strip()}')

    # write to csv

    filename = 'python_jobs.csv'

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        #csvwriter.writerow('Job Title', 'Company Name')

        # writing the data rows
        csvwriter.writerows(job)

    logger.info(f'Closing firefox.')
    f_driver.quit()


# def openChrome(logger):
#     logger.info(f'Open a chrome browser and go to python.org')
#     c_driver.get("http://www.python.org")
#     assert "Python" in c_driver.title
#     logger.info(f'Chrome opened python.org successfully.')


def runner(logger):
    try:
        logger.info(f'Opening Firefox page...')
        openFirefox(logger)

    except Exception as e:
        logger.error(f'Issue opening python.org in firefox browser.')
        logger.error(f'Please see exception raised: \n{e}')  # will write exception and stack in log on new line
        raise e  # raise exception to stop program

    # try:
    #     logger.info(f'Opening Chrome page...')
    #     openChrome(logger)
    #     logger.info(f'Opening Chrome complete.')
    #
    # except Exception as e:
    #     logger.error(f'Issue opening python.org in chrome browser.')
    #     logger.error(f'Please see exception raised: \n{e}')  # will write exception and stack in log on new line
    #     raise e  # raise exception to stop program
