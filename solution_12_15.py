import re
import itertools
import numpy as np
from random import randint
from scipy.optimize import minimize


def manhattan_dist(p1: tuple[int, int], p2: tuple[int, int]):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy

def get_cave_dimensions(pairs):
    x_vals = [[pair["sensor"][0], pair["beacon"][0]] for pair in pairs]
    x_vals = list(itertools.chain.from_iterable(x_vals))

    return (min(x_vals), max(x_vals))

def dist_to_sensors(p, pairs):
    total_dist = 0
    x, y = p
    for pair in pairs:
        d = manhattan_dist((x, y), pair["sensor"])
        if d <= pair["dist"]:
            total_dist += (pair["dist"] - d) + 1 
      
    return total_dist

def find_impossible_locations(pairs, target_row):
    coords_impossible = {}
    coords_blocked = {}

    for pair in pairs:
        x, y = pair["sensor"]
        x_beacon, y_beacon = pair["beacon"]
        d_pair = pair["dist"]

        scan_range = range(x-d_pair, x+d_pair)
        if y_beacon == target_row:
            coords_blocked[str(x_beacon)] = True
        
        for col in scan_range:
            d_cell = manhattan_dist((x, y), (col, target_row)) - 1
            col_str = str(col)
            if d_cell <= d_pair:
                if col_str not in coords_impossible and col_str not in coords_blocked:
                    coords_impossible[col_str] = True
        
    return(len(coords_impossible))

def find_global_optimum(pairs, n_iter):
    current_best = 10000000

    for _ in range(n_iter):
        p_init = np.array([randint(0, 4000000), randint(0,4000000)])
        global_optimum = minimize(dist_to_sensors, x0 = p_init, args = pairs, bounds = ((0,4000000), (0,4000000)))

        if global_optimum["fun"] == 0:
            x_opt = int(global_optimum["x"][0])
            y_opt = int(global_optimum["x"][1])
            tuning_freq = x_opt * 4000000 + y_opt
            if dist_to_sensors((x_opt, y_opt), pairs) == 0:
                print(f"Optimum: {tuning_freq} at x = {x_opt}, y = {y_opt}")
                return(tuning_freq) 
                
        if global_optimum["fun"] < current_best:
            current_best = global_optimum["fun"]
            print(current_best)   


if __name__ == "__main__":
    data = open('data/data_12_15.txt', 'r').read().split('\n')

    pairs = []
    for line in data:
        coords = re.findall(r"-?\d+", line)
        coords = [int(coord) for coord in coords]
        pair = {'sensor': (coords[0], coords[1]), 
                'beacon': (coords[2], coords[3]),
                'dist': manhattan_dist((coords[0], coords[1]), (coords[2], coords[3]))}
        pairs.append(pair)  

    # Part 1
    # print(find_impossible_locations(pairs, 2000000))
    
    # Part 2
    find_global_optimum(pairs, 10000000)
