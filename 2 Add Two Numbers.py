# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers represented as linked lists in reverse order.
        
        Args:
            l1: First number as a linked list
            l2: Second number as a linked list
            
        Returns:
            Sum as a linked list
        """
        dummy = ListNode(0)  # Dummy head
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values, use 0 if node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            
            # Create new node with ones digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


if __name__ == "__main__":
    # Test case: 342 + 465 = 807
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    solution = Solution().addTwoNumbers(l1, l2)
    
    # Print result
    result = []
    while solution:
        result.append(str(solution.val))
        solution = solution.next
    print("->".join(result))  # Expected: 7->0->8



