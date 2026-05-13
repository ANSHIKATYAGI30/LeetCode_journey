class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        numbers = [str(i) for i in range(1, n + 1)]

        # factorials
        fact = [1] * n

        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        k -= 1   # zero-based indexing

        result = []

        for i in range(n, 0, -1):

            block_size = fact[i - 1]

            index = k // block_size

            result.append(numbers[index])

            numbers.pop(index)

            k %= block_size

        return "".join(result)
