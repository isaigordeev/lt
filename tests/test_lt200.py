from lt.lt200 import numIslands_uf

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]


uf = numIslands_uf(grid)

print(uf)
