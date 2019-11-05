
keka_url = 'http://sayone.keka.com'
net_url = 'https://172.16.16.16:8090/httpclient.html'

import time

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wc
from selenium.webdriver.support import expected_conditions as ec


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

browser = webdriver.Firefox()

browser.get(net_url)

#check if Local is already logged in

user = browser.find_element_by_name('username')
passwd = browser.find_element_by_name('password')
user.send_keys(luname)
passwd.send_keys(lpass)
passwd.send_keys(Keys.ENTER)

i = 0

while i < 15:
    #check if login is okay
    time.sleep(0.2)
    i+=1
else:
    print('Local Login Failed')
    browser.quit()

ac(browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
browser.get(keka_url)

#check if keka is already loged in

browser.find_element_by_id('email').send_keys(kuname)
browser.find_element_by_id('password').send_keys(kpass)
ac(browser).send_keys(Keys.ENTER).perform()

i = 0

while i < 15:
    #check if login is okay
    time.sleep(0.2)
    i+=1
else:
    print('Keka Login Failed')
    browser.quit()
