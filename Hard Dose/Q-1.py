from collections import deque

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def shortest_path(grid, start, end):
    R, C = len(grid), len(grid[0])
    visited = [[False for _ in range(C)] for _ in range(R)]

    # Directions: up, down, right, left
    dr = [-1, +1, 0, 0]
    dc = [0, 0, +1, -1]

    rq = deque()
    cq = deque()

    sr, sc = start
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    reached_end = False

    while rq:
        r = rq.popleft()
        c = cq.popleft()

        if (r, c) == end:
            reached_end = True
            break

        # Explore neighbors
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if rr < 0 or cc < 0 or rr >= R or cc >= C:
                continue
            if visited[rr][cc]:
                continue
            if grid[rr][cc] == '#':
                continue

            rq.append(rr)
            cq.append(cc)
            visited[rr][cc] = True
            nodes_in_next_layer += 1

        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    return move_count if reached_end else -1

# === MAIN ===
grid = read_grid_from_file("log.txt")
start = (0, 0)
end = (10, 10)
result = shortest_path(grid, start, end)
print("Shortest path from (0,0) to (10,10):", result)
