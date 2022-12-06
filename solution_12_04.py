data = open('data/data_12_04.txt', 'r').read().split('\n')

count = 0

for pair in data:
    range1_str, range2_str = pair.split(",")

    range1 = list(map(int, range1_str.split("-")))
    range2 = list(map(int, range2_str.split("-")))

    if((range1[0] >= range2[0] and range1[1] <= range2[1]) or (range2[0] >= range1[0] and range2[1] <= range1[1])):
        count += 1

print(count)

####### Part 2
count = 0

for pair in data:
    range1_str, range2_str = pair.split(",")

    range1 = list(map(int, range1_str.split("-")))
    range2 = list(map(int, range2_str.split("-")))

    if(range1[0] <= range2[0] <= range1[1] or
       range1[0] <= range2[1] <= range1[1] or
       range2[0] <= range1[0] <= range2[1] or
       range2[0] <= range1[1] <= range2[1]):
       count += 1

print(count)