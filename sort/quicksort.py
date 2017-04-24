def partition(lst, start, end):
    """ quick sort: pick a pivot and order the list by what's less than/greater than the pivot. elements that are less 
        than are kept to the left, greater than is kep to the right. keep track of the divide between the two with a
        wall index, which increases to the element after the last less than swap was executed. finally, move the pivot
        to it's correct position between the two. then we can keep going through each sublist around the pivot until sorted

        best/average-case behavior: O(nlogn), worst-case behavior: O(n^2) """

    pivot = lst[end]
    wall_idx = start    # border between less than and greater than the pivot
    if start < end:
        for i in xrange(start, end):
            if lst[i] <= pivot:
                lst[i], lst[wall_idx] = lst[wall_idx], lst[i]
                wall_idx += 1
        lst[end], lst[wall_idx] = lst[wall_idx], lst[end]
    return wall_idx


def quick_sort(lst, start, end):
    if start < end:
        split = partition(lst, start, end)
        quick_sort(lst, start, split-1)
        quick_sort(lst, split+1, end)
    else:
        return

