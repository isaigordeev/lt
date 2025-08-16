import copy
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def dfs(node: Node) -> Node:
    visited = set()
    copied_node_ = Node(node.val)
    d_ = deque()
    d_.append(node)

    l_ = {node: Node(node.val)}

    while d_:
        current_node = d_.popleft()
        neighbours = getattr(current_node, "neighbors")

        visited.add(current_node)

        for n_ in neighbours:
            if n_ not in visited:
                copied_n_ = Node(n_.val)
                l_[n_] = copied_n_

                d_.append(n_)

                l_[current_node].neighbors.append(copied_n_)


    return l_[node]


if __name__ == "__main__":
    # создаём граф: 1 -- 2 -- 3 -- 4 -- 1 (квадрат)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned = dfs(node1)

    # проверим результат (у клона должны быть такие же соседи)
    print(cloned.val, [n.val for n in cloned.neighbors])
    print(cloned.neighbors[0].val, [n.val for n in cloned.neighbors[0].neighbors])





