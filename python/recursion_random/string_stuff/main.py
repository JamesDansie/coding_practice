from typing import List

def reverse(some_str: str) -> str:
    def dfs(i, res):
        if i >= len(some_str):
            print(f"CB i:{i}")
            return ""
        res = dfs(i + 1, res)
        print(f"code: i: {i}, res: {res} some_str[i]: {some_str[i]}")
        res += some_str[i]
        return res
    res = ""
    return dfs(0, res)

def normal_order(some_str: str) -> str:
    def dfs(i, res):
        if i <= 0:
            print(f"CB i:{i}")
            return some_str[i]
        res = dfs(i - 1, res)
        print(f"code: i: {i}, res: {res} some_str[i]: {some_str[i]}")
        res += some_str[i]
        return res
    res = ""
    return dfs(len(some_str) - 1, res)

def main():
    some_str = "hello"
    print(f"Reverse order: {reverse(some_str)}")
    print(f"Normal order: {normal_order(some_str)}")

if __name__ == "__main__":
    main()