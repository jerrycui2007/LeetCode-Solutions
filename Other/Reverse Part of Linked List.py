from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedListSegment(self, head: Optional[ListNode], start: int, end: int) -> Optional[ListNode]:
        """
        Reverses a segment of a linked list

        :param head:        head of the linked list
        :param start:       index of first node to reverse
        :param end:         index of last node to reverse
        :return:            head of reversed linked list
        """
        start_dummy = head
        previous_dummy = None

        for _ in range(start):
            previous_dummy = start_dummy
            start_dummy = start_dummy.next

        end_dummy = start_dummy

        for _ in range(end - start):
            end_dummy = end_dummy.next

        next_dummy = end_dummy.next

        # Isolate target segment
        if previous_dummy is not None:
            previous_dummy.next = None

        end_dummy.next = None

        segment_head, segment_tail = self.reverseLinkedList(start_dummy)

        # Re-integrate segment
        if previous_dummy is not None:
            previous_dummy.next = segment_head
        else:
            head = segment_head

        segment_tail.next = next_dummy

        return head

    def reverseLinkedList(self, head: Optional[ListNode]):
        """
        Reverses a linked list

        :param head: head of linked list
        :return:     head of linked list, tail of linked list
        """
        if head is None or head.next is None:
            return head, head

        rest, tail = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None

        return rest, head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution().reverseLinkedListSegment(head, 1, 3)

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))