from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array, allowing at most 2 occurrences.
        
        Args:
            nums: Sorted array of integers
            
        Returns:
            k: Length of modified array
        """
        # Handle arrays of length 2 or less
        if len(nums) <= 2:
            return len(nums)
            
        # Keep track of write position
        write_pos = 2
        
        # Start from third element
        for read_pos in range(2, len(nums)):
            # Keep element if it's different from element two positions back
            if nums[read_pos] != nums[write_pos - 2]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
                
        return write_pos


if __name__ == "__main__":
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
