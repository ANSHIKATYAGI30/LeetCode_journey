/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {

    let smaller = [];
    let equal = [];
    let greater = [];

    for (let num of nums) {

        if (num < pivot) {
            smaller.push(num);
        }
        else if (num === pivot) {
            equal.push(num);
        }
        else {
            greater.push(num);
        }
    }

    return [...smaller, ...equal, ...greater];
};
