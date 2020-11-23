import time
from selenium import webdriver
from followermethod import *
from accountmethod import *
from unfollow import *


#choose between following follower's followers or following followers of an account.

user_username = "username" #your username. NOT YOUR EMAIL (will make the program crash)
user_pwd = "pwd" #your password

print("Your selected account is " + user_username + ". You can change it in the main.py file.")
method_choice = input("Choose between follower's followers or followers of an account, or unfollow people (0, 1 or 2): ")
method_choice_c = 0
while True:
    if method_choice_c > 0:
        method_choice = input("Type a number again: ")
    try:
        method_choice = int(method_choice)
        if method_choice == 0 or method_choice == 1 or method_choice == 2:
            break
        else:
            print("Please enter a number between 0, 1 and 2")
    except:
        print("Please enter a valid number.")
    method_choice_c += 1

iterations = 0

while True:
    try:
        iterations = int(input("Number of people to (un)follow (approx.): "))
        break
    except:
        print("Please enter a valid number.")

if method_choice == 0:
    followermethod(user_username, user_pwd, iterations)
elif method_choice == 1:
    target = input("Targeted account username: ")
    accountmethod(user_username, user_pwd, iterations, target)
elif method_choice == 2:
    unfollow(user_username, user_pwd, iterations)
