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


class UnionFind:
    def __init__(self, grid):
        # suppose valid
        self.N = len(grid)
        self.M = len(grid[0])

        self.create_uf()

    @staticmethod
    def find(uf, i):
        _curr = i
        while _curr != uf[i]:
            _curr = uf[i]

        return _curr

    @staticmethod
    def union(uf, i, j):
        uf[i] = uf[j]

    def idx(self, i, j):
        return i * self.M + j

    def create_uf(self):
        self.uf = [i for i in range(self.N * self.M)]

        return self.uf

    def print_(self):
        for i in range(self.N):
            print(self.uf[self.M * i : self.M * (i + 1)])


def search_for_group(grid, i, j, uf) -> int:
    n = len(grid)
    m = len(grid[0])

    _group = i * m + j

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for _move in moves:
        delta_i, delta_j = _move

        if i + delta_i < len(grid) and j + delta_j < len(grid[0]):  # borders
            if grid[i + delta_i][j + delta_j] == 1:  # if island
                _group = min(_group, uf[(i + delta_i) * m + j + delta_j])

    return _group


def numIslands_uf(grid):
    n = len(grid)
    m = len(grid[0])

    _uf = UnionFind(grid=grid)

    _visited = [False for _ in range(n * m)]

    for i, _x in enumerate(grid):
        for j, _y in enumerate(_x):
            if grid[i][j] == 1:
                _group = search_for_group(grid, i, j, _uf.uf)
                _uf.uf[_uf.idx(i, j)] = _group
            else:  #  water
                _uf.uf[_uf.idx(i, j)] = -1

    return _uf


# 0 1 2 3 4
# 5 6 7 8 9
