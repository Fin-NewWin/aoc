def main():

    count = 0
    three_count = 0

    file = open("message.txt", "r")
    lines = file.readlines()
    three_lines = 0
    three_r = []

    for i in lines:
        three_lines += 1
        three_r.append(i.strip())
        if three_lines == 3:
            three_char = set(three_r[2]).intersection(set(three_r[0]).intersection(set(three_r[1])))
            print(three_char)
            three_ele = three_char.pop()
            if three_ele >= "a":
                three_count += ord(three_ele) - 96
            else:
                three_count += ord(three_ele) - 64 + 26
            three_r = []
            three_lines = 0

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
    print(three_count)


if __name__ == "__main__":
    main()
