

with open('depth.txt') as f:
    lines = list(map(int, f.readlines()))

    line_alt = 0
    count = -1

    for line in lines:
        if line > line_alt:
            count += 1

        line_alt = line
    print(count)
