import random
import string

print("Welcome to Password Generator")
length = int(input("Enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = " "

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password is :",password)