
keka_url = 'https://sayone.keka.com/'
keka_post_login_url = 'https://sayone.keka.com/#/home'
net_url = 'https://172.16.16.16:8090'

import time
import sys

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


def Wait_by_id(id):
    for i in range(320):
        time.sleep(.5)
        try:
            browser.find_element_by_id(id)
            return True
        except NoSuchElementException:
            pass
    else:
        return False

# Read credentials from file
try:
    file = open("credentials.txt",'r')
except:
    print('Some problem with file reading')
    error = 1

file.readline()
line = file.readline()
luname = line.strip().split(' ')[-1]
line = file.readline()
lpass = line.strip().split(' ')[-1]
file.readline()
line = file.readline()
kuname = line.strip().split(' ')[-1]
line = file.readline()
kpass = line.strip().split(' ')[-1]

file.close()

# Open a new firefox window
browser = wd.Firefox()
# main_window = browser.current_window_handle

# Open web login url
browser.get(net_url)
while True:
    if not Wait_by_id('loginbutton'):
        print('Local login page didn\'t load properly.\nExitting..')
        browser.quit()
        sys.exit()
    else:
        break

#check if Local is already logged in
button = browser.find_element_by_id('loginbutton')

if button.text == 'Login':
    user = browser.find_element_by_name('username')
    passwd = browser.find_element_by_name('password')
    user.send_keys(luname)
    passwd.send_keys(lpass)
    passwd.send_keys(Keys.ENTER)
    i = 0
    while i < 320:
        button = browser.find_element_by_id('loginbutton')
        if button.text == 'Logout':
            break
        i+=1
        time.sleep(.2)
    else:
        print('Local login failed.\nExiting..\n')
        browser.quit()
        sys.exit()

time.sleep(2)
browser.execute_script("window.open('{}')".format(keka_url))

# browser.get(keka_url)
while browser.current_url != keka_url:
    if browser.current_url == keka_post_login_url:
        print('Already Logged.\n')
        break
    else:
        print('Not logged in!\nTrying to login to keka')
        if Wait_by_id('email'):
            browser.find_element_by_id('email').send_keys(kuname)
            browser.find_element_by_id('password').send_keys(kpass)
            ac(browser).send_keys(Keys.ENTER).perform()
        else:
            print('Page didn\'t load properly.\nExitting..')
            browser.quit()
            sys.exit()
        if Wait_by_id('top-nav'):
            print('Logged in')
            break
        else:
            print('Unable to login...\nExiting..\n')
            browser.quit()
            sys.exit()
    time.sleep(.2)
