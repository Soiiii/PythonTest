# 직사각형 별찍기
#
# ※ Use Standrad input and output to solve this challenge
# Print a n by m grid of asterisks.
# Constrratins
# The first line contains 2-separated integers, n and m.
# 1 ≤ n, m ≤ 1,000

a, b = map(int, input().strip().split(' '))
print((('*' * a) + '\n') * b)