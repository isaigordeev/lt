from typing import Dict

# using levenstein from leetcode 72
# possible to implement 1 module distance diff func but lazy

from lt72 import minDistance


def create_graph(wordList):
    dict_ = {word: i for i, word in enumerate(wordList)}
    graph_ = {i: set() for i in range(len(wordList))}

    for word_1 in wordList:
        for word_2 in wordList:
            if minDistance(word_1, word_2) == 1:
                graph_[dict_[word_1]].add(dict_[word_2])
                graph_[dict_[word_2]].add(dict_[word_1])

    print(graph_)
    return graph_


def traverse_graph(graph_: Dict[int, set]):
    union_find_ = [i for i in range(len(wordList))]

    start_idx = wordList.index(beginWord)
    end_idx = wordList.index(endWord)

    all_nodes = set(range(len(wordList)))

    visited = set()

    found = False

    list_ = [start_idx]

    steps_ = 0

    while visited != all_nodes:
        curr_node = list_.pop()

        neighbors = graph_[curr_node]

        visited.add(curr_node)

        for n_ in neighbors:
            if n_ not in visited:
                if n_ == end_idx:
                    return steps_
                list_.append(n_)

        steps_ += 1
    print(steps_)
    return steps_ + 1


# 0 1 2 3 4 5
# 1 1 2 1 3 3

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"

    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    if beginWord not in wordList:
        wordList = [beginWord, *wordList]

    graph_ = create_graph(wordList)
    traverse_graph(graph_)


