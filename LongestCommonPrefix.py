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
