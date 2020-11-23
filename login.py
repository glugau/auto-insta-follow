from time import sleep
from selenium import webdriver

def login(user_username, user_pwd, browser):
    browser.implicitly_wait(5)

    browser.get("https://www.instagram.com/")

    sleep(3)
    try:
        cookies_button = browser.find_element_by_xpath("//button[text()='Accept']")  # accepts cookies
        cookies_button.click()
    except:
        pass

    username_input = browser.find_element_by_css_selector("input[name='username']")
    pwd_input = browser.find_element_by_css_selector("input[name='password']")

    username_input.send_keys(user_username)
    pwd_input.send_keys(user_pwd)

    submit_button = browser.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()

    sleep(3)