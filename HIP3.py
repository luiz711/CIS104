pennies = int(input("How many pennies do you have?:"))

nickels = int(input("How many nickels do you have?:"))

dimes = int(input("How many dimes do you have?:"))

quarters = int(input("How many quarters do you have?:"))

half_dollars = int(input("How many half dollars do you have?:"))

dollar_coins = int(input("How many dollar coins do you have?:"))

cents = float (pennies + (nickels * 5) + (dimes * 10) + (quarters * 25) + (half_dollars * 50) + (dollar_coins * 100))

amount = float (cents )