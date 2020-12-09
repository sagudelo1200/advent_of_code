from tree_map import tree_map

pos = 0
trees = 0

for line in tree_map:
    length = len(line)
    while length <= pos:
        line += line
        length = len(line)

    if line[pos] == '#':
        trees += 1

    pos += 3
print(trees)
