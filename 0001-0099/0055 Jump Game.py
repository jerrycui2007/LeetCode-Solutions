from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index using the jump game rules.
        Uses greedy approach tracking maximum reachable position.
        
        Args:
            nums: Array where nums[i] represents maximum jump length at position i
            
        Returns:
            True if last index is reachable, False otherwise
        """
        # Track the furthest position we can reach
        length = len(nums)

        max_reach = 0
        target = length - 1
        
        # Iterate through positions we can reach
        for i in range(length):
            # If we can't reach current position, return False
            if i > max_reach:
                return False
                
            # Update maximum reachable position
            max_reach = max(max_reach, i + nums[i])
            
            # Early return if we can reach target
            if max_reach >= target:
                return True
        
        return True


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
