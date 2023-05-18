"""
Simple app that lets the user encrypt a password and then check that the password matches the encrypted password.
"""

import hashlib

def encrypt_password(password):
    """
    Encrypts the password using the SHA256 algorithm.
    :param password: The password to encrypt.
    :return: The encrypted password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("Welcome to the password checker!")
    print("Please enter a password to encrypt:", end=" ")
    password = input()
    # overwrite the password variable with the encrypted password
    password = encrypt_password(password)
    print("Your encrypted password is:", password)
    print("Please enter a password to check:", end=" ")
    check_password = input()
    # overwrite the check_password variable with the encrypted password
    check_password = encrypt_password(check_password)
    if password == check_password:
        print("The passwords match!")
    else:
        print("The passwords do not match!")


if __name__ == '__main__':
    main()