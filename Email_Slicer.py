"""
Email slicer is a program that will take a particular email and then slices it into username and domain.For example,
hello@gmail.com is an email in which we will separete username which is "hello", separete the domain "gmail", a
nd the extension which is "com" after the dot.

The pscudo code is followed below.
"""

#Collect email from user
#Slice the email using @, first part as the username and the second part is gonna be saved as domain.
#Split domain using dot.,

import email


def main():
    print("Welcone to email slicer")
    print("")

    email_input = input("Input your email address: ")

    (username,domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

main()