def merge_sort(lst):
    """ merge sort: break up the list into sublists with only one element, then merge them back together in sorted 
        order. the merge step works by comparing sublists and appending the smallest element in either list to result

        best/average/worst-case behavior: O(nlogn) 
        space: O(n) for result list """

    if len(lst) < 2:
        return lst
    mid_point = len(lst) // 2
    left = merge_sort(lst[:mid_point])
    right = merge_sort(lst[mid_point:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

