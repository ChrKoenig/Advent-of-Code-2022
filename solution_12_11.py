import math

class Monkey:
    def __init__(self, starting_items, operation, test_factor, test_true, test_false):
        self.items = starting_items
        self.operation = operation
        self.test_factor = test_factor
        self.test_true = test_true
        self.test_false = test_false
        self.inspection_counter =  0
    
    def inspect_item(self, item):
        self.inspection_counter += 1
        old = item
        new = eval(self.operation)
        #item = math.floor(new / 3)
        item = new % 9699690  # Product of all test_factors

        if item % self.test_factor == 0:
            return((item, self.test_true))
        else:
            return((item, self.test_false))
    
    def null_items(self):
        self.items = []

    def append_item(self, item):
        self.items.append(item)

if __name__ == "__main__":
    monkeys = []

    monkeys.append(Monkey([57], "old * 13", 11, 3, 2))
    monkeys.append(Monkey([58, 93, 88, 81, 72, 73, 65], "old + 2", 7, 6, 7))
    monkeys.append(Monkey([65, 95], "old + 6", 13, 3, 5))
    monkeys.append(Monkey([58, 80, 81, 83], "old * old", 5, 4, 5))
    monkeys.append(Monkey([58, 89, 90, 96, 55], "old + 3", 3, 1, 7))
    monkeys.append(Monkey([66, 73, 87, 58, 62, 67], "old * 7", 17, 4, 1))
    monkeys.append(Monkey([85, 55, 89], "old + 4", 2, 2, 0))
    monkeys.append(Monkey([73, 80, 54, 94, 90, 52, 69, 58], "old + 7", 19, 6, 0))

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                item, new_monkey = monkey.inspect_item(item)
                monkeys[new_monkey].append_item(item)
            monkey.null_items()
                        
    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i} inspected items {monkey.inspection_counter} times")
    
    inspections = [monkey.inspection_counter for monkey in monkeys]
    inspections.sort()
    print(inspections[-1] * inspections[-2])   
    
