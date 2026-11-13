import random


def main():
    bank_balance = 50
    rounds = int(input("How many rounds do you want to play? "))
    print("Starting balance:", bank_balance, "euro")
    print("Playing", rounds, "rounds")

    for round_number in range(1, rounds + 1):
        print("--- Round", round_number, "---")

        input("Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print("You rolled a", dice)

        if dice == 1:
            print("Bad luck! You lose 15 euro")
            bank_balance = bank_balance - 15
        elif dice == 2:
            print("Nice roll! You win 10 euro!")
            bank_balance = bank_balance + 10
        elif dice == 3:
            print("Ouch! You lose 20 euro")
            bank_balance = bank_balance - 20
        elif dice == 4:
            print("Unlucky roll! You lose 10 euro")
            bank_balance = bank_balance - 10
        elif dice == 5:
            print("Sweet! You win 5 euro!")
            bank_balance = bank_balance + 5
        elif dice == 6:
            print("Jackpot! You win 25 euro!")
            bank_balance = bank_balance + 25

        print("Balance:", bank_balance, "euro")

    print("=== GAME OVER ===")
    print("Final balance:", bank_balance, "euro")


if __name__ == "__main__":
    main()

