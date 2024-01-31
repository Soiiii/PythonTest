# Elimination by Grouping
# Elimination by grouping starts with a string consisting of lower-case letters.
# First, find a pair of two identical letters placed consecutively.
# Eliminate the pair, then concatenate the split strings.
# Elimination by grouping ends when all strings are eliminated by repeatedly
# doing this procedure. Given a string "S", write a function solution to return
# whether elimination by grouping can be successfully done or not. Return 1 for success and 0 otherwise.
# For example, when string "S" = baabaa, return 1 because all strings can be eliminated as follows:
# b aa baa → bb aa → aa →
def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0

# Example usage:
result = solution("baabaa")
print(result)
