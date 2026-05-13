class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        def backtrack(current, openCount, closeCount):

            # Complete valid string
            if len(current) == 2 * n:

                result.append(current)

                return

            # Add '('
            if openCount < n:

                backtrack(
                    current + "(",
                    openCount + 1,
                    closeCount
                )

            # Add ')'
            if closeCount < openCount:

                backtrack(
                    current + ")",
                    openCount,
                    closeCount + 1
                )

        backtrack("", 0, 0)

        return result
