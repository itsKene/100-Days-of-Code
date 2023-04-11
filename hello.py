def main():
    print(challenge(get_info()))
    

def get_info():
    name = input("What's your name? ")
    check = input("Do you accept the '100 days of code' challenge? (y/n)\n ").lower()
    return name, check

def challenge(check):
    if check[1] == 'y':
        return f"Hello {check[0]}, Thanks for accepting this challenge"
    elif check[1] == 'n':
        return f"Hello {check[0]}, Oops, the challenge would have been fun"
    else:
        return "invalid input, cheers!"

main()

    