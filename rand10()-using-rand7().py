# The rand7() API is already defined for you.
# def rand7():
#     return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        while True:

            # Generate numbers from 1 to 49
            num = (rand7() - 1) * 7 + rand7()

            # Use only 1 to 40
            if num <= 40:

                # Convert to 1 to 10
                return (num - 1) % 10 + 1
