class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Check if a state is able to be reached by rotating the string

        Args:
            s: original string
            goal: target state

        Returns:
            If it is possible to reach the target state
        """
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False


if __name__ == "__main__":
    print(Solution().rotateString("abcde", "cdeab"))
    print(Solution().rotateString("abcde", "abced"))
