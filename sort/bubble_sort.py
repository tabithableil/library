def bubble_sort(lst):
    """ bubble sort: loops through the list and compares each pair of adjacent items and swaps them if they're
        in the wrong order. at each pass, the largest element "bubbles" up to the top of the list. the inner
        loop traverses the list and does the comparison work while the outer loop forces the inner loops to repeat

        best/average/worse-case behavior: O(n^2) """

    for i in xrange(len(lst)):
        for j in xrange(len(lst)-1-i):  # don't loop through sorted elements
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

