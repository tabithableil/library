def counting_sort(lst):
    """ counting sort: creates a histogram of the number of times each value occurs in the list, then loops over
        the histogram and adds each value*number of times it occurred to an output list

        best/average/worse-case behavior: O(n+k) where n=len(lst) and k=range of possible values 
        space: O(n+k) for histogram and output """

    counter = [0] * (max(lst) + 1)
    results = []
    for val in lst:
        counter[val] += 1
    for value, count in enumerate(counter):
        results.extend([value]*count)
    return results

