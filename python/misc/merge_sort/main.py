

def merge_sort(arr: list) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        left_index = right_index = ans_index = 0

        while left_index < len(L) and right_index < len(R):
            if L[left_index] <= R[right_index]:
                arr[ans_index] = L[left_index]
                left_index += 1
            else:
                arr[ans_index] = R[right_index]
                right_index += 1
            ans_index += 1
        
        while left_index < len(L):
            arr[ans_index] = L[left_index]
            ans_index += 1
            left_index += 1
        
        while right_index < len(R):
            arr[ans_index] = R[right_index]
            ans_index += 1
            right_index += 1

def main():
    arr = [4, 2, 1, 5]
    merge_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()