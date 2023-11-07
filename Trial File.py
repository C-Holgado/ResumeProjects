import random
guess = input('Enter an integer between 0 and 9')
answer = random.randrange(0,9)
if guess.isdigit() and (guess == answer):
    print('Your guess is correct')
    print('The Correct Answer is :', answer)
elif guess.isdigit() and (guess != answer):
    print('Your guess is not correct')
    print('The Correct Answer is :', answer)
else:
    print('Your guess is not a positive integer')
