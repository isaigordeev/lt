"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

word2 = "zoologicoarchaeologist"
word1 = "zoogeologist"

# letter by letter changes
# # horse
# r 11011
# o 10111
# s 11101


# actions are I D R

# word by word changes
# # horse
# r 12234
# o 21234
# s 32223


def minDistance(word1: str, word2: str) -> int:
    if len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)
    elif len(word1) == len(word2) and len(word2) == 0:
        return 0

    def edit(word1, word2):
        match_matrix_ = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        match_matrix_[0][0] = 0

        for i in range(len(word1) + 1):
            match_matrix_[i][0] = i
        for j in range(len(word2) + 1):
            match_matrix_[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                letter_i = word1[i - 1]
                letter_j = word2[j - 1]

                if letter_j != letter_i:
                    cost = 1
                else:
                    cost = 0

                match_matrix_[i][j] = min(match_matrix_[i - 1][j - 1] + cost, match_matrix_[i - 1][j] + 1,
                                          match_matrix_[i][j - 1] + 1)
        # print(match_matrix_)
        return match_matrix_

    return edit(word1, word2)[-1][-1]

if __name__ == "__main__":

    print(minDistance(word1, word2))