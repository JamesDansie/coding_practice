from collections import defaultdict
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
def main():
    solution = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head

    head1 = ListNode(3)
    head1.next = ListNode(2)
    head1.next.next = ListNode(0)

    print(f"Has cycle: {solution.hasCycle(head)}")
    print(f"Has no cycle: {solution.hasCycle(head1)}") 

if __name__ == "__main__":
    main()