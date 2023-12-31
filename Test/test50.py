# Adding Ciphers
# Given a natural number N as the parameter, write a function solution to return the sum of each digit of N.
# For example, if N = 123, return 1 + 2 + 3 = 6.
# Constraints
# Range of N : natural number less than or equal to 100,000,000.

def sum_digit(number):
    return sum([int(i) for i in str(number)])
print(sum_digit(123))

# def solution(n):
#     answer = 0
#     list = []
#     for i in str(n):
#         list.append(i)
#     for j in list:
#         answer += int(j)
#     return answer
