#!/usr/bin/env python3

import string
import random
import sys
import os

"""
This scripts generates random passwords inside `base_path`
The file name is taken from purpose user asked input.
"""

extra_chars = "@*_-!?.#" # Add or remove characters if they don't apply to your preferences
base_path = "/tmp/passwords.d"

password_length = int(input("How long should the password be? Please tell me in numbers: "))
purpose = input("What are you going to use this password for? ")

file_path = base_path + "/" + purpose

if os.path.isfile(file_path):
    print("Password for {} already exists!".format(purpose))

    overwrite = input("Do you want to overwrite it? [y/N]")
    if overwrite != "y":
        sys.exit(1)

password_characters = string.ascii_letters + string.digits + extra_chars
password = ""

for x in range(password_length):
    password += random.choice(password_characters)


print("Your new password for {} is {} and has been saved at: {}".format(
    purpose,
    password,
    file_path,
    )
)

try:
    os.mkdir(base_path)
except FileExistsError:
    pass

pw_file = open(file_path, 'w')

pw_file.write(password + "\n")
pw_file.close()