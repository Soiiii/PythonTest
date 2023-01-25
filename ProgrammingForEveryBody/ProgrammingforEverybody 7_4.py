
class coursera7_4:
    #Loop Idioms
    #To count how many times we execute a loop, we introduce a counter variable
    #that starts at 0 and we add one to it each time through the loop
    zork = 0
    print('Before', zork)
    for thing in [9, 41, 12, 3, 74, 15]:
        zork = zork + 1
        print(zork, thing)
    print('After', zork)
    # Before 0
    # 1 9
    # 2 41
    # 3 12
    # 4 3
    # 5 74
    # 6 15
    # After 6

    #Summing in a Loop
    # To add up a value we encounter in a loop, we introduce a sum variable that
    #starts at 0 and we add the value to the sum each time through the loop.
    zork = 0
    print('Before', zork)
    for thing in [9, 41, 12, 3, 74, 15]:
        zork = zork + thing
        print(zork, thing)
    print('After', zork)
    # Before 0
    # 9 9
    # 50 41
    # 62 12
    # 65 3
    # 139 74
    # 154 15
    # After 154

#Finding the Average in a Loop
    count = 0
    sum = 0
    print('Before', count, sum)
    for value in [9, 41, 12, 3, 74, 15]:
        count = count + 1
        sum = sum + value
        print(count, sum, value)
    print('After', count, sum, sum / count)

    # Before 0 0
    # 1 9 9
    # 2 50 41
    # 3 62 12
    # 4 65 3
    # 5 139 74
    # 6 154 15
    # After 6 154 25.666666666666668

    #Search Using a Boolean Variable
    #If we just want to search and know if a value was found, we use a variable that
    #starts af False and is set to Ture as soon as we find what we are looking for.

    found = False
    print('Before', found)
    for value in [9, 41, 12, 3, 74, 15]:
        if value == 3:
            found = True
        print(found, value)
    print('After', found)
    # Before False
    # False 9
    # False 41
    # False 12
    # True 3
    # True 74
    # True 15
    # After True

    #How to find the Smallest Value

    smallest = None
    print('Before')
    for value in [9, 41, 12, 3, 74, 15]:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
        print(smallest, value)
    print('After', smallest)
    # Before
    # 9 9
    # 9 41
    # 9 12
    # 3 3
    # 3 74
    # 3 15
    # After 3