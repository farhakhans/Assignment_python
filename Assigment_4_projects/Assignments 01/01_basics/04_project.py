import random

TOTAL_NUMBERS: int = 10
LOW: int = 1
HIGH: int = 100

def main():
    print("🎲 Generating", TOTAL_NUMBERS, "random numbers between", LOW, "and", HIGH)

    for i in range(TOTAL_NUMBERS):
        number = random.randint(LOW, HIGH)
        print("Number", i + 1, ":", number)

# Run the main function
main()
