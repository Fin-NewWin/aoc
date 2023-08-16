def main():

    score = 0
    win_score = 0

    file = open("input", "r")
    lines = file.readlines()

    for i in lines:
        op = i.strip()[0]
        mc = i.strip()[2]
        if op == "A":
            if mc == "X":
                score += 1 + 3
                win_score += 3 + 0
            elif mc == "Y":
                score += 2 + 6
                win_score += 1 + 3
            elif mc == "Z":
                score += 3 + 0
                win_score += 2 + 6
        elif op == "B":
            if mc == "X":
                score += 1 + 0
                win_score += 1 + 0
            elif mc == "Y":
                score += 2 + 3
                win_score += 2 + 3
            elif mc == "Z":
                score += 3 + 6
                win_score += 3 + 6
        else:
            if mc == "X":
                score += 1 + 6
                win_score += 2 + 0
            elif mc == "Y":
                score += 2 + 0
                win_score += 3 + 3
            elif mc == "Z":
                score += 3 + 3
                win_score += 1 + 6
    print(score)
    print(win_score)


if __name__ == "__main__":
    main()
