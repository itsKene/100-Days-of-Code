def main():
    print(challenge(get_info()))
    

def get_info():
    name = input("What's your name? ")
    check = input("Do you accept the '100 days of code' challenge? (y/n)\n ").lower()
    return name, check

def challenge(name, check):
    if check == 'y':
        return f"Hello {name}, Thanks for accepting this challenge"
    elif check == 'n':
        return f"Hello {name}, Oops, the challenge would have been fun"
    else:
        return "invalid input, cheers!"

main()

    