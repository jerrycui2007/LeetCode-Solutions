from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):

        if self.next is not None:
            return str(self.val) + " -> " + self.next.__str__()

        else:
            return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a linked list.

        Args:
            head: Head of the linked list
        Returns:
            Head of the reversed linked list
        """
        # Handle empty list
        if not head:
            return None
        
        previous = None
        current = head
        
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        return previous


if __name__ == "__main__":
    print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).__str__())
