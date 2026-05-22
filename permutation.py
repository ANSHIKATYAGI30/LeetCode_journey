class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def backtrack(path, used):

            # One complete permutation formed
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path, used)

                # Undo (Backtrack)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result
