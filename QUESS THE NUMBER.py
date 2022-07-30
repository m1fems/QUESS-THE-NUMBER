import random


def the_random_number(number):
    print(f'The number was {number}')
    quit()


random_number = random.randint(1, 10)
print('You have 3 tries to guess the number I`m thinking of')
i = 0
for i in range(3):
    guess = int(input())
    if guess == random_number:
        print('CONGRATULATIONS YOU GOT THE NUMBER RIGHT')
    elif guess < random_number:
        i += 1
        if i == 3:
            the_random_number(random_number)
        print('The number is bigger')
    elif guess > random_number:
        i += 1
        if i == 3:
            the_random_number(random_number)
        print('The number is lower')
