
with open('depth.txt') as f:
    lines = list(map(int, f.readlines()))

    summe = 0
    summe_alt = 0
    count = -1
    lines_3 = []

    for i in range(len(lines) - 2):
        lines_3 = [lines[i], lines[i + 1], lines[i + 2]]
        summe = sum(lines_3)
        print(summe)

        if summe > summe_alt:
            count += 1

        summe_alt = summe

    print("Count:", count)
