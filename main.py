def main():
    while True:
        menu()
        x = int(input("Please enter an option: "))
        if x == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")
        if x == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
        if x == 3:
            break

def encode(password):
    list = ""
    for i in password:
        i = int(i)
        i += 3
        if i >= 10:
            i -= 10
        list += str(i)
    return list

def decode(password):
    list = ""
    for i in password:
        i = int(i)
        i -= 3
        if i <= 0:
            i += 10
        list += str(i)
    return list


def menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

if __name__ == "__main__":
    main()