# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                print('top_element', top_element)
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
        # answer = list(s)
        # c = []
        # b = { '[' : ']', '{' : '}', '(':')'}
        # for i in list(s):
        # print('i',i,'b',b.get(i))
        # if i in b:
        # c.append(i)
        # if b.get(i) != None:
        #     c.append(i)
        # print(c)