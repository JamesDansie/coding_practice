from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            y = heapq.heappop(neg_stones)
            x = heapq.heappop(neg_stones)
            if x != y:
                heapq.heappush(neg_stones, y - x)
        if neg_stones:
            return -neg_stones[0]
        else:
            return 0

        
    
def main():
    solution = Solution()
    stones = [1, 3]
    print(f"output: {solution.lastStoneWeight(stones)}")

if __name__ == "__main__":
    main()