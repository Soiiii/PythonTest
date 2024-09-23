# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers
# without using multiplication, division, and mod operator.
#
# The integer division should truncate toward zero,
# which means losing its fractional part. For example, 8.345 would be truncated to 8,
# and -2.7335 would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.





class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num = 0
        target = 0
        if dividend == 0:
            return 0
        elif abs(dividend) == 1:
            if abs(dividend) >= abs(divisor):
                if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
                    return -1
                elif (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
                    return 1
            else:
                return 0
        while(abs(dividend) > target):
            num += 1
            target += abs(divisor)
            if abs(dividend) < (target + abs(divisor)):
                if divisor < 0:
                    return -num
                else:
                    return num
            elif abs(dividend) < target:
                return dividend
