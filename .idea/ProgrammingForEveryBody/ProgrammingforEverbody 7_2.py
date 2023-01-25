# Definite Loops
# Definite loops(for loops) have explicit iteration variables
# that change each time through a loop. These iteration
# variables move through the sequence or set.

class coursera7_2:
    for i in [5, 4, 3, 2, 1]:
        print(i)
    print('Blastoff!')

    friends=['Joseph', 'Glenn', 'Sally']
    for friend in friends:
        print('Happy New Year:', friend)
    print('Done!')
    # 5
    # 4
    # 3
    # 2
    # 1
    # Blastoff!
    # Happy New Year: Joseph
    # Happy New Year: Glenn
    # Happy New Year: Sally
    # Done!

class coursera7_3:
    #Finding the Largest Value
    #We make a variable that contains the largest value we have seen so far.
    #If the current number we are looking at is larger, it is the new
    #largest value we have seen so far.

    largest_so_far = -1
    print('Before', largest_so_far)
    for the_num in [9, 41, 12, 3, 74, 15]:
        if the_num > largest_so_far:
            largest_so_far = the_num
        print(largest_so_far, the_num)
    print('After', largest_so_far)
    # 9 9
    # 41 41
    # 41 12
    # 41 3
    # 74 74
    # 74 15
    # After 74
