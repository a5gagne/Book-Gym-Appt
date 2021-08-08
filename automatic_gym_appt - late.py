# 1. open browser
# 2. login   
    # -open login screen
    # -enter credentials
# 3. find appt time
# 4. book


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# open browser
driver = webdriver.Chrome(r"C:\Users\aigag\Documents\Python Projects\chromedriver.exe")
driver.get("https://www.goodlifefitness.com/home.html")
driver.maximize_window()

wait = WebDriverWait(driver, 15)
login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "c-header__login-text")))
login.click()

loginemail = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "c-field__input.js-login-email.c-login-block__input")))
loginpass = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "c-field__input.js-login-password.c-login-block__input")))
loginemail.send_keys('aigagne01@gmail.com')
loginpass.send_keys('Alx-g343')
send = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "c-form__button-group")))
send.click()

time.sleep(10)

driver.get('https://www.goodlifefitness.com/book-workout.html#no-redirect')

date = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"col.tablink.js-class-weekday")))
date = driver.find_elements_by_class_name("col.tablink.js-class-weekday")[6]
date.click()


time.sleep(10)
time_range = "7:45 pm - 8:45 pm"
category = "Co-ed"

timeslot = driver.find_element_by_xpath("//div[@id='day-number-7']/li[descendant::text()='{}' and descendant::span[text()='{}'] and descendant::span[text()='{}']]".format(time_range.split(' - ')[0],time_range.split(' - ')[1], category))
driver.execute_script("arguments[0].scrollIntoView();", timeslot)
timeslot.click()

book = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"c-btn-cta.c-btn-cta--chevron.modal-class-action")))
book.click()

time.sleep(5)
agree = driver.find_element_by_id('js-workout-booking-agreement-input')
agree.click()

confirm = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"c-btn-cta.c-btn-cta--chevron.modal-class-action.js-terms-agreement-cta")))
confirm.click()


time.sleep(5)
driver.close()