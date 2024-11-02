class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Check if a sentence is circular (last char of each word matches first char of next word,
        and last char of last word matches first char of first word).
        
        Args:
            sentence: String containing words separated by spaces
            
        Returns:
            True if sentence is circular, False otherwise
        """
        # Split sentence into words
        words = sentence.split()
        
        # Check each consecutive pair of words
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check if last word's end matches first word's start
        return words[0][0] == words[-1][-1]


if __name__ == '__main__':
    print(Solution().isCircularSentence("leetcode exercises sound delightful"))
