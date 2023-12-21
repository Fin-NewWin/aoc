def main():
    file = open("input", "r")
    lines = file.readlines()

    for line in lines:
        for letter in line:
            if letter.isnumeric():
                print(letter, end="")
        print()


if __name__ == "__main__":
    main()
