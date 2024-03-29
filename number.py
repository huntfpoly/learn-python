def main():
    x = get_int()
    print(x)


def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("You must enter a number.")
            pass
        else:
            return x


main()
