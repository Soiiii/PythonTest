# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        listA = list(s)
        maps = {"(":")", "[":"]", "{":"}"}
        k = 0
        while((k < len(listA)//2)+1):
            if len(listA) == 1:
                return False
            print('k', k)
            print(listA[-1-k])
            print(maps.get(listA[k]))
            print(listA[-1-k] != maps.get(listA[k]))
            if k < 4 and listA[k+1] == maps.get(listA[k]):
                print('11')
                return True
            if k < 4 and listA[-1-k] == maps.get(listA[k]):
                print('22')
                return True
            if k < 4 and listA[k+1] != maps.get(listA[k]):
                print('33')
                return False
            if k < 4 and listA[-1-k] != maps.get(listA[k]):
                print('44')
                return False
            if listA[k+1] == maps.get(listA[k]):
                print('1')
                k += 2
            elif listA[-1-k] == maps.get(listA[k]):
                print('2')
                k += 1
            elif listA[k+1] != maps.get(listA[k]) or listA[-1-k] != maps.get(listA[k]):
                print('3')
                return False
        return True

        # for k,i in enumerate(listA):
        #     print('k', k, 'i', i)
        #     print(maps.get(i))
        #     if k < len(listA)-1:
        #         if listA[k+1] == maps.get(i) or listA[-1-k] == maps.get(i):
        #             print('!!!' )
        #             pass
        #         else:
        #             return False
        # return True