def main():

    count1 = 0
    count2 = 0

    f = open("day4.txt", "r")
    lines = f.readlines()

    for i in lines:

        t = i.split(",")
        t1 = t[0].strip()
        t2 = t[1].strip()

        t1a = int(t1.split("-")[0])
        t1b = int(t1.split("-")[1])

        t2a = int(t2.split("-")[0])
        t2b = int(t2.split("-")[1])

        if t1a <= t2a and t1b >= t2b or t2a <= t1a and t2b >= t1b:
            count1 += 1
        if t1a <= t2a <= t1b or t2a <= t1a <= t2b:
            count2 += 1

    print(count1)
    print(count2)


if __name__ == "__main__":
    main()
