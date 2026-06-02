class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """

        if valueDiff < 0:
            return False

        buckets = {}
        bucket_size = valueDiff + 1

        for i, num in enumerate(nums):

            # Bucket ID
            bucket_id = num // bucket_size

            # Handle negative numbers correctly
            if num < 0:
                bucket_id -= 1

            # Same bucket
            if bucket_id in buckets:
                return True

            # Neighbor bucket check
            if (bucket_id - 1 in buckets and
                abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True

            if (bucket_id + 1 in buckets and
                abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True

            # Add current number
            buckets[bucket_id] = num

            # Maintain sliding window of size indexDiff
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket = old_num // bucket_size

                if old_num < 0:
                    old_bucket -= 1

                del buckets[old_bucket]

        return False
