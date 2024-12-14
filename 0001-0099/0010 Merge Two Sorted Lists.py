from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists

        Args:
            list1: First list
            list2: Second list

        Returns:
            Head of the merged linked list
        """

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Append the remainder of the other list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return head


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(3, ListNode(4)))
    l2 = ListNode(4, ListNode(5, ListNode(6)))

    solution = Solution().mergeTwoLists(l1, l2)

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))  # Expected: 2->3->4->4->5->6