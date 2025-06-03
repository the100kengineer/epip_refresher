import heapq
# for k-largest use a min-heap of size k
def stream_processing_k_largest(stream, k=3):
    heap = []
    for item in stream:
        heapq.heappush(heap, item)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

# for k-smallest use a max-heap of size k
def stream_processing_k_smallest(stream, k=3):   
    heap = []
    for item in stream:
        heapq.heappush(heap, -item)  # Push negative values for max-heap
        if len(heap) > k:
            heapq.heappop(heap)
    return [-x for x in heap] # Return the k smallest elements as positive values

# TODO: add an example to process stream of tuples/names tuples
stream = [5, 7, 9, 1, 3, 2, 8, 6]
print('Processing stream:', stream)
print('k-largest\t', stream_processing_k_largest(stream, 3)) # [7, 8, 9]
print('k-smallest\t', stream_processing_k_smallest(stream, 3)) # [1, 2, 3]