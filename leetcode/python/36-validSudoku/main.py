from typing import List
import copy

def isValidSudoku(board: List[List[str]]) -> bool:
    row_set = [set() for row in board]
    col_set = copy.deepcopy(row_set)
    little_set = [[set() for _ in range(3)] for _ in range(3)]

    for row in range(len(board)):
        for col in range(len(board[row])):
            curr = board[row][col]
            if curr.isnumeric():
                if (curr in row_set[row] or 
                    curr in col_set[col] or 
                    curr in little_set[int(row/3)][int(col/3)]):
                    breakpoint()
                    return False
                else:
                    row_set[row].add(curr)
                    col_set[col].add(curr)
                    little_set[int(row/3)][int(col/3)].add(curr)
    return True
    
def main():
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(f"valid board?: {isValidSudoku(board)}")

if __name__ == "__main__":
    main()