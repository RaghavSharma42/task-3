import random
import string

s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation

pass_length = int(input("Enter lemgth of your password :\n"))

n_letters = int(input("How many letters you want :\n"))
n_digits = int(input("How many digits you want :\n"))
n_symbols = int(input("How many symbols you want :\n"))
total_characters = n_letters + n_digits + n_symbols
if total_characters > pass_length:
    print("Total characters exceed password length. Please adjust.")
    exit()
password = ""
for i in range(1,n_letters+1):
    char = random.choice(s1)
    password = password + char

for i in range(1,n_digits+1):
    char = random.choice(s2)
    password = password + char

for i in range(1,n_symbols+1):
    char = random.choice(s3)
    password = password + char

print(password)