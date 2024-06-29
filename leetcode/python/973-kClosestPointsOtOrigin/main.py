from typing import List
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            point.insert(0, distance)
        heapq.heapify(points)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(points)
            res.append([x, y])
        return res
        
    
def main():
    solution = Solution()
    points = [[1, 3], [-2,2]]
    k = 1
    print(f"output: {solution.kClosest(points, k)}")

if __name__ == "__main__":
    main()