from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
username='XYZ3@gmail.com'
password='asdfg'
browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Drm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession'))
username = browser.find_element_by_id('Email')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('next')
nextButton.click()
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys(passwordStr)
 
signInButton = browser.find_element_by_id('signIn')
signInButton.click()

