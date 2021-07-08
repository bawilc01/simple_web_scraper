import logging


# todo these make great todo comments as reminders

# this file is a 'caller' file that calls the other files. it has the logging set up in this file's main function and
# the logger here can be reused for the other files since they are being called by this file's "main' file and it
# will recognize logger. just set logger as a param in other file's functions or classes and set it to something in
# the function, like a logger.info

def main(logger):

    try:
        import bc_web_scraper
        logger.info(f'Running webscraper py file main function.')
        bc_web_scraper.runner(logger)
    except Exception as e:
        logger.error(f'Error running main function in webscraper py file.')
        raise e

if __name__ == '__main__':
    # setting up custom loggin in the console

    logger = logging.getLogger(f'Webscraper Logger')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    strhndlr = logging.StreamHandler()
    strhndlr.setFormatter(formatter)
    logger.addHandler(strhndlr)

    logger.info(
        f'------------------------------------process with caller started--------------------------------------')

    main(logger)

    logger.info(f'------------------------------------process with caller ended--------------------------------------')