import random
import string

#characters = string.ascii_letters + string.digits + string.punctuation
characters = string.ascii_letters + string.digits

password = ""

for i in range(8):
    password += random.choice(characters)

print("Random Password:", password)