from tree_map import tree_map

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
trees = []
res = 1

for slope in slopes:
    pos = 0
    count = 0
    right = slope[0]
    down = slope[1]
    line_break = down

    for line in tree_map:
        if pos == 0 or line_break == 1:
            length = len(line)
            while length <= pos:
                line += line
                length = len(line)

            if line[pos] == '#':
                count += 1

            pos += right
            line_break = down
        else:
            line_break -= 1

    res *= count

print(res)
