def main():

    count = 0

    file = open("input", "r")
    lines = file.readlines()

    for i in lines:
        r = i.strip()
        n = len(r)
        r1 = r[0:int(n / 2)]
        r2 = r[int(n / 2):n]

        char = set(r1).intersection(set(r2))
        ele = char.pop()
        if ele >= "a":
            count += ord(ele) - 96
        else:
            count += ord(ele) - 64 + 26
    print(count)


if __name__ == "__main__":
    main()
