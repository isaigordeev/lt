# Условие
#
# Дана строка s и словарь слов wordDict. Нужно вернуть true, если строку s можно разбить на последовательность одного или более слов из словаря, иначе false.

# отвратительное условие задачи :)


def mark_word(s: str, wordDict: list[str]):
    dict_ = {i: set() for i, letter in enumerate(s)}
    segs_ = {word_: i for i, word_ in enumerate(wordDict)}

    for word_ in wordDict:
        start_idx = s.find(word_)
        if start_idx != -1:
            for i_ in range(start_idx, start_idx + len(word_)):
                curr_seg_ = segs_[word_]
                dict_[i_].add(curr_seg_)

    return dict_, segs_

#|1111####
#|||||||||
#|####2222
#|#####333

def traverse_segments(dict_, segs_):

    list_ = list([(0, segm_) for segm_ in dict_[0]])

    while list_:
        curr_letter_idx_, curr_segm_ = list_.pop()
        shift_ = len(segs_[curr_segm_])
        new_letter_idx_ = shift_ + curr_letter_idx_

        if new_letter_idx_ == len(segs_) + 1:
            return True

        for segm_ in dict_[new_letter_idx_]:
            list_.append((shift_ + curr_letter_idx_, segm_))

    return False




if __name__ == "main.py":
    s = "leetcode"

    wordDict = ["leet", "code"]

    dict_, segs_ = mark_word(s, wordDict)
    print(traverse_segments(dict_, segs_))





