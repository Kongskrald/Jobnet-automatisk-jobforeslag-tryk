'''
	This is a script that will automatically press the jobforslag button on jobnet.
	You have to install selenium and download the correct version of chromedriver.
	If you wish to have delays between actions uncomment the time.sleep(1) parts and specify your delay.
	
	Author:
		Shagen Djanian
		16-08-2019
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Change this into your username and password
your_username = "Karen"
your_password= "Hunter2"
driver = webdriver.Chrome('chromedriver.exe') # Change this line if you wish to use a different browser
driver.get("https://job.jobnet.dk/CV/frontpage")

#assert "Python" in driver.title
user_name = driver.find_element_by_id("JobnetUsername")
user_name.clear()
user_name.send_keys(your_username)
#time.sleep(1)


user_name = driver.find_element_by_id("JobnetPassword")
user_name.clear()
user_name.send_keys(your_password)
#time.sleep(1)

login_button = driver.find_element_by_id("LoginButton")
login_button.click()
#time.sleep(1)


job_forslag_button = driver.find_element_by_id("TjobButton")
job_forslag_button.click()
#time.sleep(1)

driver.quit()

