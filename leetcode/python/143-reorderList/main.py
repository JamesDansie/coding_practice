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
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        prev = slow.next = None 
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        p1 = head
        p2 = head2
        while p1 and p2:
            n1 = p1.next
            n2 = p2.next
            p1.next = p2
            p2.next = n1
            p1 = n1
            p2 = n2
        head =  p1
        
    
def main():
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution.reorderList(head)
    
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

if __name__ == "__main__":
    main()