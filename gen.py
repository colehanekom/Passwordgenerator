import random

# 33 - 126 ascii

list = []

while len(list) != 12:
    list.append(chr(random.randint(33,126)))

print("Password: ",' '.join(list))