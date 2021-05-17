import base64
from binascii import hexlify
from hashlib import sha256

RANDOM_SEED = base64.b64decode("2RUHYAyJWdDdXOicZfnTRw==") # from settings.py - "stolen seed"
    
def hash_pword(salt, pword): # from extras.py
    hasher = sha256()
    hasher.update(RANDOM_SEED)
    hasher.update(pword.encode('utf-8'))
    print(hasher.hexdigest())
    print(salt)
    return hasher.hexdigest()

def password_crack(pwFile, pwHash):
    afile = open(pwFile, 'r')

    for line in afile:
        # print(line.strip()) # test
        currPW = line.strip()
        if hash_pword(RANDOM_SEED, currPW) == pwHash: # check that currPW and then hash are str
            print("The password is: " + currPW)
            break
        
    print("Completed.")
    afile.close

# Test
password_crack("password_list.txt", "test")
# password_crack("password_list.txt", "000000000000000000000000000078d2$18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3")