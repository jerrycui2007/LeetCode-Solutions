from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy

        while previous.next and previous.next.next:
            # Nodes to be swapped
            first = previous.next
            second = previous.next.next

            # Swapping the nodes
            first.next = second.next
            second.next = first
            previous.next = second

            # Move to the next pair
            previous = first

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

    solution = Solution().swapPairs(head)

    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))  # Expected: 2, 1, 4, 3, 6, 5





