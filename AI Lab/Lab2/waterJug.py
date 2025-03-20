from collections import deque

def waterJub(a, b, target):
    visited = set()
    q = deque()

    q.append((0,0, 0))

    while q:
        x, y, steps= q.popleft()
        if x == target or y == target:
            print(f"Yes, did it in {steps} steps")
            return steps
        if (x , y) in visited:
            continue
        visited.add((x, y))

        q.append((a, y, steps + 1))
        q.append((x, b, steps + 1))
        q.append((0, y, steps + 1))
        q.append((x, 0, steps + 1))
        q.append((a, y - (a - x), steps + 1))
        q.append((x - (b - y), b, steps + 1))
        q.append((x + y, 0, steps + 1))
        q.append((0, x+ y, steps + 1))

    print("No solution")
    return False

a = 32
b = 19
target = 3
waterJub(a, b, target)
