#The selection sort improves on the bubble sort by making only one exchange for every pass
#through the list. In order to do this,
#a selection sort looks for the largest value as it makes a
#pass and, after completing the pass, places it in the proper location.
# As with a bubble sort, after
#the first pass, the largest item is in the correct place. After the second pass,
#  the next largest is in place.

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
                temp = a_list[fill_slot]
                a_list[fill_slot] = a_list[pos_of_max]
                a_list[pos_of_max] = temp
  