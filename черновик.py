# with open('history.txt') as file:
#     lines = [line.rstrip() for line in file]
# print(lines)


with open('history.txt') as f:
    lines = [line.rstrip('\n') for line in f]
print(lines)
