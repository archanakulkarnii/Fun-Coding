import random

nump = random.randint(1000, 9999)

print("🎯 Welcome to the Number Guessing Game!")
print("Guess the 4-digit number! (Enter 0 to quit)")

while True:
    n = int(input("Enter your 4-digit guess: "))

    if n == 0:
        print("You quit the game. Goodbye!")
        break

    num = nump
    temp = n
    correct_digits = 0

    # Compare each digit from right to left
    for i in range(4):
        if num % 10 == temp % 10:
            correct_digits += 1
        num //= 10
        temp //= 10

    if correct_digits == 4:
        print(f"🎉 Congrats! You guessed it right! The number was {nump}.")
        break
    else:
        print(f"{correct_digits} digit(s) were guessed correctly.")
