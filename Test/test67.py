# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = 0
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                answer = nums[i] + nums[j]
                if target == answer:
                    result.append(i)
                    result.append(j)
                    return result


def twoSum(nums, target):
    # for i,j in (range(0,len(nums)), range(1,len(nums))):
    #     print(i)
    answer = 0
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            answer = nums[i] + nums[j]
            if target == answer:
                result.append(i)
                result.append(j)
                return result
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))