def main():

    score = 0

    file = open("input.txt", "r")
    lines = file.readlines()

    dictA = {"rock": "A", "paper": "B", "scissors": "C"}
    dictB = {"rock": "X", "paper": "Y", "scissors": "Z"}
    dictC = { 1: "rock", 2: "paper", 3: "scissors"}

    for i in lines:
        op = i.strip()[0]
        mc = i.strip()[2]
        if op == "A":
            if mc == "X":
                score += 1 + 3
            elif mc == "Y":
                score += 2 + 6
            elif mc == "Z":
                score += 3 + 0
        elif op == "B":
            if mc == "X":
                score += 1 + 0
            elif mc == "Y":
                score += 2 + 3
            elif mc == "Z":
                score += 3 + 6
        else:
            if mc == "X":
                score += 1 + 6
            elif mc == "Y":
                score += 2 + 0
            elif mc == "Z":
                score += 3 + 3
    print(score)

if __name__ == "__main__":
    main()
