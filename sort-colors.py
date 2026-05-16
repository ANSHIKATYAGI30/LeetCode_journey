class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # place 0 to left side
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # 1 stays in middle
            elif nums[mid] == 1:
                mid += 1

            # place 2 to right side
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
