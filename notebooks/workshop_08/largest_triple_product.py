import heapq


def find_max_product(arr):
    result = [-1 for x in arr]

    if len(result) < 3:
        return result

    heap = [x for x in arr[:2]]
    heapq.heapify(heap)

    for i, x in enumerate(arr[2:]):
        heapq.heappush(heap, x)
        if len(heap) > 3:
            heap = heap[1:]

        result[i + 2] = heap[0] * heap[1] * heap[2]

    return result
