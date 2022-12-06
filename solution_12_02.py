data = open('data/data_12_02.txt', 'r').read().split('\n')

options_a = ["A", "B", "C"]
options_b = ["X", "Y", "Z"]
def play_game1(input):
    index_a = options_a.index(input[0]) 
    index_b = options_b.index(input[2])
    if index_a == index_b:
        score = 3
    elif (index_b == 0 and index_a == 1) or (index_b == 1 and index_a == 2) or (index_b == 2 and index_a == 0):
        score = 0
    else:
        score = 6

    value = index_b + 1

    return score + value

game_result = map(play_game1, data)

print(sum(game_result))

####### Part 2
def play_game2(input):
    index_a = options_a.index(input[0]) 
    match input[2]:
        case "X":
            score = 0
            value = ((index_a + 2) % 3) + 1 
        case "Y": 
            score = 3
            value = index_a + 1
        case "Z":
            score = 6
            value = ((index_a + 1) % 3) + 1

    return score + value

game_result = map(play_game2, data)

print(sum(game_result))