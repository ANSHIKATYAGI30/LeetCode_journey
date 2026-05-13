class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:

            # If n is odd
            if n % 2 == 1:
                result *= x

            # Square x
            x *= x

            # Divide n by 2
            n //= 2

        return result
