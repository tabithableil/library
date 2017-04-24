import heapq


def heap_sort(lst):
    """ heap sort: just build a heap and pop elements off. this way is handy because it's super fast + no recursion

        best/average/worst-case behavior: O(nlogn) """

    heap = []
    for i in lst:
        heapq.heappush(heap, i)
    for j in xrange(len(lst)):
        lst[j] = heapq.heappop(heap)

