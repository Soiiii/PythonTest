# Zigzag Conversion
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        listA = []
        for i in s:
            listA.append(i)
        num = (numRows - 1) * 2
        answer = ' '.join[listA[:numRows]]
        print(listA[num])
