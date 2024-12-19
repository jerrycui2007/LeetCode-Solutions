from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

        k is a positive integer and is less than or equal to the length of the linked list.
        If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

        :param head: head of the linked list
        :param k:    nodes to reverse at a time
        :return:     head of the new linked list
        """
        head_dummy = ListNode(0, head)
        group_previous = head_dummy

        while True:
            group_last = self.getKthNode(group_previous, k)
            if group_last is None:
                break  # we are done

            group_next = group_last.next

            # Reverse current group
            previous, current = group_last.next, group_previous.next
            while current != group_next:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

            temp = group_previous.next
            group_previous.next = group_last
            group_previous = temp

        return head_dummy.next

    def getKthNode(self, current: Optional[ListNode], k: int):
        """
        Returns the kth node after the head, or None if not long enough

        :param current: head node
        :param k:       nodes to search ahead
        :return:        the kth node
        """
        for _ in range(k):
            if current is None:
                return None

            current = current.next

        return current


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution().reverseKGroup(head, 2)

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))