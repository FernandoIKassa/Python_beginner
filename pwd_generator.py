import random
import string


chars = list(string.ascii_letters + string.digits + string.punctuation)

print("How many passwords do you need?")
pwd_number = int(input())

print("How many chars for every password")
pwd_length = int(input())

print('\nPasswords generated:')

for pwd in range(pwd_number):
    passwords = ''
    for x in range(pwd_length):
        passwords += random.choice(chars)
    print(passwords)
