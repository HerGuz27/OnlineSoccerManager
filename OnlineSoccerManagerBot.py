from selenium import webdriver
import os
import time

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)


def login(user,password):
    driver.get('https://en.onlinesoccermanager.com')
    time.sleep(5)
    driver.find_element('css selector', '.btn-new').click()
    time.sleep(5)
    driver.find_element('css selector', '.btn-alternative').click()
    time.sleep(5)
    driver.find_element("css selector",'#manager-name').send_keys(user)
    driver.find_element("css selector",'#password').send_keys(password)
    driver.find_element("css selector",'#login').click()
    time.sleep(15)

def getBusinessTokens():
    print('Negocios')
    time.sleep(5)
    driver.find_element('css selector', 'li.dropdown:nth-child(3) > a:nth-child(1)').click()
    time.sleep(5)
    driver.find_element('css selector', 'div.product-free:nth-child(2)').click()
    time.sleep(5)
    for i in range(3):
       driver.find_element('css selector', 'div.product-free:nth-child(1)').click()
       time.sleep(30)
    print('finish')

user=os.environ['USER']
password=os.environ['PASSWORD']
print(user,password)
login(user,password)
getBusinessTokens()
