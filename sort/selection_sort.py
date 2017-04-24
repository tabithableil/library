def selection_sort(lst):
    """ selection sort: find the smallest element in the list and put it at the beginning. that's all brah

        best/average/worst-case behavior: O(n^2) """

    for i in xrange(len(lst)):
        min_idx = i
        for j in xrange(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

