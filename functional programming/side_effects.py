## States 
#   The state of a programme can be modifiable or immutable, depending on whether it can be changed or not during the program's execution.

y = [3, 2]
x = [2]
x = y

print(y)
print(x)

def my_cool_function(x, y):
    x[:] = y

y = [3, 2]
x = [2]
my_cool_function(x, y)

print(y)
print(x)


z = 3
def my_cool_function(x, y):
    global z
    x = y
    z = z + 1


y = [3, 2]
x = [2]
my_cool_function(x, y)

print(x)
print(y)
print(z)

# The examples above show the challenges of having a state that is constantly updated. Functional programming tries to avoid this. 

## Side effects and pure functions.
#   A pure function simply has no side effects. WHich function is pure?

def add_one(x):
    return x + 1

def say_hello(name):
    print('Hello', name)

def append_item_1(a_list, item):
    a_list += [item]
    return a_list

def append_item_2(a_list, item):
    result = a_list + [item]
    return result

add_one(5)
#Is pure - will always return the same answer with the same input
say_hello("Josh")
#Not pure as printing text is interacting with the outside world
a_list = [1,2,3]
list_1 = append_item_1(a_list, 4)
print(a_list)
print(list_1)
#Not pure as a list gets modified
list_2 = append_item_2(a_list, 5)
print(a_list)
print(list_2)
#Pure as a list does not get modified after being defined

## Conway's game of life
#   Conway's Game of Life is a popular cellular automaton that simulates the evolution of a two-dimensional grid of cells. In this exercise, you will refactor a Python program that implements Conway's Game of Life. The basic rules of the game of life are:
#       Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
#       Any live cell with two or three live neighbors lives on to the next generation.
#       Any live cell with more than three live neighbors dies, as if by overpopulation.
#       The code has a bug related to the improper management of the program state, which you will fix. Refactor the code so that the step function is a pure function.

#Buggy code:
import numpy as np

def step(grid):
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid, i, j)
            count = sum(neighbors)
            if grid[i, j] == 1:
                if count in [2, 3]:
                    grid[i, j] = 1
            elif count == 3:
                grid[i, j] = 1


def get_neighbors(grid, i, j):
    rows, cols = grid.shape
    indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),             (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)])
    valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
                    (indices[:, 1] >= 0) & (indices[:, 1] < cols)
    return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]

# Test
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]], dtype=np.int8)
step(grid)
print(grid)  # should be unchanged, but may change due to the bug

## We can fix the bug by creating a new grid to store the results of the step.
#  We can make the function pure by returning the new grid instead of modifying the input grid.

import numpy as np

def step(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=np.int8)
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid, i, j)
            count = np.sum(neighbors)
            if grid[i, j] == 1 and count in [2, 3]:
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and count == 3:
                new_grid[i, j] = 1
    return new_grid


def get_neighbors(grid, i, j):
    rows, cols = grid.shape
    indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),             (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)])
    valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
                    (indices[:, 1] >= 0) & (indices[:, 1] < cols)
    return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]

# Test
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]], dtype=np.int8)

new_grid = step(grid)
assert np.array_equal(new_grid, grid), "Grid should be unchanged"


## Functional programming has three main benefits:
#   Testability
#   Composability
#   Parallelisability


