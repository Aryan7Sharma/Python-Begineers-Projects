import random

try:
    def guess(x):
        random_number = random.randint(1, x)
        guess = 0
        count = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')
            count+=1

        print(f'Yay, congrats. You have guessed the number {random_number} correctly in {count} attempts!!')
except Exception as e:
    print(e)


guessing_range = int(input('Please tell us What range would you like to set for playing this game  :'))
guess(guessing_range)  # Calling guess function

