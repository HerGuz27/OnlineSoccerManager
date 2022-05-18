from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
import time

service = FirefoxService(executable_path=GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)

def login(user,password):
    driver.get('https://en.onlinesoccermanager.com/Dashboard')
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[3]/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[4]/div[2]/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="manager-name"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="login"]').click()
    time.sleep(15)

driver.get('https://en.onlinesoccermanager.com/BusinessClub')
time.sleep(20)
for j in range (3):
    driver.find_element_by_xpath('/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div/div[1]/div').click()
    time.sleep(70)
