# Web Scraping Example

This is an example web scraping project. It will scrape data from a given webpage and log
it for analysis.

Uses logging package that comes with python to log messages. Logger created in caller file and is reused for logging in other py files.
Logging documentation: https://docs.python.org/3/howto/logging.html


Requirements:

Install python 3.9 or higher.
Install pip for python: _python get-pip.py_ in the terminal.
If pip is already installed, check that pip is up to date with:  _pip install --upgrade pip_

Check your browser version and then go to these sites to download the webdriver
for your browser version. Download the executable for your machine and update the binary path for each 
browser. I am on Chrome version 91, for example, so I need the chromedriver exe
that works for Chrome version 91:

Firefox: https://github.com/mozilla/geckodriver/releases

Chrome: https://chromedriver.chromium.org/downloads

Follow this youtube video to set your binary path for the WebDriver. This is for the Chrome chromedriver but 
the same thing can be done for the Firefox geckodriver:
https://www.youtube.com/watch?v=qeddFX5HXis

Webscraping with Beautiful Soup:

https://realpython.com/beautiful-soup-web-scraper-python/
https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/


Will also need to run 
_pip install -r requirements.txt_ in the terminal to install the packages used in the project. 
