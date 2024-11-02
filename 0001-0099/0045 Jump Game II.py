from typing import List
from math import inf


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Find minimum number of jumps to reach last index.
        Uses dynamic programming approach.
        
        Args:
            nums: Array where nums[i] represents maximum jump length at position i
            
        Returns:
            Minimum number of jumps to reach last index
        """
        # Get length of input array
        length = len(nums)
        
        # Initialize dp array with infinity
        dp = [inf for _ in range(length)]
        
        # Base case: starting position needs 0 jumps
        dp[0] = 0
        
        # Fill dp array
        for i in range(length):
            # Try all possible jumps from current position
            for j in range(nums[i] + 1):
                # Check if jump is within array bounds
                if i + j < length:
                    # Update minimum jumps needed if current path is better
                    if dp[i] + 1 < dp[i + j]:
                        dp[i + j] = dp[i] + 1
        
        # Return minimum jumps to reach last position
        return dp[-1]


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
