def main():

    max_cal = 0
    m_cal_stack = []

    file = open("input", "r")
    lines = file.readlines()

    curr_cal = 0
    for i in lines:
        if i != "\n":
            curr_cal += int(i)
        else:
            max_cal = max(curr_cal, max_cal)
            if len(m_cal_stack) < 3:
                m_cal_stack.append(curr_cal)
            elif m_cal_stack[2] < curr_cal:
                m_cal_stack.pop()
                m_cal_stack.append(curr_cal)
            m_cal_stack = sorted(m_cal_stack, reverse=True)
            curr_cal = 0


    print(m_cal_stack)
    print(sum(m_cal_stack))
    print(max_cal)



if __name__ == "__main__":
    main()
