from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"val: {self.val}"
    def __repr__(self) -> str:
        return self.__str__()

class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        prev = None
        while head.next:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        breakpoint()
    
def main():
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution.reverse(head)
    
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

if __name__ == "__main__":
    main()