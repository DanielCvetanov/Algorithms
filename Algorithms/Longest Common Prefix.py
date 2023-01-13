
# My approach
def longestCommonPrefix(strs) -> str:

    def findLongestPrefix(str1, str2) -> str:
        result = ""
        i = 0
        j = 0

        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                break

            result += str1[i]

            i += 1
            j += 1

        return result

    prefix = strs[0]

    for i in range(1, len(strs)):
        prefix = findLongestPrefix(prefix, strs[i])

    return (prefix)


# Using zip and unpacking
def longestCommonPrefix(strs: list) -> str:
    res = ""
    for a in zip(*strs):
        if len(set(a)) == 1:
            res += a[0]
        else:
            return res
    return res

print(longestCommonPrefix(["flower","flow","flight"]))