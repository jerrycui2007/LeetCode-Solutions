from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the Nth last node from a linked list

        :param head: head of linked list
        :param n:    n
        :return:     head of the new linked list
        """
        dummy = ListNode(0, head)

        previous = dummy
        current_ahead = dummy

        for _ in range(n + 1):
            current_ahead = current_ahead.next

        while current_ahead is not None:
            previous = previous.next
            current_ahead = current_ahead.next

        previous.next = previous.next.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution().removeNthFromEnd(head, 2)

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))