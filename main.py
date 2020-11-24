import time
from selenium import webdriver
from followermethod import *
from accountmethod import *
from unfollow import *
from comment import *
from followkw import *

#choose between following follower's followers or following followers of an account.

user_username = "" #your username. NOT YOUR EMAIL (will make the program crash)
user_pwd = "" #your password

print("Your selected account is " + user_username + ". You can change it in the main.py file.")
print("Method list:")
print("0 - Follow your followers' followers")
print("1 - Follow the followers of a specified account")
print("2 - Unfollow people")
print("3 - Post a comment on multiple accounts")
print("4 - Follow people following accounts fitting a keyword")
method_choice = input("Enter a number: ")
method_choice_c = 0
while True:
    if method_choice_c > 0:
        method_choice = input("Type a number again: ")
    try:
        method_choice = int(method_choice)
        if 0 <= method_choice <= 4:
            break
        else:
            print("Please enter a number between 0, 1, 2, 3 and 4")
    except:
        print("Please enter a valid number.")
    method_choice_c += 1

iterations = 0

while True:
    try:
        interationword = ""
        if method_choice == 0 or method_choice == 1:
            iterationword = "Number of people to follow: "
        elif method_choice == 2:
            iterationword = "Number of people to unfollow: "
        elif method_choice == 3:
            iterationword = "Number of comments to post: "
        elif method_choice == 4:
            iterationword = "Number of people to follow: "
        iterations = int(input(iterationword))
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
elif method_choice == 3:
    commentposts(user_username, user_pwd, iterations)
elif method_choice == 4:
    followkeyword(user_username, user_pwd, iterations)
