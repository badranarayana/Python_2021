# return the
# longest
# palindromic
# substring in s.
#
# Example
# 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also
# a
# valid
# answer.
# Example
# 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example
# 3:
#
# Input: s = "a"
# Output: "a"
# Example
# 4:
#
# Input: s = "ac"
# Output: "a"

s = "bbqwertyaiou"
#Output: "bab"

lenth = len(s)


def find_langest_poli(s):
    if len(s) < 0:
        return None
    if s[::-1] == s:
       return s

    mid = len(s)//2
    if s[mid -1] == s[mid + 1]:
        return s[mid-1: mid +2]



print(find_langest_poli(s))



find_langest_poli(s)










