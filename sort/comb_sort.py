def comb_sort(lst):
    """ comb sort: improved bubble sort. instead of comparing elements that are directly beside each other, create a 
        gap between them. this helps when there are small values towards the end of the list, known as 'turtles.' at
        each pass, the gap shrinks until it equals 1, where it will act like bubble sort

        best-case behavior: O(nlogn), average/worst-case behavior: O(n^2) """

    gap = len(lst)
    shrink = 1.3    # ideal shrink factor specified in article
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap/shrink)
        if gap == 9 or gap == 10:   # rule of 11
            gap = 11
        swapped = False
        for i in xrange(0, len(lst)-gap):
            if lst[i] > lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
                swapped = True

