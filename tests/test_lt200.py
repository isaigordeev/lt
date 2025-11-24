from lt.lt200 import UnionFind, numIslands_dfs, numIslands_uf

# grid = [
#     [1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]


# uf: UnionFind = numIslands_uf(grid)
# uf.print_()

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]


uf: UnionFind = numIslands_uf(grid)
uf.print_()

print("islands uf: ", len(set(uf.uf)))

print("islands dfs: ", numIslands_dfs(grid))
