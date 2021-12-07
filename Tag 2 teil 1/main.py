with open('g-code.txt') as f:
    lines = f.readlines()

position = [0, 0]

for line in lines:
    lines_split = line.split(" ")
    lines_split[1] = int(lines_split[1])
    print(lines_split)
    if lines_split[0] == "forward":
        position[0] += lines_split[1]

    if lines_split[0] == "down":
        position[1] += lines_split[1]

    if lines_split[0] == "up":
        position[1] -= lines_split[1]
position_fin = position[0] * position[1]
print(position_fin)




# string = "Hello World"
# string = string.split(" ")
# print(string)
