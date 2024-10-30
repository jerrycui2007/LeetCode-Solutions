class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        Uses sliding window technique with a hash map for O(n) time complexity.
        
        Args:
            s: Input string
            
        Returns:
            Length of longest substring without repeating characters
        """
        # Handle empty string case
        if not s:
            return 0
            
        # Dictionary to store character positions
        char_index = {}
        max_length = 0
        start = 0
        
        # Iterate through string using sliding window
        for end, char in enumerate(s):
            # If character is in window, update start pointer
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                # Update max_length if current window is longer
                max_length = max(max_length, end - start + 1)
                
            # Update character's last seen position
            char_index[char] = end
            
        return max_length


if __name__ == "__main__":
    # Test cases
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", ""]
    solution = Solution()
    
    for test in test_cases:
        result = solution.lengthOfLongestSubstring(test)
        print(f'Input: "{test}" -> Output: {result}')

