from art import logo
import random

print(logo)

number = random.randint(1, 100)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")

EASY = 10
HARD = 5

if difficulty == 'easy':
  attempts = EASY
elif difficulty == 'hard':
  attempts = HARD

while attempts > 0:
  print(f'You have {attempts} attempts remaining to guess the number.')
  guess = int(input("Make a guess: "))
  if guess < number:
    print("Too low.")
  elif guess > number:
    print("Too high.")
  elif guess == number:
    print("You got it! The answer was " + str(number) + ".")
    attempts = 0
  if attempts == 1:
    print("You've run out of guesses, you lose.")
    attempts = 0
  attempts -= 1
  if attempts > 0:
    print("Guess again.")
