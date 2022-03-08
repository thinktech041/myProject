# this algorithim goes through the items of a list one by one till
# it finds the item it looks for
# the list may or may not be Ordered
li = [1,2,4,3,5]


# IMPLEMENTATION

def sequSearch(Item_list, Item):
    # this function returns the position of the item 
    # if it is found 
    found = False
    pos = 0       # refrences the position
    while pos < len(Item_list) and not found:
        if Item_list[pos]==Item:
            found=True               
        else:
            pos+=1

    return found,pos+1   # thr poss+1 is the position of the item with 
                         #refrence to human view

print(sequSearch(li,3))


# for ordered sequential list 
# in ordered sequential search, the item is easy to find
# IMPLIMENTATION




def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:           
                stop = True
        else:
            pos = pos+1
    return found, pos+1
    
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))
      