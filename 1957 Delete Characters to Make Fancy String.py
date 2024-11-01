class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Remove characters that appear three or more times consecutively.
        
        Args:
            s: Input string
            
        Returns:
            Modified string where no character appears three or more times in a row
        """
        # Handle empty or single character strings
        if len(s) <= 2:
            return s
            
        # Initialize result with first two characters
        result = [s[0], s[1]]
        
        # Check each character starting from third position
        for char in s[2:]:
            # Add char only if it would not create three consecutive same characters
            if char != result[-1] or char != result[-2]:
                result.append(char)
        
        return ''.join(result)


if __name__ == "__main__":
    print(Solution().makeFancyString("leeetcode"))
