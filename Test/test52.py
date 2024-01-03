# The Number of p and y in String
# Suppose that a string s consisting of both lower-case and upper-case
# letters are given. Write a function "solution" to return True when
# the number of 'p' and 'y' in s are the same, and return False otherwise.
# Note that when there is neither 'p' nor 'y', it should always return True.
# Also, when comparing the number of 'p' and 'y', lower-case and upper-case
# are not distinguished.
# For example, if s is "pPoooyY", then return true. In the case of "Pyy",
# return false.

def solution(s):
    a = list(s.lower())
    p=0
    y=0
    for num in a:
        if num == 'p':
            p += 1
        elif num == 'y':
            y += 1
    return p==y

print(solution("pPoooyY"))