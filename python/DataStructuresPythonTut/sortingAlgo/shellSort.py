# The shell sort, sometimes called the “diminishing increment sort,”
# improves on the insertion sort
# by breaking the original list into a number of smaller sublists, 
# each of which is sorted usingan insertion sort. 
# The unique way that these sublists are chosen is the key to the shell sort.
# Instead of breaking the list into sublists of contiguous items,
# the shell sort uses an increment i,
# sometimes called the gap, 
# to create a sublist by choosing all items that are i items apart


#-------------------------------------------------------------------#

# We said earlier that the way in which the increments are chosen
# is the unique feature of the shell sort. 
# The function shell_sort shown below uses a different set of increments. 
# In this case, we begin with 𝑛/2 sublists.

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = I
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
            

