# Web Scraper Comment

"""
B. Coble
Web Scraping Example
05/21/2020

# Data to scrape - Laptop Information from Newegg.com
    # Item Name and Price
    # Used Right Click + Inspect to find the tags of the fields to scrape
"""



# Packages imported for web scraping
# Had to install them all for the project
# also had to upgrade pip


from selenium import webdriver # automation package; this will open our web browser for us
from webdriver_manager.chrome import ChromeDriverManager # will likely need to run pip install web-driver manager


from bs4 import BeautifulSoup # html parser package; will parse through tags in Elements section of Inspect tool
import pandas as pd # page used to read and manipulate our data


# Configuring selenium webdriver to use the Chrome Browser
# There are similar commands for other browsers if you wish to use IE, Firefox, Safari, etc.
driver = webdriver.Chrome(ChromeDriverManager().install())

# selenium will open a browser for us to the URL we provide (the newegg url for laptops)
#
products=[] #List to store name of the product
prices=[] #List to store price of the product

# the URL we want selenium webdriver to get for us

driver.get("https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptops")

