from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import USERNAME,PASSWORD
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("https://www.instagram.com/accounts/login/")
driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)
driver.find_element_by_tag_name('button').click()
try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Profile')))
	print("LOGGED IN")
finally:
	driver.quit()