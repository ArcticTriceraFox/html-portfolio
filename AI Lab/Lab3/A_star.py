import math
import heapq

ROW, COL = 9, 10
class Cell:
    def __init__(self):
        self.parent = (0, 0) 
        self.f = float('inf')  
        self.g = float('inf')  
        self.h = 0  
def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL

def is_unblocked(grid, row, col):
    return grid[row][col] == 1
def is_destination(row, col, dest):
    return (row, col) == dest
def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

def trace_path(cell_details, dest):
    path = []
    row, col = dest
    while (row, col) != cell_details[row][col].parent:
        path.append((row, col))
        row, col = cell_details[row][col].parent
    path.append((row, col))
    path.reverse()
    print("The Path is:", " -> ".join(map(str, path)))

# A* Search Algorithm
def a_star_search(grid, src, dest):
    if not is_valid(*src) or not is_valid(*dest):
        return print("Source or destination is invalid")
    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        return print("Source or destination is blocked")
    if is_destination(*src, dest):
        return print("We are already at the destination")

    # Initialize cell details and open list
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]
    i, j = src
    cell_details[i][j].f = cell_details[i][j].g = cell_details[i][j].h = 0
    cell_details[i][j].parent = (i, j)

    open_list = [(0.0, i, j)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while open_list:
        f, i, j = heapq.heappop(open_list)

        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]
            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j):
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i][new_j].parent = (i, j)
                    print("Destination found!")
                    trace_path(cell_details, dest)
                    return
                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent = (i, j)

    print("Failed to find the destination")

def main():
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]
    src = (8, 0)
    dest = (0, 0)
    a_star_search(grid, src, dest)

if __name__ == "__main__":
    main()