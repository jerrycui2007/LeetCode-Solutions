from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product of all elements except self without division.
        
        Args:
            nums: Input array of integers
            
        Returns:
            Array where each element is product of all numbers except self
        """
        n = len(nums)
        output_array = [1 for _ in range(n)]
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            output_array[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and combine with left product
        right_product = 1
        for i in range(n - 1, -1, -1):
            output_array[i] *= right_product
            right_product *= nums[i]
        
        return output_array


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))

