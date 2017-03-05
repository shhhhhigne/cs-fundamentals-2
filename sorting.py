#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # bubble = lst[0]

    # print lst
    for i in range(len(lst) ):
        for j in range( len(lst)-1, i, -1):
            if lst[j] < lst[j-1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp

    return lst



def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    lst = []
    i = 0
    j = 0
    while True:
        # for i in xrange()
        try:
            item1 = list1[i]
        except IndexError:
            lst.extend(list2[j:])
            return lst
        try:
            item2 = list2[j]
        except IndexError:
            lst.extend(list1[i:])
            return lst
            
        # elif list2 == []:
        #     lst.extend(list1)
        #     return lst
        # item1 = 
        # item2 = list2[j]
        if item1 < item2:
            lst.append(item1)
            i = i+1
            continue
        else:
            lst.append(item2)
            j = j+1



    # pass

# def merge(item1, item2):



##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) < 2:
        return lst

    middle = int(len(lst) / 2)  # index at half the list
    list1 = merge_sort(lst[:middle])  # divide list in half
    list2 = merge_sort(lst[middle:])  # assign other half

    return merge_lists(list1, list2)




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
