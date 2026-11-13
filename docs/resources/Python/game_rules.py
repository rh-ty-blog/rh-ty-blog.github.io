        
#insert the if statements directly between the `print("You rolled a", dice)` and the `print("Balance:", bank_balance, "euro")`
#make sure these if statements are indented under the for loop correctly, (the if statements should be indented under the for loop 8 spaces exactly)
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