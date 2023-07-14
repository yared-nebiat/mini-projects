'''This is a module that and contains two functions,
the "encrypt" function and the "decrypt" function which encrypt and decrypt
a string respectively.'''

def encrypt(string, key):
    '''This function takes two positional arguments and is used to encrypt
the string by shifting up the alphabet by the amount stated as key.'''
    scrambled = ''
    length = len(string)
    for index in range(length):
        scrambled += chr(ord(string[index]) + key)
    return scrambled


def decrypt(string, key):
    '''This function takes two positional argument and is used to decrypt
an encrypted string by shifting down the alphabet by the amount stated as key.'''
    unscrambled = ''
    length = len(string)
    for index in range(length):
        unscrambled += chr(ord(string[index]) - key)
    return unscrambled
