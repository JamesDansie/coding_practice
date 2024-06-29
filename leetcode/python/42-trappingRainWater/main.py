from typing import List, Optional

class Solution:
    def trap(self, height: List[int]) -> int:
        # l_max = [0 for _ in height]
        # r_max = [0 for _ in height]
        # l_max_num = 0
        # r_max_num = 0
        # for index in range(len(height)):
        #     l_max_num = max(l_max_num, height[index])
        #     l_max[index] = l_max_num
        #     r_max_num = max(r_max_num, height[-(index+1)])
        #     r_max[-(index+1)] = r_max_num
        # area = 0
        # print(l_max)
        # print(r_max)
        # for index in range(len(height)):
        #     area += min(l_max[index], r_max[index]) - height[index]
        # return area
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        area = 0
        while l < r:
            if l_max <= r_max:
                l += 1
                sub_area = min(l_max, r_max) - height[l]
                area += max(sub_area, 0)
                l_max = max(l_max, height[l])
            else:
                r -= 1
                sub_area = min(l_max, r_max) - height[r]
                area += max(0, sub_area)
                r_max = max(r_max, height[r])
        return area
    
def main():
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [4,2,3]
    # height = [4,2,0,3,2,5]
    height = [5,5,1,7,1,1,5,2,7,6]
    solution = Solution()
    print(f"output: {solution.trap(height)}")

if __name__ == "__main__":
    main()