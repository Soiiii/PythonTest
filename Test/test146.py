# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        listA = list(str(x))
        if len(listA) == 0 or x == 0:
            return 0
        while(listA[0] == '0' or listA[-1] == '0'):
            if listA[0] == '0':
                listA.pop(0)
            elif listA[-1] == '0':
                listA.pop(-1)
        listA.reverse()
        if '-' in listA:
            listA.pop(listA.index('-'))
            listA.insert(0, '-')
        answer = int(''.join(listA))
        if answer > 2 ** 31 or answer < - (2 ** 31):
            return 0
        return answer