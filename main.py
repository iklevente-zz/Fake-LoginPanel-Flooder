from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from time import sleep


tries = 1

while (tries < 10000): # Set 10000 to how many times you want to spam the stealer site with fake passwords.
	
	print tries

	usernameStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) # Generate random uppercase username
	passwordStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) # Generate random uppercase password

	print "Current generated password is: " + usernameStr
	print "Current generated password is: " + passwordStr

	# Chose your chromedriver path. I was using Linux and I downloaded it from https://chromedriver.chromium.org/downloads. Download the one wich matches your chrome/chromium version. You can check your chromium version on html5test.com
	browser = webdriver.Chrome("/bin/chromedriver") 
	browser.get(('https://casenorm.fun/auth')) # Login panel's URL address

	username = browser.find_element_by_id('steamAccountName') # Username textbox on login site. (Right click in username textbox --> Inspect element --> search for id="something")
	username.send_keys(usernameStr) 

	username = browser.find_element_by_id('steamPassword') # Password textbox on login site. (Right click in password textbox --> Inspect element --> search for id="something")
	username.send_keys(passwordStr)

	loginButton = browser.find_element_by_id('SteamLogin') # Login button on login site. (Right click on login button --> Inspect element --> search for id="something")
	loginButton.click()
	sleep(2)
	browser.close()
	tries = tries + 1
