data = open('data/data_12_01.txt', 'r').read().split('\n')

count = max_count = 0

for val in data:
    if val == "": 
        if count > max_count:
            max_count = count
        count = 0
    else:
        count += int(val)

print(max_count)

###### Part 2
total_calories = []
current_sum = 0
for snack in data:
    if snack == "": 
        total_calories.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(snack)

top3 = sorted(total_calories, reverse=True)[:3]
print(sum(top3))
