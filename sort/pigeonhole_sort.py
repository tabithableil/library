def pigeonhole_sort(lst):
    """ pigeonhole sort: essentially like counting sort? might be wrong, can't find much info on this one
        supposedly this is better than counting sort because we only have to move twice, but if you remove
        that weird part of counting sort where you calculate indexes, you only move twice anyway? however,
        this one is in space and counting sort uses extra space. also O(n+k) """

    max_val, min_val = max(lst), min(lst)
    range_size = max_val - min_val + 1
    pigeonholes = [0] * range_size
    for i in lst:
        pigeonholes[i-min_val] += 1

    in_idx = 0
    for count in xrange(range_size):
        while pigeonholes[count]:
            lst[in_idx] = count + min_val
            pigeonholes[count] -= 1
            in_idx += 1

