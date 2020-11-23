from time import sleep
from selenium import webdriver
from login import login
import math

def followermethod(user_username, user_pwd, iterations):
    browser = webdriver.Chrome("./chromedriver.exe")
    login(user_username, user_pwd, browser)
    browser.get("https://www.instagram.com/" + user_username + "")
    sleep(2)
    followers_button = browser.find_element_by_xpath("//a[@href='/" + user_username + "/followers/']")
    followers_button.click()
    sleep(1)

    nbaccounts = 1

    if iterations > 10:
        nbaccounts = math.ceil(iterations / 10)
    accounts_per_acc = math.ceil(iterations / nbaccounts)
    i = 0
    while i < nbaccounts:
        continuewhile = False
        followers = browser.find_elements_by_class_name("FPmhX.notranslate._0imsa")
        followers[i].click()
        sleep(2)
        current_account = browser.current_url
        current_account = current_account[:-1]
        current_account = current_account[26:]
        print("Following followers of " + current_account)
        try:
            followers_button = browser.find_element_by_xpath("//a[@href='/" + current_account + "/followers/']")
            followers_button.click()
        except:
            print("Error: this account is private. Returning to another account")
            i += 1
            nbaccounts += 1
            browser.get("https://www.instagram.com/" + user_username + "")
            sleep(2)
            sleep(2)
            followers_button = browser.find_element_by_xpath("//a[@href='/" + user_username + "/followers/']")
            followers_button.click()
            continue
        for l in range(accounts_per_acc):
            try:
                follow_buttons = browser.find_elements_by_xpath("//button[text()='Follow']")
                follow_buttons[1].click()
                print("done")
            except:
                print("Error: this account displays suggestions, causing the program to bug. Returning to another account")
                continuewhile = True
                break
            sleep(3)
        if continuewhile:
            i += 1
            nbaccounts += 1
            browser.get("https://www.instagram.com/" + user_username + "")
            sleep(2)
            followers_button = browser.find_element_by_xpath("//a[@href='/" + user_username + "/followers/']")
            followers_button.click()
            continue
        browser.get("https://www.instagram.com/" + user_username + "")
        sleep(2)
        followers_button = browser.find_element_by_xpath("//a[@href='/" + user_username + "/followers/']")
        followers_button.click()
        sleep(1)
        i += 1
    browser.close()