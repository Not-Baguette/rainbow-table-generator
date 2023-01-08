import requests as req
import hashlib


def check_password(password):
    # Find if the password exists in the list, returns true if it exists
    if passwords[password] <= 1:
        return True
    else:
        return False


def get_hash_dict():
    def hash_password(pw):
        # Hash the password using the sha1 algorithm
        return hashlib.sha1(pw.encode()).hexdigest()

    hashed_pass = dict()
    for password in passwords:
        hashed_pass[hash_password(password)] = password

    return hashed_pass


def convert_to_csv(hash_table):
    # Convert the dictionary to a csv file
    with open('table.csv', 'w') as f:
        for hashed, password in hash_table.items():
            f.write(f'{hashed},{password}\n')


# https://github.com/danielmiessler/SecLists/tree/aad07fff50ca37af2926de4d07ff670bf3416fbc/Passwords
password_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10" \
               "-million-password-list-top-1000000.txt"

passwords = req.get(password_url).text.splitlines()
passwords = {passwords[i]: i for i in range(len(passwords))}

hashed_pw = get_hash_dict()
convert_to_csv(hashed_pw)
