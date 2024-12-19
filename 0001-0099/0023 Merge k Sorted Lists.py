from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges K sorted linked lists

        :param lists: list of heads of the linked lists
        :return:
        """
        dummy = ListNode(0)
        current = dummy

        heap = []

        # Initialize heapq
        for index, head in enumerate(lists):
            if head is not None:
                heapq.heappush(heap, (head.val, index, head))

        while len(heap) > 0:

            value, index, head = heapq.heappop(heap)

            current.next = head
            current = current.next

            if head.next is not None:
                heapq.heappush(heap, (head.next.val, index, head.next))

        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    solution = Solution().mergeKLists([list1, list2, list3])

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))


