import numpy as np 
import matplotlib.animation as animation 
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
import matplotlib.cm as cm 
import random 

# Define a function to simulate the sex distribution of lanternfish larvae
def simulate_population(height, width, thresholds, iterations):

    grid = np.random.choice([0, 1, 2], size=(height, width), p=[0.5, 0.265, 0.235])
    population = [grid]
    # Iterate to update the state
    for i in range(iterations):
        new_grid = update_cell(grid, thresholds)
        population.append(new_grid)
        grid = new_grid
    return population

# Define a function to update the state of the lanternfish larvae according to the thresholds
def update_cell(grid, thresholds):
    height, width = grid.shape 

def sim_population(height,width,thresholds,iterations):
    grid = np.random.choice([0,1,2],size=(height,width),p=[0.5,0.25,0.25])
    population = [grid]

    for i in range(iterations):
        new_grid = update_cell(grid,thresholds)
        population.append(new_grid)
        grid = new_grid
    return population
def update_cell(grid, thresholds):
    height,width = grid.shape 
    new_grid = np.copy(grid)

    for i in range(height):
        for j in range(width):
            cell = grid[i,j]
            if cell == 0:
                if np.sum(grid[max(i-1,0):min(i+2,height),max(j-1,0):min(j+2,height),] == 1) >= thresholds[cell]:
                    new_grid[i,j] = random.choice([1, 2]) # 随机选择1或2
            elif cell ==1:
                if np.sum(grid[max(i-1,0):min(i+2,height),max(j-1,0):min(j+2,height),] == 1) >= thresholds[cell]:
                    new_grid[i,j] = 2
            elif cell ==2:
                if np.sum(grid[max(i-1,0):min(i+3,height),max(j-1,0):min(j+3,height),] == 1) >= thresholds[cell]:
                    new_grid[i,j] = 1
    # 在这里调用 check_color_ratio 函数
    new_grid = check_color_ratio(new_grid)
    return new_grid 

# 定义一个新的函数，用来检查红色和蓝色格子的总数是否达到80%或以上
def check_color_ratio(grid):
    height,width = grid.shape
    total_cells = height * width
    red_cells = np.sum(grid == 1)
    blue_cells = np.sum(grid == 2)
    color_ratio = (red_cells + blue_cells) / total_cells
    # 如果颜色比例大于等于0.8，就调用 change_color 函数
    if color_ratio >= 0.8:
        grid = change_color(grid)
    return grid

# 定义一个新的函数，用来根据规则改变格子的颜色
def change_color(grid):
    height,width = grid.shape
    new_grid = np.copy(grid)
    for i in range(height):
        for j in range(width):
            cell = grid[i,j]
            # 如果是红色格子，且周围没有三个格子，就变为白色格子
            if cell == 1:
                if np.sum(grid[max(i-1,0):min(i+2,height),max(j-1,0):min(j+2,width),] != 0) < 3:
                    new_grid[i,j] = 0
                    # 有10%的概率变成黑色格子
                    if random.random() < 0.8:
                        new_grid[i,j] = 3
            # 如果是蓝色格子，且周围没有两个白色格子，就变为白色格子
            elif cell == 2:
                if np.sum(grid[max(i-1,0):min(i+2,height),max(j-1,0):min(j+2,width),] == 0) < 7:
                    new_grid[i,j] = 0
                    # 有20%的概率变成黑色格子
                    if random.random() < 0.8:
                        new_grid[i,j] = 3
    return new_grid

def plot_population(population):
    mycolor_0=(246/255,235/255,20/255)
    mycolor_1=(125/255,20/255,21/255)
    mycolor_2=(67/255,120/255,188/255)
    cmap = colors.ListedColormap(['white',mycolor_1,mycolor_2,'black'])
    bounds = [0,1,2,3,4]
    norm = colors.BoundaryNorm(bounds,cmap.N)
    fig, ax = plt.subplots()
    ax.imshow(population[0],cmap=cmap,norm=norm)
    # 在这里修改文本框的位置和颜色
    text = ax.text(0.5, 1.05, '', transform=ax.transAxes, color='black', fontsize=12, ha='center', va='bottom')

    def update(frame):
        ax.imshow(population[frame],cmap = cmap,norm=norm)
        # 在这里计算和更新百分比
        grid = population[frame]
        height,width = grid.shape
        total_cells = height * width
        red_cells = np.sum(grid == 1)
        blue_cells = np.sum(grid == 2)
        black_cell = np.sum(grid == 3)
        red_ratio = red_cells / total_cells
        blue_ratio = blue_cells / total_cells
        black_ratio = black_cell / total_cells
        text.set_text(f'Red: {red_ratio:.2%}, Blue: {blue_ratio:.2%},balck:{black_ratio:.2%}')

    ani = animation.FuncAnimation(fig,update,frames=len(population),interval=200)
    plt.show()
height = 100
width = 100
thresholds = [5,5,5]
iterations = 45
population = sim_population(height,width,thresholds,iterations)
plot_population(population)