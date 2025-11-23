# LeetCode 200 - Number of Islands (Medium)
#
# Дана m x n 2D бинарная сетка grid, которая представляет карту из '1's (земля) и '0's (вода),
# верни количество островов.
#
# Остров окружен водой и формируется путем соединения соседних земель горизонтально или вертикально.
# Можно предположить, что все четыре края сетки окружены водой.
#
# Пример 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Пример 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# - m == grid.length
# - n == grid[i].length
# - 1 <= m, n <= 300
# - grid[i][j] is '0' or '1'


def create_uf(n):
    return [i for i in range(n)]


def find(uf, i):
    _curr = i
    while _curr != uf[i]:
        _curr = uf[i]

    return _curr


def union(uf, i, j):
    uf[i] = uf[j]


def search_for_union(grid, i, j):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for _move in moves:
        delta_i, delta_j = _move

        if i + delta_i < len(grid) and j + delta_j < len(grid[0]):
            group = grid[i + delta_i][j + delta_j]
        else:
            group = 0  # water outside the grid

    return group


def numIslands_uf(grid):
    m = len(grid)
    n = len(grid[0])

    _uf = create_uf(n * m)

    _visited = [False for _ in range(n * m)]

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i, _x in enumerate(grid):
        for j, _y in enumerate(_x):
            if grid[i][j] == 1:
                _cur_idx_uf = m * i + j
                print("cur", _cur_idx_uf)
                for _move in moves:
                    delta_i, delta_j = _move
                    if _visited[(i + delta_i) * m + j + delta_j]:
                        continue

                    if i + delta_i < len(grid) and j + delta_j < len(grid[0]):
                        _uf[(i + delta_i) * m + j + delta_j] = _cur_idx_uf

    return _uf
