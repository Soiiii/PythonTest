# Ponketmon
#
# Suppose that you arrive at Dr. Hong's lab at the end of a long journey to catch ponketmon. Dr. Hong allows you to take "N"/2 ponketmons among "N" ponketmons in his lab.
# Ponketmons in Dr. Hong's lab are identified by a number given based on its type. Therefore, ponketmons with the same type have the same number. For example,
# if there are 4 ponketmons in the lab, and the type number of each ponketmon is [number 3, number 1, number 2, number 3], this represents that there are two ponketmons of number 3,
# one ponketmon of number 1, and one ponketmon of number 2.
# At this point, there are 6 ways to select two ponketmons among the four ponketmons as follows.
def solution(nums):
    answer = 0
    ll = set()
    for i in nums:
        ll.add(i)
    answer = len(ll)
    if answer > (len(nums)//2):
        return len(nums)//2
    return answer