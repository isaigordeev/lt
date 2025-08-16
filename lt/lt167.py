numbers = [2,7,11,15]
target = 9

def find(numbers: list[int], target: int):
    for num_1 in numbers:
        for num_2 in numbers:
            if num_1 + num_2 == target:
                return num_1, num_2


print(find(numbers, target))

def ef_find(numbers: list[int], target: int):
    
    dict_ = dict()
    for i, num_ in enumerate(numbers):
        if num_ not in dict_.keys():
            dict_[target-num_] = num_
        else:
            return num_, target-num_

print(ef_find(numbers, target))

