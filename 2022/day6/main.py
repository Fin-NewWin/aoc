def main():

    f = open("input", "r")
    lines = f.readlines()[0].strip()

    ans1 = False
    ans2 = False
    for i in range(3, len(lines)):
        if len(set(lines[i - 3:i + 1])) == 4 and not ans1:
            print(i + 1)
            ans1 = True
        if len(set(lines[i - 13:i + 1])) == 14 and not ans2:
            print(i + 1)
            ans2 = True




if __name__ == "__main__":
    main()
