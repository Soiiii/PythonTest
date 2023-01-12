# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the hour out from the 'From '
# line by finding the time and then splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# /Users/baeksoyoung/Desktop/mbox.txt
name = input("Enter file:")
counts = dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line = line.split()
        line = line[5]
        line = line[:2]
        counts[line] = counts.get(line, 0) + 1
lst = list()
for value, count in counts.items():
    lst.append((value, count))
lst.sort()
for value,count in lst:
    print(value,count)
print(line, counts[line])

# tmp = list()
# for k,v in di.items():
#     newt = (v,k)
#     tmp.append(newt)
# tmp.sorted(tmp,reversed = True)
# print(tmp)