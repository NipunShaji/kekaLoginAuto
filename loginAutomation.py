
keka_url = 'http://sayone.keka.com'
net_url = 'https://172.16.16.16:8090/httpclient.html'

try:
    from selenium import webdriver as wd
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains as ac
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait as wc
    from selenium.webdriver.support import expected_conditions as ec
except:
    print('No selenium Module found.')
    print('Please install it and retry.')

browser = wd.Firefox()

browser.get(net_url)
user = browser.find_element_by_name('username')
passwd = browser.find_element_by_name('password')
user.send_keys('nipun_sayone')
passwd.send_keys('Napster@123')
passwd.send_keys(Keys.ENTER)
try:
    element = wc(browser, 20).until(
        ec.visibility_of_element_located((By.TAG_NAME,'xmp'))
    )
finally:
    browser.quit()
ac(browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
browser.get(keka_url)
browser.find_element_by_id('email').send_keys('nipun@sayonetech.com')
browser.find_element_by_id('password').send_keys('Napster@123')
ac(browser).send_keys(Keys.ENTER).perform()
