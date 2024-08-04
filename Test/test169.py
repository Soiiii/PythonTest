# 4sum
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        length = len(nums)

        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for i
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for j
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # Skip duplicates for left
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # Skip duplicates for right
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return results
