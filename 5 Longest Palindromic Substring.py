class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring using a dynamic programming approach.
        
        Args:
            s: Input string
            
        Returns:
            Longest palindromic substring
        """
        if not s:
            return ""
            
        n = len(s)
        # Initialize dp table and result tracking
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1
        
        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Check if substring is palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
        
        return s[start:start + max_length]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
