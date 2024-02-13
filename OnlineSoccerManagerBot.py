from selenium import webdriver
import os
import time

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)


def login(user,password):

    #Open 'https://en.onlinesoccermanager.com' in firefox
    driver.get('https://en.onlinesoccermanager.com')
    time.sleep(5)

    #Click in accept button
    driver.find_element('css selector', '.btn-new').click()
    time.sleep(5)

    #Click in the login button
    driver.find_element('css selector', '.btn-alternative').click()
    time.sleep(5)

    #Enter the user name
    driver.find_element("css selector",'#manager-name').send_keys(user)

    #Enter the password
    driver.find_element("css selector",'#password').send_keys(password)

    #Click in the login button
    driver.find_element("css selector",'#login').click()
    time.sleep(15)

def get_business_tokens():
    time.sleep(5)
    driver.find_element('css selector', 'li.dropdown:nth-child(3) > a:nth-child(1)').click()
    time.sleep(5)
    driver.find_element('css selector', 'div.product-free:nth-child(2)').click()
    time.sleep(5)
    for i in range(3):
       driver.find_element('css selector', 'div.product-free:nth-child(1)').click()
       time.sleep(30)
    print('finish')


# User and Paswword set with env variables
user=os.environ['USER']
password=os.environ['PASSWORD']

#Execute login function
login(user,password)

#Execute get
get_business_tokens()
