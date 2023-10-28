import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")

        play_again = input("Roll again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()

