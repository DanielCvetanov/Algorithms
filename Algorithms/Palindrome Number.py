def isPalindrome(number: int) -> bool:
    if (number < 0):
      return False
    return str(number) == str(number)[::-1]

print(isPalindrome(123321))

# def isPalindrome(x):
#     string_number = str(x)
#     i = -1
#     j = 0
#
#     while i >= -len(string_number):
#         if string_number[i] != string_number[j]:
#             return False
#         i -= 1
#         j += 1
#
#     return True
#
# print(isPalindrome(121))

# def isPalindormeNumber(number):
#     string_number = str(number)
#
#     i = 0
#     for i in range(len(string_number) - 1):
#         if string_number[i] != string_number[len(string_number) - (i + 1)]:
#             return False
#
#     return True
#
# print(isPalindormeNumber())