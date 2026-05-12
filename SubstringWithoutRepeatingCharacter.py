class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = set()

        left = 0
        maxLen = 0

        for right in range(len(s)):

            # Remove duplicates
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Update maximum length
            maxLen = max(maxLen, right - left + 1)

        return maxLen
