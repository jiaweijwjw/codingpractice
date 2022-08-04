from heapq import heappushpop, heappush, heappop

class MedianFinder:

    # to find median fast, we need a sorted array. how do we get a sorted array for a running stream of inputs?
    # think of the different type of sorting algorithm. cant be we run sort() everytime a new number is added to the array.
    # the only possible sorting algorithm to use is heap sort.
    # the trick is then to realise that to find the median of a sorted array, we need to know the middle element in the array
    # to do this, we use 2 heaps, the first heap to store numbers on the smaller half of the sorted array and the other to store the larger numbers
    # note that for the heap storing the smaller half, we are using max heap while for the heap storing the larger half, we are using min heap
    # since we are using python heapq, the default is a min heap. to convert to a max heap, multiply the value by -1
    # next, note that at any one point in time, both the heaps should have either the same size, or one heap larger by 1
    # if one heap is larger than the other by 1 element, we know that the total number of elements in the array is odd and the median value
    # is the min / max of the heap with 1 extra element
    # for my implementation, i am using the max heap to store the extra element if there are odd number of elements
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
    # https://leetcode.com/problems/find-median-from-data-stream/discuss/1330646/C%2B%2BJavaPython-MinHeap-MaxHeap-Solution-Picture-explain-Clean-and-Concise
    # for the implementation of add number, the pseudo code is as follows:
    # first, we always add the number to the max_heap
    # then, we will take out the largest number in max_heap and put it into min_heap
    # this is to account for the chance that the newly added number should belong to the larger half of the array (on the min_heap side)
    # since we do this, there is a chance that the size of min heap is larger than max heap.
    # remember that at any one time, the min heap size should either be same size as max heap or max_heap.size-1 as we are storing the odd number element on max heap
    # if the size is not balanced to the afore mentioned requirements, we pass back 1 element from the min_heap to the max_heap
    def addNum(self, num: int) -> None:
        largest_in_max_heap = heappushpop(self.max_heap, num*-1)
        heappush(self.min_heap, largest_in_max_heap*-1)
        if len(self.min_heap) > len(self.max_heap):
            smallest_in_min_heap = heappop(self.min_heap)
            heappush(self.max_heap, smallest_in_min_heap*-1)

    # finding the median is simple, if odd number, return the top element of the larger size heap
    # in my implementation, the larger size heap is always the max heap
    # if both heaps are the same size, return the average value of the top element in min and max heap
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(self.max_heap[0]*-1)
        assert len(self.max_heap) == len(self.min_heap)
        return (self.max_heap[0]*-1+self.min_heap[0])/2.0

if __name__ == "__main__":
    finder = MedianFinder()
    nums = [5,1,3,4,2]
    for num in nums:
        finder.addNum(num)
        print(finder.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()