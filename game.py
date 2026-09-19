import random

secret = random.randint(1, 20)
attempt = 0

while True:
    guess = int(input("Enter the number: "))
    attempt += 1

    if guess == secret:
        print(f"You guessed it in {attempt} attempts")
        break
    elif guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")