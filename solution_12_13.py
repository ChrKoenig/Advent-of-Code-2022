from functools import cmp_to_key

def is_in_order(left, right):
    # Catch int pairs right away
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        elif left < right:
            return 1
        else: 
            return -1
    
    # Cast inputs to list
    if type(left) == int and type(right) == list:
        left = [left]
    if type(left) == list and type(right) == int:
        right = [right]

    # Compare lists
    if len(left) == 0 and len(right) == 0:
        return 0
    for i in range(max(len(left), len(right))):
        if len(left) <= i <= len(right):
            return 1
        if len(right) <= i <= len(left):
            return -1

        in_order = is_in_order(left[i], right[i])
        if in_order != 0:
            return in_order

    return 0

if __name__ == "__main__":
    data = open('data/data_12_13.txt', 'r').read().split('\n')
    data = [x for x in data if x != ""]

    # Part 1
    pairs_in_order = []
    for i in range(0, len(data), 2):
        left = eval(data[i])
        right = eval(data[i+1])

        in_order = is_in_order(left, right)
        if in_order == 1:
            index = (i/2)+1
            pairs_in_order.append(index)

    print(sum(pairs_in_order))

    # Part 2
    data.append("[[2]]")
    data.append("[[6]]")
    
    # avoid repeated eval
    data = [eval(x) for x in data]

    # sort data using is_in_order
    in_order_key = cmp_to_key(is_in_order)
    data.sort(key = in_order_key)
    data.reverse()

    # Calc decodey_key
    decoder_key = 1
    for i, x in enumerate(data):
        if x == [[6]] or x == [[2]]:
            decoder_key *= i+1
        
    print(decoder_key)