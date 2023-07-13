""" Spiral Problem
Write a function that takes in a grid of numbers (as a list of lists), and outputs them as
a list in spiral order -- starting from the top left, in clockwise direction.
"""

grid1 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]
#
grid2 = [
    [1,  2,  3,  4],
    [10, 11, 12, 5],
    [9,  8,  7,  6],
]

grid3 = [
    [1,  2,  3,  4],
    [14, 15, 16, 5],
    [13, 20, 17, 6],
    [12, 19, 18, 7],
    [11, 10, 9,  8],
]

grid1 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]

output = [1,2,3,4,5,6,7,8,9]


def get_spiral(grid):
    if not grid:
        return []
    # return a path as a spiral
    result = []
    num_cols = len(grid[0])
    num_rows = len(grid)
    total_num = num_cols * num_rows
    curr_row = 0
    curr_col = 0
    direction = "right"
    visited = set()

    while total_num > 0:
        visited.add((curr_row, curr_col))
        result.append(grid[curr_row][curr_col])

        if direction == "right":
            if curr_col == num_cols - 1 or (curr_row, curr_col+1) in visited:
                new_r, new_c = mov_down(curr_row, curr_col)
                direction = "down"
            else:
                new_r, new_c = mov_right(curr_row, curr_col)
        elif direction == "down":
            if curr_row == num_rows - 1 or (curr_row + 1, curr_col) in visited:
                new_r, new_c  = mov_left(curr_row, curr_col)
                direction = "left"
            else:
                new_r, new_c = mov_down(curr_row, curr_col)
        elif direction == "left":
            if curr_col == 0 or (curr_row, curr_col - 1) in visited:
                new_r, new_c = mov_up(curr_row, curr_col)
                direction = "up"
            else:
                new_r, new_c = mov_left(curr_row, curr_col)
        else:
            if curr_row == 0 or (curr_row - 1, curr_col) in visited:
                new_r, new_c = mov_right(curr_row, curr_col)
                direction = "right"
            else:
                new_r, new_c = mov_up(curr_row, curr_col)

        print("row: " + str(curr_row) + " col: " + str(curr_col))
        print("next_row: " + str(new_r) + " next_col: " + str(new_c))
        curr_row = new_r
        curr_col = new_c
        total_num -= 1

    return result


def mov_right(curr_row, curr_col):
    curr_col += 1
    return curr_row, curr_col


def mov_left(curr_row, curr_col):
    curr_col -= 1
    return curr_row, curr_col


def mov_up(curr_row, curr_col):
    curr_row -= 1
    return curr_row, curr_col


def mov_down(curr_row, curr_col):
    curr_row += 1
    return curr_row, curr_col


print(get_spiral(grid1))
print(get_spiral(grid2))
print(get_spiral(grid3))
