from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotates the list to the right by k places

        :param head: head of linked list
        :param k:    places to rotate
        :return:     head of linked list
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0, head)

        length = 1
        current = head

        while current.next is not None:
            current = current.next
            length += 1

        k = k % length

        for _ in range(k):
            tail = head
            tail_previous = None
            while tail.next is not None:
                tail_previous = tail
                tail = tail.next

            tail.next = dummy.next
            tail_previous.next = None
            dummy.next = tail

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution().rotateRight(head, 2)

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))

