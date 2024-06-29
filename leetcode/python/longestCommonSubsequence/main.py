

def longestCommonSubsequence(text1: str, text2: str) -> int:
    memo = {}
    def recurse_solve(p1, p2):
        if p1 == len(text1) or p2 == len(text2):
            return 0
        
        if (p1, p2) in memo:
            return memo[(p1, p2)]
        
        # p1 is not part of the solution
        sol_1 = recurse_solve(p1 + 1, p2)

        # breakpoint()
        # p1 is part of the solution
        first_occurrence = text2.find(text1[p1], p2)
        sol_2 = 0
        if first_occurrence != -1:
            sol_2 = 1 + recurse_solve(p1 + 1, first_occurrence + 1)
        
        ans = max(sol_1, sol_2)
        memo[(p1, p2)] = ans
        print(ans, p1, p2, text1[p1], text2[p2])
        return ans
    return recurse_solve(0, 0)

def longestCommonSubsequenceDynamic(text1: str, text2: str) -> int:
    # fill with all zeros
    dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) +1)]
    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text1))):
            if text2[col] == text1[row]:
                dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
            else:
                dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

    return dp_grid[0][0]

def main():
    string1 = "ezupkr"
    string2 = "ubmrapg"
    print(f"Recursive solution: {longestCommonSubsequence(string1, string2)}")
    print(f"Dynamic solution: {longestCommonSubsequenceDynamic(string1, string2)}")
    # print(longestCommonSubsequence(string2, string2))

if __name__ == "__main__":
    main()