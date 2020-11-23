import math
from selenium import webdriver
from time import sleep
from login import login

def followkeyword(user_username, user_pwd, iterations):
    keyword = input("Keyword (string to search on instagram): ")
    browser = webdriver.Chrome("./chromedriver.exe")
    login(user_username, user_pwd, browser)
    nbaccounts = 1
    if iterations > 10:
        nbaccounts = math.ceil(iterations / 10)
    accounts_per_acc = math.ceil(iterations / nbaccounts)
    browser.get("https://www.instagram.com/" + user_username + "/")
    c = 0
    while c < nbaccounts:
        continuewhile = False
        try:
            search_bar = browser.find_element_by_css_selector("input[placeholder='Search']")
        except:
            print("Error: couldn't find the search bar")
            browser.close()
            return
        search_bar.send_keys(keyword)
        sleep(2)
        try:
            results = browser.find_elements_by_class_name("yCE8d")
        except:
            print("Error: couldn't find any results for your keyword")
            browser.close()
            return
        results[c].click()
        sleep(3)
        target = browser.current_url
        target = target[:-1]
        target = target[26:]
        currurl = browser.current_url
        try:
            followers_button = browser.find_element_by_xpath("//a[@href='/" + target + "/followers/']")
            followers_button.click()
        except:
            print("This account is private or it is a hashtag. Going to the next account")
            c += 1
            nbaccounts += 1
            continue
        print("Following followers of " + target)
        sleep(1)
        for i in range(accounts_per_acc):
            try:
                follow_buttons = browser.find_elements_by_xpath("//button[text()='Follow']")
                follow_buttons[1].click()
                print("done")
            except Exception as e:
                print("Error: this account displays suggestions, or it is ")
                print(e)
                browser.get(currurl)
                sleep(3)
                continuewhile = True
                break
            sleep(3)

        if continuewhile:
            c += 1
            nbaccounts += 1
            browser.get(currurl)
            sleep(3)
            continue
        browser.get(currurl)
        sleep(3)
        c += 1