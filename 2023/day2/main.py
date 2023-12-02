def main():
    file = open("input", "r")
    lines = file.readlines()

    red = 12
    blue = 14
    green = 13

    count = 0
    id = 1

    for line in lines:
        stop = False
        count += id
        line = line.strip().split(";")
        line[0] = line[0].split(":")[1]
        for i in line:
            i = i.split(",")
            for j in i:
                j = j.strip().split(" ")
                val = int(j[0])
                if j[1] == "red" and val > red:
                    count -= id
                    stop = True
                    break
                elif j[1] == "blue" and val > blue:
                    count -= id
                    stop = True
                    break
                elif j[1] == "green" and val > green:
                    count -= id
                    stop = True
                    break
            if stop:
                break
        id += 1

    min_count = 0
    for line in lines:
        temp = [0, 0, 0]
        line = line.strip().replace(";", "").replace(",", "").split()[2:]
        for i in range(0, len(line), 2):
            val = int(line[i])
            color = line[i + 1]
            if color == "red":
                temp[0] = max(val, temp[0])
            if color == "blue":
                temp[1] = max(val, temp[1])
            if color == "green":
                temp[2] = max(val, temp[2])
        # print(temp)
        min_count += temp[0] * temp[1] * temp[2]

    print(count)
    print(min_count)


if __name__ == "__main__":
    main()
