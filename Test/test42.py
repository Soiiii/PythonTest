# Calculating Insufficient Amount
# This new ride at an amusement park is very popular and runs nonstop.
# The original fee of this ride is price, but it is determined that when using the ride for the Nth time,
# the fee will increase as N times of the original fee. That is, if the original fee is 100,
# it will be 200 for the second time, and 300 for the third time.
# Write a function solution to return the insufficient money when the ride is used count times.
# However, return 0 when the owed amount is sufficient.

def solution(price, money, count):
    answer = -1
    sum = 0
    for i in range(count+1):
        sum += (price * i)
        if sum > money:
            answer = sum-money
        else:
            answer = 0
    return answer

solution(3,20,4)