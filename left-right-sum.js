/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function(nums) {

    let n = nums.length;
    let answer = new Array(n);

    let totalSum = 0;

    // Calculate total sum
    for (let num of nums) {
        totalSum += num;
    }

    let leftSum = 0;

    for (let i = 0; i < n; i++) {

        // right sum = total - left - current element
        let rightSum = totalSum - leftSum - nums[i];

        answer[i] = Math.abs(leftSum - rightSum);

        leftSum += nums[i];
    }

    return answer;
};
