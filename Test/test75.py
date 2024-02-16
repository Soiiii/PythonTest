# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]  # Assume the first string as the prefix

        # Iterate through each string starting from the second one
        for s in strs[1:]:
            # Keep shortening the prefix until it matches the beginning of the current string
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
