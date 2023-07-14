from Cipher import decrypt

with open("scrambled.txt", "r") as doc:
    msg = []
    for line in doc:
        unscrambled = decrypt(line,5)
        msg.append(unscrambled)

with open("recovered.txt", "w") as recovered:
    for each in msg:
        print(each, end='', file=recovered)