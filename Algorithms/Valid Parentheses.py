def isValid(string: str)-> bool:
    if len(string) // 2 != 0 or len(string) == 0 or string[0] == "}" or string[0] == "]" or string[0] == ")": return False

    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):



print(isValid("AAA"))

