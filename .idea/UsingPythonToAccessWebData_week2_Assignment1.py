# Finding Numbers in a Haystack
#
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
# in the file and compute the sum of the numbers.
#
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
# other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1688964.txt (There are 71 values and the sum ends with 27)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python
# program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for
# analysis.
# Data Format
# The file contains much of the text from the introduction of the textbook except that random numbers are inserted
# throughout the text. Here is a sample of the output you might see:
# The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of
# numbers in each line (including none).
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
# regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.




#/Users/baeksoyoung/Desktop/regex_sum_42.txt
import re

hand = open('/Users/baeksoyoung/Desktop/regex_sum_1688964.txt')
b = list()
c = list()
for line in hand:
    a = re.findall('[0-9]+',line)
    b.extend(a)
    #c.append(a)
print(b)
# list.extend를 하면 리스트 대괄호안에 바로 들어감
# ['8232', '1827', '434', '8172', '4010', '5867', '8312', '7055', '8000', '2173', '8081', '2498', '9197', '5392', '702', '723', '5574', '2262', '9192', '4229', '7953', '2319', '9430', '1258', '3991', '9472', '8910', '3019', '380', '4837', '378', '9580', '7115', '4369', '5921', '1743', '2134', '7306', '3830', '269', '4', '4956', '9869', '6516', '2850', '5676', '1745', '4617', '9397', '7570', '4285', '7961', '6966', '2639', '1047', '4456', '3985', '5175', '9703', '9734', '6429', '9101', '8145', '6845', '941', '9295', '4200', '1725', '4', '3', '42']
#print(c)
#list.append를 하면 대괄호속 대괄호가 그대로 들어감
#[[], [], [], [], [], [], [], [], [], [], ['8232', '1827', '434'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['8172', '4010'], ['5867'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['8312'], ['7055'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['8000', '2173', '8081'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['2498'], [], [], [], [], [], [], ['9197', '5392', '702'], [], ['723', '5574'], [], [], [], [], [], [], ['2262'], [], ['9192', '4229', '7953'], [], [], [], [], ['2319', '9430', '1258'], [], ['3991'], [], [], [], [], [], ['9472'], [], ['8910'], [], [], [], [], [], [], ['3019', '380', '4837'], [], [], [], [], [], [], [], [], [], [], [], [], [], ['378'], [], [], [], [], [], [], [], [], [], ['9580'], [], [], [], [], [], [], [], ['7115', '4369', '5921'], [], ['1743'], [], [], [], [], [], [], [], [], [], [], [], [], ['2134', '7306'], ['3830'], [], [], [], [], [], [], [], [], [], [], ['269'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['4'], [], [], [], [], [], [], [], [], [], [], [], ['4956', '9869'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['6516', '2850'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['5676'], [], [], [], [], [], [], [], [], ['1745', '4617', '9397'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['7570', '4285', '7961'], ['6966', '2639'], [], [], [], [], ['1047', '4456'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['3985', '5175', '9703'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['9734', '6429', '9101'], ['8145'], [], [], [], ['6845', '941', '9295'], ['4200'], [], [], [], [], ['1725'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['4', '3'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['42'], []]
s = [int(x) for x in b]
#String인 리스트를 int타입으로 바꿔준다
print(s)
#[8232, 1827, 434, 8172, 4010, 5867, 8312, 7055, 8000, 2173, 8081, 2498, 9197, 5392, 702, 723, 5574, 2262, 9192, 4229, 7953, 2319, 9430, 1258, 3991, 9472, 8910, 3019, 380, 4837, 378, 9580, 7115, 4369, 5921, 1743, 2134, 7306, 3830, 269, 4, 4956, 9869, 6516, 2850, 5676, 1745, 4617, 9397, 7570, 4285, 7961, 6966, 2639, 1047, 4456, 3985, 5175, 9703, 9734, 6429, 9101, 8145, 6845, 941, 9295, 4200, 1725, 4, 3, 42]
print(sum(s))
# To sum a list of numbers, use sum
# 352027
# print(sun)