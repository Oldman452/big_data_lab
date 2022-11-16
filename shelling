import numpy as np
import matplotlib.pyplot as plt
import cell_happines_calc as mf


world_size = 100
num_for_happy = 2

def cell_happines(world, i, j, num_same_for_happiness):
    cur_happy = 0
    cur_cell_value = world[i, j]
    x, y = world.shape
    if j + 1 < y:
        if cur_cell_value == world[i, j + 1]:
            cur_happy += 1

    if j - 1 >= 0:
        if cur_cell_value == world[i, j - 1]:
            cur_happy += 1
    
    if (i + 1 < x) & (j - 1 >= 0):
        if cur_cell_value == world[i + 1, j - 1]:
            cur_happy += 1
    
    if i + 1 < x:
        if cur_cell_value == world[i + 1, j]:
            cur_happy += 1
    
    if (i + 1 < x) & (j + 1 < y):
        if cur_cell_value == world[i + 1, j + 1]:
            cur_happy += 1
    
    if (i - 1 >= 0) & (j - 1 >= 0):
        if cur_cell_value == world[i - 1, j - 1]:
            cur_happy += 1
    
    if (i - 1 >= 0) & (j + 1 < y):
        if cur_cell_value == world[i - 1, j + 1]:
            cur_happy += 1
    
    if i - 1 >= 0:
        if cur_cell_value == world[i - 1, j]:
            cur_happy += 1
    
    if cur_happy >= num_same_for_happiness: # Hitler's inequality
        return True
    return False


Color_map_flat = np.zeros((world_size**2))
num_elements = world_size ** 2
num_blue = round(num_elements * 0.45)
num_red = round(num_elements * 0.45)
Color_map_flat[0:num_blue] = -0.6  # blue
Color_map_flat[num_blue: num_red+num_blue] = 0.6 
np.random.shuffle(Color_map_flat)
Color_map = Color_map_flat.reshape((world_size, world_size))

fig, ax = plt.subplots()
happiness_map = np.zeros_like(Color_map)

for iteration in range 100:
    # Calculate happiness map    
    for i, _ in enumerate(happiness_map):
        for j, _ in enumerate(happiness_map[i]):
            happiness_map[i, j] = cell_happines(Color_map, i, j, num_for_happy)
    unhappy_x, unhappy_y = np.where((happiness_map == 0) & (Color_map != 0))
    empty_x, empty_y = np.where(Color_map == 0)
    
    if len(unhappy_x) != 0:
        unhappy_to_move_idx = np.random.randint(0, len(unhappy_x))
        empty_to_move_idx = np.random.randint(0, len(empty_x))
        Color_map[empty_x[empty_to_move_idx], empty_y[empty_to_move_idx]] =\
            Color_map[unhappy_x[unhappy_to_move_idx ], unhappy_y[unhappy_to_move_idx]]
        Color_map[unhappy_x[unhappy_to_move_idx ], unhappy_y[unhappy_to_move_idx]] = 0
        
        
        ax.cla()
        ax.set_title("Iteration {}".format(iteration + 1))
        plt.imshow(Color_map, cmap='bwr', vmin=-1, vmax=1)
        plt.pause(0.5)
    else:
        print("счастливых клеток не осталось после", iteration)
        print("No unhappy cells!!!")
        break
