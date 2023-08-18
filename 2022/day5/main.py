import copy


def main():

    f = open("input", "r")
    lines = f.readlines()

    arr = [[] for i in range(9)]
    arr2 = []
    for i in lines:
        if "[" in i:
            pos = 0
            for j in range(1, len(i), 4):
                if i[j] not in " ":
                    arr[pos].append(i[j])
                pos += 1
            arr2 = copy.deepcopy(arr)
        elif "move" in i:
            i = i.split()
            n = int(i[1])
            for j in range(n):
                arr[int(i[5]) - 1].insert(0, arr[int(i[3]) - 1].pop(0))
                arr2[int(i[5]) - 1].insert(0, arr2[int(i[3]) - 1].pop(n - j - 1))


    print(arr)
    print(arr2)

    for i in arr:
        print(i[0], end="")

    print("")

    for i in arr2:
        print(i[0], end="")

    print("")


if __name__ == "__main__":
    main()
