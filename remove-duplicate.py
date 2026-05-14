class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        # Position for next unique element
        i = 1

        for j in range(1, len(nums)):

            # New unique element found
            if nums[j] != nums[i - 1]:

                nums[i] = nums[j]

                i += 1

        return i
