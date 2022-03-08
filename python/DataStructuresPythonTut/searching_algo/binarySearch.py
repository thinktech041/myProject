# this is a divide and coquer overrall technique
# in the binarySearch algorithim , the list must be ordered

def binary_search(a_list, item):

    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item: # checking for midpoint
            found = True

        elif item < a_list[midpoint]: # midpoint greater than item
            last = midpoint - 1
        else:                         # midpoint is less than item
            first = midpoint + 1
    return found
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))

# using the recursion technique

def binary_searchre(a_list, item):
    
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item: # checking for midpoint Validation 
            found = True

        elif item < a_list[midpoint]: # midpoint greater than item
            binary_searchre(a_list[:midpoint], item)
        else:                         # midpoint is less than item
            binary_searchre(a_list[midpoint+1:], item)
    return found 
