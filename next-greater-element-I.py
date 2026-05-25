class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        nextGreater = {}

        # Find next greater for every element in nums2
        for num in nums2:

            while stack and num > stack[-1]:
                nextGreater[stack.pop()] = num

            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            nextGreater[stack.pop()] = -1

        # Build answer for nums1
        ans = []

        for num in nums1:
            ans.append(nextGreater[num])

        return ans
