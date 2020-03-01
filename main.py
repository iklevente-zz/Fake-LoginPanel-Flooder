from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from time import sleep


tries = 1

while (tries < 10000):
	
	print tries

	usernameStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
	passwordStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

	print "Current generated password is: " + usernameStr
	print "Current generated password is: " + passwordStr

	browser = webdriver.Chrome("/bin/chromedriver")
	browser.get(('https://casenorm.fun/'))
	browser.get(('https://casenorm.fun/auth'))

	username = browser.find_element_by_id('steamAccountName')
	username.send_keys(usernameStr)

	username = browser.find_element_by_id('steamPassword')
	username.send_keys(passwordStr)

	loginButton = browser.find_element_by_id('SteamLogin')
	loginButton.click()
	sleep(2)
	browser.close()
	tries = tries + 1
