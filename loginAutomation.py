
keka_url = 'http://sayone.keka.com'
net_url = 'https://172.16.16.16:8090/httpclient.html'

import time

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class is_logged_in_id(object):
    def __init__(self,locator):
        self.locator = locator

    def __call__(self,driver):
        try:
            elem = driver.find_element_by_id(*self.locator)
            return elem
        except:
            return False
# # Read credentials from file
# try:
#     file = open("credentials.txt",'r')
# except:
#     print('Some problem with file reading')
#     error = 1
#
# file.readline()
# line = file.readline()
# luname = line.strip().split(' ')[-1]
# line = file.readline()
# lpass = line.strip().split(' ')[-1]
# file.readline()
# line = file.readline()
# kuname = line.strip().split(' ')[-1]
# line = file.readline()
# kpass = line.strip().split(' ')[-1]
#
# # Open a new firefox window
browser = wd.Firefox()
#
# # Open web login url
# browser.get(net_url)
#
# #check if Local is already logged in
#
#
# user = browser.find_element_by_name('username')
# passwd = browser.find_element_by_name('password')
# user.send_keys(luname)
# passwd.send_keys(lpass)
# passwd.send_keys(Keys.ENTER)
#
# i = 0
# while i < 15:
#     #check if login is okay
#     time.sleep(0.2)
#     i+=1
# else:
#     print('Local Login Failed')
#     browser.quit()
#
# ac(browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
browser.get(keka_url)

#check if keka is already loged in
try:
    elem = browser.find_element_by_id('userProfile')
    print(elem)
except NoSuchElementException:
    print('No loged in!\nTrying to login to keka')
    browser.find_element_by_id('email').send_keys('nipun@sayonetech.com')
    browser.find_element_by_id('password').send_keys('Napster@123')
    ac(browser).send_keys(Keys.ENTER).perform()

time.sleep(10)
elem = browser.find_element_by_id('logoutForm')
print(elem)

# when logged in for first time check for logoutform
# If user is already logged in, must check for logoutform and userProfile
# Need to find a way to check if two elements is present, at the same time.

# element = wc(browser, 20).until(
#         is_logged_in_id("userProfile")
#     )
# print(element)

# try:
#     element = wc(browser, 10).until(
#         ec.is_logged_in_id((By.ID, "userProfile"))
#     )
# except:
#     print('Keka Login Failed')
# finally:
#     browser.quit()


#
# browser.find_element_by_id('email').send_keys(kuname)
# browser.find_element_by_id('password').send_keys(kpass)
# ac(browser).send_keys(Keys.ENTER).perform()
#
# i = 0
#
# while i < 15:
#     #check if login is okay
#     time.sleep(0.2)
#     i+=1
# else:
#     print('Keka Login Failed')
#     browser.quit()

# goto attendence page and activate webclockin
