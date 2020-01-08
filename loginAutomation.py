
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

print('Auto login initiated')


def Wait_by_id(id):
    print('Waiting for id ["{}"]'.format(id))
    for i in range(320):
        try:
            browser.find_element_by_id(id)
            return True
        except NoSuchElementException:
            time.sleep(0.5)
    else:
        print('Id ["{}"] not found'.format(id))
        return False

def waitForClockIn():
    print('waiting for web clock-in button');
    for i in range(320):
        try:
            browser.find_element_by_css_selector('input[value="Web Clock-In"]')
            return True
        except NoSuchElementException:
            time.sleep(0.5)
    else:
        print("Element not found")
        return False

# Read credentials from file
print('Reading credentials..')
try:
    file = open("credentials.txt",'r')
except:
    print('Some problem with file reading\nTerminating...')
    sys.exit()

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
print('Completed..')
file.close()

# Open a new firefox window

firefoxProfile = wd.FirefoxProfile()
firefoxProfile.set_preference("geo.enabled", True)
firefoxProfile.set_preference("geo.provider.use_corelocation",True)
firefoxProfile.set_preference("geo.prompt.testing",True)
firefoxProfile.set_preference("geo.prompt.testing.allow",True)
firefoxProfile.set_preference("browser.link.open_newwindow.restriction", 0)

print('Opening a new browser window')
try:
    browser = wd.Firefox(firefox_profile = firefoxProfile)
except:
    print('Error in opening the browser window.\nTerminating...')
    sys.exit()
# main_window = browser.current_window_handle

# Open web login url
print('Opening local login url')
browser.get(net_url)
while True:
    if not Wait_by_id('loginbutton'):
        browser.quit()
        sys.exit()
    else:
        break

#check if Local is already logged in
button = browser.find_element_by_id('loginbutton')

if button.text == 'Login':
    print('Not already logged in.\nTrying to login')
    user = browser.find_element_by_name('username')
    passwd = browser.find_element_by_name('password')
    user.send_keys(luname)
    passwd.send_keys(lpass)
    passwd.send_keys(Keys.ENTER)
    i = 0
    while i < 320:
        button = browser.find_element_by_id('loginbutton')
        if button.text == 'Logout':
            print('Local login Successful')
            break
        i+=1
        time.sleep(.2)
    else:
        print('Local login failed.\nExiting..')
        browser.quit()
        sys.exit()
else:
    print('Already logged in')

time.sleep(2)
# browser.execute_script("window.open('{}')".format(keka_url))
print('Opening Keka login url')
browser.get(keka_url)

while browser.current_url != keka_url:
    if browser.current_url == keka_post_login_url:
        print('Already Logged')
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
            print('Unable to login...\nExiting..')
            browser.quit()
            sys.exit()
    time.sleep(.2)

# get a reference to webclockin button and click
# Check if web clock in Successful

if(waitForClockIn()):
    browser.find_element_by_css_selector("input[value='Web Clock-In']").click()
else:
    browser.quit()
