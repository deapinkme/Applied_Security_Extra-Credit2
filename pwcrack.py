import base64
from binascii import hexlify
from hashlib import sha256
    
def hash_pword(salt, pword): # from extras.py
    hasher = sha256()
    hasher.update(salt)
    try:
        hasher.update(pword.encode('utf-8'))
    except:
        return("")
    return hasher.hexdigest()

def password_crack(pwFile, pwSaltHash):
    salt, pwHash = pwSaltHash.split('$')
    afile = open(pwFile, 'r')

    for line in afile:
        # print(line.strip()) # test
        currPW = line.strip()
        if hash_pword(salt, currPW) == pwHash: # check that currPW and then hash are str
            print("The password is: " + currPW)
            break
        
    print("Completed.")
    afile.close

password_crack("rockyou.txt", "000000000000000000000000000078d2$18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3")