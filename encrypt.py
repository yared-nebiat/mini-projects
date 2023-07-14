from Cipher import encrypt

with open("message.txt", "r") as doc:
    msg = []
    for line in doc:
        scrambled = encrypt(line,5)
        msg.append(scrambled)

with open("scrambled.txt", "w") as encrypted_doc:
    for each in msg:
        print(each, end='', file=encrypted_doc)