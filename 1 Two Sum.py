class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two distinct items in an array of numbers that add up to the target.
        Optimizes the solution by hashing each number and searching for a complement
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of two numbers that add up to target
        """
        num_map = {}  # val -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
            
        return []  # No solution found


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    
    print(Solution().twoSum(nums, target))
