# with open('names.txt', 'r') as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(line.rstrip())
names = []
with open('names.txt', 'r') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(name)
