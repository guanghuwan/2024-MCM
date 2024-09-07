import numpy as np 
import matplotlib.animation as animation 
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
import matplotlib.cm as cm 
import random 

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
    return new_grid 

def plot_population(population):
    cmap = colors.ListedColormap(['white','red','blue'])
    bounds = [0,1,2,3]
    norm = colors.BoundaryNorm(bounds,cmap.N)
    fig, ax = plt.subplots()
    ax.imshow(population[0],cmap=cmap,norm=norm)

    def update(frame):
        ax.imshow(population[frame],cmap = cmap,norm=norm)

    ani = animation.FuncAnimation(fig,update,frames=len(population),interval=200)
    plt.show()

height = 100
width = 100
thresholds = [5,5,5]
iterations = 45

population = sim_population(height,width,thresholds,iterations)


plot_population(population)