from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os


class OnlineSoccerManagerService:

    # instantiante env variables and webdriver
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)
        self.user = os.environ['USER']
        self.password = os.environ['PASSWORD']

    def login(self, user, password):

        try:

            # Open 'https://en.onlinesoccermanager.com' in firefox
            self.driver.get('https://en.onlinesoccermanager.com')
            time.sleep(5)

            # Click in accept button
            self.driver.find_element('css selector', '.btn-new').click()
            time.sleep(5)

            # Click in the login button
            self.driver.find_element('css selector', '.btn-alternative').click()
            time.sleep(5)

            # Enter the user name
            self.driver.find_element("css selector", '#manager-name').send_keys(user)

            # Enter the password
            self.driver.find_element("css selector", '#password').send_keys(password)

            # Click in the login button
            self.driver.find_element("css selector", '#login').click()
            time.sleep(15)
            print('Login successfuly')
        except:
            print('Login failed')

    def get_business_tokens(self):

        # call the login function
        self.login( self.user, self.password )

        time.sleep(5)

        # go to the buissnes page in game
        self.driver.find_element('css selector', 'li.dropdown:nth-child(3) > a:nth-child(1)').click()
        time.sleep(5)
        self.driver.find_element('css selector', 'div.product-free:nth-child(2)').click()
        time.sleep(5)

        #array to get the four coins
        for i in range(3):
            self.driver.find_element('css selector', 'div.product-free:nth-child(1)').click()
            time.sleep(30)

        for j in range (3):
            self.driver.find_element('css selector', 'div.product-free:nth-child(1)')
            time.sleep(30)
        print('finish')

        self.close_browser()

    def close_browser(self):
        # Close the browser
        self.driver.quit()