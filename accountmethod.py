from time import sleep
from selenium import webdriver
from login import login

def accountmethod(user_username, user_pwd, iterations, target):
    browser = webdriver.Chrome("./chromedriver.exe")
    login(user_username, user_pwd, browser)
    browser.get("https://www.instagram.com/" + target + "")
    sleep(2)
    try:
        followers_button = browser.find_element_by_xpath("//a[@href='/" + target + "/followers/']")
        followers_button.click()
    except:
        print("The account is private or does not exist. Make sure the username is correct")
        return

    print("Following followers of " + target)
    for i in range(iterations):
        try:
            follow_buttons = browser.find_elements_by_xpath("//button[text()='Follow']")
            follow_buttons[1].click()
            print("done")
            sleep(3)
        except:
            print("The account is probably displaying suggestions, causing the program to bug. You may also have already followed to much people from that account")
    browser.close()