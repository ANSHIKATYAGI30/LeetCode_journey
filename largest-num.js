/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    
    // Convert numbers to strings
    nums = nums.map(String);

    // Custom sorting
    nums.sort((a, b) => (b + a) - (a + b));

    // Edge case: all zeros
    if (nums[0] === "0") {
        return "0";
    }

    return nums.join('');
};
