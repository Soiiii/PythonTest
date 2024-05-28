# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest
# substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # Initialize variables
        aa = []
        max_length = 0
        start = 0

        for i in range(len(s)):
            if s[i] in aa:
                # Remove characters from the start up to the repeated character
                while s[start] != s[i]:
                    aa.remove(s[start])
                    start += 1
                # Move start one step forward to exclude the repeated character
                start += 1
            else:
                aa.append(s[i])
                # Update the max length if current length is greater
                max_length = max(max_length, len(aa))

        return max_length

        # class Solution:
        #     def lengthOfLongestSubstring(self, s: str) -> int:
        #         char_index = {}
        #         start = 0
        #         max_length = 0

        #         for end in range(len(s)):
        #             if s[end] in char_index:
        #                 # Update the start to be one more than the last index of the repeated character
        #                 start = max(start, char_index[s[end]] + 1)

        #             # Update the last index of the character
        #             char_index[s[end]] = end
        #             # Calculate the current length of the substring
        #             max_length = max(max_length, end - start + 1)

        return max_length


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         aa = []
#         bb = []
#         answer = 0
#         if len(s) == 0:
#             return 0
#         elif s == ' ':
#             return 1
#         for i in range(len(s)):
#             # print(i, s[i])
#             # print('aa', aa)
#             if s[i] not in aa:
#                 # print('???', s[i])
#                 aa.append(s[i])
#                 # answer += s[i]
#             else:
#                 # print('!!!!', i )
#                 # print('answer', answer)
#                 bb.append(answer)
#                 answer = 0
#                 aa.clear()
#                 aa.append(s[i])
#             answer += 1
#         bb.sort(reverse=True)
#         return bb[0]