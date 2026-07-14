class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def backtrack(start, target, path):
            # Found valid combination
            if target == 0:
                result.append(path[:])
                return

            # Target exceeded
            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Reuse same element → pass i again
                backtrack(i, target - candidates[i], path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])

        return result
