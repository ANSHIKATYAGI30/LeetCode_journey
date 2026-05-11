/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};
/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    let sum = 0;
    for (let num of this.nums) {
        sum += num;
    }
    return sum;
};
/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(',')}]`;
};
