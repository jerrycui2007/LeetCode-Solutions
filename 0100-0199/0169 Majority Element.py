from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element (appears more than n/2 times) using Boyer-Moore algorithm.
        
        Args:
            nums: Array of integers
            
        Returns:
            Majority element (guaranteed to exist)
        """
        # Initialize candidate and counter
        majority = nums[0]  # Initial candidate
        count = 1          # Count of current candidate
        
        # Boyer-Moore Voting Algorithm
        for num in nums[1:]:
            # If counter reaches zero, update candidate
            if count == 0:
                majority = num
                count = 1
                continue
                
            # Update counter based on current number
            if num == majority:
                count += 1
            else:
                count -= 1
        
        return majority


if __name__ == "__main__":
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
