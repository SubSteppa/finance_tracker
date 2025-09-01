import random

while True:
    choice = input("Type Y or N to roll dice: ").lower()
    if choice == 'y':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f'{dice_1}, {dice_2}')
    elif choice == 'n':
        print("Thank you for playing")
        break   # only break if user chose 'n'
    else:
        print("Invalid Choice")


# Boring ass project
