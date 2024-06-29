from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = heapq.nlargest(k, nums)
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
    
def main():
    kthLargest = KthLargest(3, [5, -1])
    print(f"output: {kthLargest.add(2)}")
    print(f"output: {kthLargest.add(1)}")
    print(f"output: {kthLargest.add(10)}")

if __name__ == "__main__":
    main()