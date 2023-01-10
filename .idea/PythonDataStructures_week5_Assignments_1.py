# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the
# greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file. After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to find the most prolific committer.
# /Users/baeksoyoung/Desktop/mbox.txt

name = input("Enter file: ")
if len(name) < 1:
    open = "/Users/baeksoyoung/Desktop/mbox.txt"
handle= open(name)
dic = dict()
for aa in handle:
    if aa.startswith('From:'):
        continue
    if aa.startswith('From'):
        word = aa.rstrip()
        words = aa.split()
        words = words[1]
        dic[words] = dic.get(words,0) + 1
maxword = None
maxcount = None

for word, count in dic.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxword = word
print(maxword, maxcount)
