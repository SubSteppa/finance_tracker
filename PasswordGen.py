import random
import string

# length = int(input('Enter Character lenght here'))  # passworld length

while True:
    length = int(input('Enter password length (min 10): '))
    if length >= 10:
        break
    print("Password length must be at least 10. Try again.")


digits = string.digits
punctuation = string.punctuation
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

password_list = [
    random.choice(digits),
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(punctuation)
]

all_chars = digits+punctuation+uppercase+lowercase

for _ in range(length - 4):
    password_list.append(random.choice(all_chars))

random.shuffle(password_list)

password = ''.join(password_list)
print('Password Generated Successfully')
print(password)
