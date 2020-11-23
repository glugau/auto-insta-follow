from time import sleep
from selenium import webdriver
from login import login

def unfollow(user_username, user_pwd, iterations):
    browser = webdriver.Chrome("./chromedriver.exe")
    login(user_username, user_pwd, browser)
    browser.get("https://www.instagram.com/" + user_username + "")
    sleep(2)
    following_button = browser.find_element_by_xpath("//a[@href='/" + user_username + "/following/']")
    following_button.click()
    sleep(1)
    for i in range(iterations):
        try:
            unfollow_button = browser.find_element_by_xpath("//button[text()='Following']")
            unfollow_button.click()
            comfirm_button = browser.find_element_by_xpath("//button[text()='Unfollow']")
            comfirm_button.click()
            print("done")
            sleep(5)
        except:
            print("Error while trying to unfollow account number " + str(i) + " of the list")
            pass
    browser.close()