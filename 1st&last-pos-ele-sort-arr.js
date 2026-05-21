/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {

    function findFirst(nums, target) {

        let left = 0;
        let right = nums.length - 1;
        let ans = -1;

        while (left <= right) {

            let mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                ans = mid;
                right = mid - 1; // search left side
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return ans;
    }

    function findLast(nums, target) {

        let left = 0;
        let right = nums.length - 1;
        let ans = -1;

        while (left <= right) {

            let mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                ans = mid;
                left = mid + 1; // search right side
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return ans;
    }

    return [findFirst(nums, target), findLast(nums, target)];
};
