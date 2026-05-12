class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while x != 0:
            digit = x % 10
            # Overflow check
            if reverse > (INT_MAX - digit) // 10:
                return 0
            reverse = reverse * 10 + digit
            x //= 10
        return sign * reverse
