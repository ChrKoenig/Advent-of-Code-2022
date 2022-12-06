import re

data = open('data/data_12_05.txt', 'r').read().split('\n')

def import_stacks(data):
    stacks = {new_list:[] for new_list in range(1,10)}

    for line in data:
        if line == " 1   2   3   4   5   6   7   8   9 ":
            break
        for j, k in enumerate(range(1, 37, 4)):
            if(line[k] != " "):
                stack_index = j+1
                item = line[k]
                stacks[stack_index].insert(0, item)
    
    return(stacks)  

def move_items(line, stacks):
    n_items, stack_1, stack_2, = re.findall(r'\d+', line)
    for _ in range(int(n_items)):
        item = stacks[int(stack_1)].pop()
        stacks[int(stack_2)].append(item)

stacks = import_stacks(data)

for line in data[10:]:
    move_items(line, stacks)

solution = ""
for stack in stacks.values():
    solution += stack.pop()

print(solution)

######## Part 2
def move_items2(line, stacks):
    n_items, stack_1, stack_2, = re.findall(r'\d+', line)
    items = []
    for _ in range(int(n_items)):
        item = stacks[int(stack_1)].pop()
        items.append(item)
    
    items.reverse()
    stacks[int(stack_2)].extend(items)
    
stacks = import_stacks(data)

for line in data[10:]:
    move_items2(line, stacks)

solution = ""
for stack in stacks.values():
    solution += stack.pop()

print(solution)