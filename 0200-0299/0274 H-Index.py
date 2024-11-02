from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Calculate the H-Index of a researcher.
        
        Args:
            citations: List where citations[i] is number of citations for paper i
            
        Returns:
            H-Index value
        """
        n = len(citations)
        # Create counting array for citations
        count = [0] * (n + 1)
        
        # Count papers for each citation number
        for citation in citations:
            # If citations more than n, count it as n
            count[min(citation, n)] += 1
        
        # Start from the top and accumulate papers
        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            # If we have enough papers with at least i citations
            if total >= i:
                return i
        
        return 0


if __name__ == "__main__":
    print(Solution().hIndex([1, 3, 1]))

