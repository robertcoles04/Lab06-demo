def main():
    while True:
        menu()
        x = int(input("Please enter an option: "))
        if x == 1:
            password = int(input("Please enter your password to encode: "))
            print(encode(password))


def encode(password):
    list = ""
    for i in password:
        i = i
        i += 3
        if i >= 10:
            i -= 10
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
