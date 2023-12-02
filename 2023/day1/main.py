def main():
    file = open("input", "r")
    lines = file.readlines()

    number = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    sum = 0

    for line in lines:
        first = last = ""
        for i in range(len(line)):
            if line[i] in number:
                if first == "":
                    first = line[i]
                last = line[i]
            elif line[i] >= "a" and line[i] <= "z":
                cnt = 1 + i
                while cnt < len(line) and line[i] >= "a" and line[i] <= "z":
                    if line[i:cnt] in numbers:
                        if first == "":
                            first = line[i:cnt]
                        last = line[i:cnt]
                        break
                    cnt += 1
        if first in numbers:
            first = number[numbers.index(first)]
        if last in numbers:
            last = number[numbers.index(last)]
        sum += int(first + last)
    print(sum)


if __name__ == "__main__":
    main()
