class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def quickselect(left, right):
            pivot = nums[right]
            p = left

            # Place larger elements on left side
            for i in range(left, right):
                if nums[i] > pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            if p == k - 1:
                return nums[p]
            elif p > k - 1:
                return quickselect(left, p - 1)
            else:
                return quickselect(p + 1, right)

        return quickselect(0, len(nums) - 1)
