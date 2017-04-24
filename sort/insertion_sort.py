def insertion_sort(lst):
    """ insertion sort: compare all the elements previous to the newly 'inserted' element. if the new element is smaller,
        then 'shift' the previous element(s) forward in the list until the end of the list is reached or a position is
        found where the element to the left is smaller than the new element. 'shifting' the element forward works by
        just assigning the same value to the position ahead of it

        best-case behavior: O(n), average/worst-case behavior: O(n^2) """

    for i in xrange(1, len(lst)):
        j = i - 1
        key = lst[i]
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key


