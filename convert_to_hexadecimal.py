class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
          return "0"

        # Handle negative numbers using 32-bit two's complement
        num &= 0xffffffff

        hex_chars = "0123456789abcdef"

        result = ""

        while num > 0:

            digit = num % 16
            result = hex_chars[digit] + result
            num //= 16

        return result
