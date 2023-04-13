"""
This is a code for a Soda dispenser.
This dispenser can only take in 5 cents, 10 cents, and 25 cents and ignores other inputs.
However, it won't dispense until a total of 50 cents have been reached.
If you exceed the 50 cent, it displays your change also.

"""


def main(soda = 50):
    coin = prompt(soda)
    soda = soda - coin
    if soda > 0:
        main(soda)
    else:
        print("Change Owed:", (soda * -1))


def prompt(k):
    i = k
    print("Amount Due:", i)
    c = int(input("Insert Coin: ").strip())
    valid = [5, 10, 25]
    if c in valid:
        return c
    else:
        main(i)



main()