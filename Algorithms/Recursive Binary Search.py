def recursive_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_search(list[midpoint+1:],target)
            else:
                return recursive_search(list[:midpoint],target)

TheList = [1,2,3,4,5,6,7,8,9,10]
Target = 1

print(recursive_search(TheList,Target))