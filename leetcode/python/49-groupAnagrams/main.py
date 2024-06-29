from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(str)
        return res.values()
    
    
def main():
    solution = Solution()
    input = ["eat","tea","tan","ate","nat","bat"]
    print(f"input: {input} ouput: {solution.groupAnagrams(input)}")
    print(f'input: {[""]} ouput: {solution.groupAnagrams([""])}')
    print(f'input: {["a"]} ouput: {solution.groupAnagrams(["a"])}')
    print(f'input: {["", ""]} ouput: {solution.groupAnagrams(["", ""])}')

if __name__ == "__main__":
    main()