class Cave:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.rocks_x_min = 500
        self.rocks_x_max = 500
        self.interior = [["."] * self.width for _ in range(self.height)]
        self.sand_count = 0
    
    def scan_rock(self, scan: str):
        scan_split = scan.split(" -> ")
        
        for i in range(len(scan_split)-1): 
            p_start = list(map(int, scan_split[i].split(",")))
            p_end = list(map(int, scan_split[i+1].split(",")))

            # iterate either in x or y direction
            if p_start[0] == p_end[0]:
                y_range = range(min(p_start[1], p_end[1]), max(p_start[1], p_end[1]) + 1)
                for y in y_range:
                    self.add_rock(p_start[0], y)
            elif p_start[1] == p_end[1]:
                x_range = range(min(p_start[0], p_end[0]), max(p_start[0], p_end[0]) +1 )
                for x in x_range:
                    self.add_rock(x, p_start[1])

    def add_rock(self, x, y):
        if x < self.rocks_x_min:
            self.rocks_x_min = x
        elif x > self.rocks_x_max:
            self.rocks_x_max = x

        # Append new columns if x is out of bounds
        if x >= self.width-1:
            new_cells = ["."] * (x - self.width + 2)
            for i in range(len(self.interior)):
                self.interior[i] += new_cells
            self.width = len(self.interior[0])
            
        # Append new rows if y is out of bounds
        if y >= self.height-1:
            for _ in range(y - self.height + 1):
                self.interior.append(["."] * self.width)
            self.height = len(self.interior)

        self.interior[y][x] = "#"

    def fill(self):
        while True:
            count1 = self.sand_count
            self.add_sand()
            count2 = self.sand_count
            if count1 == count2:
                return self.sand_count

    def print(self):
        cols = [str(i) for i in range(self.rocks_x_min, self.rocks_x_max+1)]
        print("    " + "".join([s[0] for s in cols]))
        print("    " + "".join([s[1] for s in cols if int(s) >= 10]))
        print("    " + "".join([s[2] for s in cols if int(s) >= 100]))

        for i, row in enumerate(self.interior):
            s = str(i).zfill(3) + " " + "".join(row[self.rocks_x_min:self.rocks_x_max+1])
            print(s)

class InfiniteCave(Cave):
    def add_sand(self):
        pos_x = 500
        pos_y = 0
        in_rest = False
        in_void = False

        while not in_rest and not in_void:
            if self.interior[pos_y + 1][pos_x] == ".":
                pos_y += 1
            elif self.interior[pos_y + 1][pos_x - 1] == ".":
                pos_x -= 1
                pos_y += 1
            elif self.interior[pos_y + 1][pos_x + 1] == ".":
                pos_x += 1
                pos_y += 1
            else:
                in_rest = True
                self.sand_count += 1
                self.interior[pos_y][pos_x] = "o"
            
            if not self.rocks_x_min <= pos_x <= self.rocks_x_max or pos_y >= self.height -1:
                in_void = True

class FiniteCave(Cave):
    def __init__(self, height: int, width: int):
        super().__init__(height, width)
        self.source_blocked = False

    def add_sand(self):
        pos_x = 500
        pos_y = 0
        in_rest = False
        in_void = False

        while not in_rest and not in_void and not self.source_blocked:
            if self.interior[pos_y + 1][pos_x] == ".":
                pos_y += 1
            elif self.interior[pos_y + 1][pos_x - 1] == ".":
                pos_x -= 1
                pos_y += 1
            elif self.interior[pos_y + 1][pos_x + 1] == ".":
                pos_x += 1
                pos_y += 1
            else:
                in_rest = True
                self.sand_count += 1
                self.interior[pos_y][pos_x] = "o"

            if not self.rocks_x_min <= pos_x <= self.rocks_x_max or pos_y >= self.height -1:
                in_void = True
        
        if pos_x == 500 and pos_y == 0:
            self.source_blocked = True
            
    def scan_ground(self):
        rock = f"{500-self.height-1},{self.height+1} -> {500+self.height+1},{self.height+1}"
        self.scan_rock(rock)

if __name__ == "__main__":
    data = open('data/data_12_14.txt', 'r').read().split('\n')
    
    # Case 1
    cave1 = InfiniteCave(1, 500)
    for rock in data:
        cave1.scan_rock(rock)
    res1 = cave1.fill()
    # cave1.print()
    print(res1)
    
    # Case 2
    cave2 = FiniteCave(1, 700)
    for rock in data:
        cave2.scan_rock(rock)
    cave2.scan_ground()
    res2 = cave2.fill()
    # cave2.print()
    print(res2)


