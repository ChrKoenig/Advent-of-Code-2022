def scan_direction(range1, range2, mode = "rowwise"):
    visible_trees = []
    for i in range1:
        max_height = ""
        for j in range2:
            if(mode == "colwise"):
                height = data[j][i]
            else:
                height = data[i][j]
            if height > max_height:
                max_height = height
                if(mode == "colwise"):
                    visible_trees.append((j, i))
                else:
                    visible_trees.append((i, j))

    return(visible_trees)

def get_scenic_score(xpos, ypos):
    tree_limit_top = 0
    tree_limit_bottom = 0
    tree_limit_right = 0
    tree_limit_left = 0

    #Checking Top
    for x in range(xpos - 1, -1, -1):
        if data[x][ypos] < data[xpos][ypos]:
            tree_limit_top += 1
        elif data[x][ypos] >= data[xpos][ypos]:
            tree_limit_top += 1
            break
    #Checking Left
    for y in range(ypos - 1, -1, -1):
        if data[xpos][y] < data[xpos][ypos]:
            tree_limit_left  += 1
        elif data[xpos][y] >= data[xpos][ypos]:
            tree_limit_left += 1
            break
    #Checking Right
    for i in range(ypos + 1, len(data[xpos])):
        if data[xpos][i] < data[xpos][ypos]:
            tree_limit_right += 1
        elif data[xpos][i] >= data[xpos][ypos]:
            tree_limit_right += 1
            break
    #Checking Bottom
    for j in range(xpos + 1, len(data)):
        if data[j][ypos] < data[xpos][ypos]:
            tree_limit_bottom += 1
        elif data[j][ypos] >= data[xpos][ypos]:
            tree_limit_bottom += 1
            break

    return (tree_limit_top * tree_limit_left * tree_limit_bottom * tree_limit_right)



if __name__ == "__main__":
    data = open('data/data_12_08.txt', 'r').read().split('\n')

    # four passes, one for each direction
    dim = len(data)
    visible_left = scan_direction(range(dim), range(dim))
    visible_right = scan_direction(range(dim), range(dim-1, -1, -1))
    visible_top = scan_direction(range(dim), range(dim-1), mode = "colwise")
    visible_bottom = scan_direction(range(dim), range(dim-1, -1, -1), mode = "colwise")

    print(len(set(visible_left + visible_right + visible_top + visible_bottom)))
    print(get_scenic_score(455,63))