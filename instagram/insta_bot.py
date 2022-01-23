from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')
browser.implicitly_wait(5)

browser.find_element(by=By.NAME, value='username').send_keys('<username here>')
browser.find_element(by=By.NAME, value='password').send_keys('<password here>')
login_element = browser.find_element(by=By.XPATH, value='//button[@type=\'submit\']')
sleep(5)
login_element.click()
browser.implicitly_wait(5)
try:
    dont_save_login_info_button = browser.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/div/div/div/button')
    dont_save_login_info_button.click()

    dialog_box = browser.find_element(by=By.XPATH, value='/html/body/div[4]/div')

    dont_turn_on_notifications_button = dialog_box.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[3]/button[2]')
    dont_turn_on_notifications_button.click()
except:
    print('Error')