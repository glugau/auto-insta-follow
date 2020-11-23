from time import sleep
from login import login
from selenium import webdriver
import math

def commentposts(user_username, user_pwd, iterations):

    keyword = input("Keyword (string to search on instagram): ")
    msgcount = 0
    while True:
        msgcount = input("How many different comments do you want to post? (max 10): ")
        try:
            msgcount = int(msgcount)
        except:
            print("Please input a valid number")
            continue
        if msgcount > 0 and msgcount <= 10:
            break
        else:
            print("Please input a number between 1 and 10")
    peracc = 0
    while True:
        peracc = input("How many comments per account/hashtag: ")
        try:
            peracc = int(peracc)
        except:
            print("Please input a valid number")
            continue
        if peracc > 0 and peracc <= 10:
            break
        else:
            print("Please input a number between 1 and 10")
    messages = []
    for i in range(msgcount):
        currI = str(i+1)
        newcomment = input("Comment " + currI + ":")
        messages.append(newcomment)
    browser = webdriver.Chrome("chromedriver.exe")
    login(user_username, user_pwd, browser)
    browser.get("https://www.instagram.com/" + user_username + "/")
    sleep(3)
    accountcount = math.ceil(iterations / peracc)
    c = 0
    while c < accountcount:
        currentmessage = 0
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
        curr_url = browser.current_url
        skip = False
        for l in range(peracc):
            try:
                posts = browser.find_elements_by_xpath('//a[contains(@href,"/p/")]')
                posts[l].click()
            except:
                print("Error while trying to click on an image")
                skip = True
                break
            sleep(2)
            try:
                textzone = browser.find_element_by_css_selector("textarea[placeholder='Add a comment…']")
                textzone.click()
                textzone = browser.find_element_by_css_selector("textarea[placeholder='Add a comment…']")
                textzone.send_keys(messages[currentmessage])
                submitbtn = browser.find_element_by_xpath("//button[text()='Post']")
                submitbtn.click()
            except:
                print("Error while trying to post a comment")
                skip = True
                break
            if currentmessage == len(messages) - 1:
                currentmessage = -1
            currentmessage += 1
            sleep(2)
            browser.get(curr_url)
            sleep(3)
        if skip:
            c += 1
            accountcount += 1
            continue
        c += 1