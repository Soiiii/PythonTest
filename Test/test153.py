# 27. Remove Element

# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(val in nums):
            if val in nums:
                nums.pop(nums.index(val))
