from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.

        Args:
            nums: Sorted array of integers
            
        Returns:
            k: Number of unique elements
        """
        # Handle empty array
        if not nums:
            return 0
            
        # Use two-pointer technique
        write_pos = 1  # Start from 1 as first element is always unique
        
        # Iterate through array starting from second element
        for read_pos in range(1, len(nums)):
            # If current element is different from previous, keep it
            if nums[read_pos] != nums[write_pos - 1]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos


if __name__ == "__main__":
    print(Solution().removeDuplicates([0, 3, 4]))
