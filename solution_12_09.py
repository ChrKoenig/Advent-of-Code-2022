import matplotlib.pyplot as plt

class Segment:
    child = None
    parent = None

    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def add_child(self, child):
        self.child = child
        self.child.parent = self

    def update(self):
        delta_x = self.pos_x - self.parent.pos_x
        delta_y = self.pos_y - self.parent.pos_y
        if abs(delta_x) > 1 or abs(delta_y) > 1:
            if abs(delta_x) > 0 and abs(delta_y) > 0:
                if delta_x < 0:
                    self.pos_x += 1
                if delta_x > 0:
                    self.pos_x -= 1
                if delta_y < 0:
                    self.pos_y += 1
                if delta_y > 0:
                    self.pos_y -= 1
            elif delta_x < 0:
                self.pos_x += 1
            elif delta_x > 0:
                self.pos_x -= 1
            elif delta_y < 0:
                self.pos_y += 1
            elif delta_y > 0:
                self.pos_y -= 1
            
            if self.child:
                self.child.update()
                
    
    def move(self, direction):
        if direction == "R":
            self.pos_x += 1
        elif direction == "L":
            self.pos_x -= 1
        elif direction == "U":
            self.pos_y += 1
        elif direction == "D":
            self.pos_y -= 1
        if self.child:
            self.child.update()


if __name__ == "__main__":
    data = open('data/data_12_09.txt', 'r').read().split('\n')
    
    h = Segment(0,0)
    s1 = Segment(0,0)
    s2 = Segment(0,0)
    s3 = Segment(0,0)
    s4 = Segment(0,0)
    s5 = Segment(0,0)
    s6 = Segment(0,0)
    s7 = Segment(0,0)
    s8 = Segment(0,0)
    s9 = Segment(0,0)
    
    h.add_child(s1)
    s1.add_child(s2)
    s2.add_child(s3)
    s3.add_child(s4)
    s4.add_child(s5)
    s5.add_child(s6)
    s6.add_child(s7)
    s7.add_child(s8)
    s8.add_child(s9)

    coord_list = [(0,0)]
    
    for x in data:
        x_split = x.split(" ")
        direction = x_split[0]
        dist = x_split[1]

        for i in range(int(dist)):
            h.move(direction)
            coord_list.append((s9.pos_x, s9.pos_y))

            #plt.scatter([h.pos_x, s1.pos_x, s2.pos_x, s3.pos_x, s4.pos_x, s5.pos_x, s6.pos_x, s7.pos_x, s8.pos_x, s9.pos_x], 
            #[h.pos_y, s1.pos_y, s2.pos_y, s3.pos_y, s4.pos_y, s5.pos_y, s6.pos_y, s7.pos_y, s8.pos_y, s9.pos_y])
            #plt.xlim(-15, 15)
            #plt.ylim(-15, 15)
            #plt.show()

    print(len(set(coord_list)))

