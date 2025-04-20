import random

def main():
    score = 0

    for _ in range(5):  # 5 rounds
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {your_number}")
        guess = input("Higher or lower? (h/l): ").lower()

        if (guess == "h" and your_number > computer_number) or (guess == "l" and your_number < computer_number):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your final score is: {score}")

main()
