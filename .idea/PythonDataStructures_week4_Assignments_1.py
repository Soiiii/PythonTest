# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
# the split() method. The program should build a list of words. For each word on each line check to see if the
# word is already in the list and if not append it to the list. When the program completes, sort and print the
# resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

#/Users/baeksoyoung/Desktop/mbox.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word: #word안에 element 루프는
        if element in lst: #lst 빈 리스트 안에 element 루프는?
            continue
        else:
            lst.append(element) #빈 리스트에 element 채워넣기
lst.sort()
print(lst)

