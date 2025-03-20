from collections import deque

grid = [[1, 1, 1],[0, 1, 1],[1, 1, 0],[0, 1, 1]]

def dfs(grid, start):
    row = len(grid)
    col = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    parent = {}
    visited.add(start)
    parent[start] = None

    def solve(grid, start, visited, parent, row, col):
        x, y = start
        if (x, y) == (row-1, col-1):
            return True
        for i, j in directions:
            nx, ny = x + i, y + j
            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                if solve(grid, (nx, ny), visited, parent, row, col):
                    return True
        return False

    if solve(grid, start, visited, parent, row, col):
        path = []
        i = (row-1, col-1)
        while i is not None:
            path.append(i)
            i = parent[i]
        path.reverse()
        print(path)
    else:
        print("No path")
start = (0, 0)
dfs(grid, start)

































# from collections import deque
# grid = [[1 ,1 ,1],[0 , 1 ,1],[1 , 1, 0],[0 , 1 ,1]]

# def bfs(grid , start):
    
#     row = len(grid)
#     col = len(grid[0])

#     directions = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)] 

    # q = deque()

    # visited = []
    
    # parent = {} 

    # q.append(start)
    # visited.append(start)
    # parent[start] = None

#     while q:
#         x , y = q.popleft()

#         if (x , y) == (row-1 ,col-1):
#             break

#         for i , j in directions:
#             nx , ny = x+i , y+j

#             if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1 and (nx , ny) not in visited:
#                 visited.append((nx , ny))
#                 q.append((nx , ny))
#                 parent[(nx , ny)] = (x , y)

#     path = []
#     curr = (row-1 , col-1)
#     path.append(curr)
#     while(curr is not None):
#         curr = parent[curr]
#         path.append(curr)
#     path.reverse()
#     print(path)

# bfs(grid , (0 , 0))