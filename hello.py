def main():
    name = input("What's your name?")
    check = input("Do you accept the '100 days of code' challenge? (y/n)").lower()

    if check == 'y':
        print(f"Hello{name}, Thanks for accepting the challenge")
    elif check == 'n':
        print(f"Hello{name}, Oops, the challenge would have been fun")
    else:
        print("invalid input, cheers!")

main()

    