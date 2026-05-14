/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumGap = function(nums) {

    let n = nums.length;

    if(n < 2) return 0;

    let minVal = Math.min(...nums);
    let maxVal = Math.max(...nums);

    if(minVal === maxVal) return 0;

    // Bucket size
    let bucketSize = Math.max(
        1,
        Math.floor((maxVal - minVal) / (n - 1))
    );

    let bucketCount =
        Math.floor((maxVal - minVal) / bucketSize) + 1;

    let buckets = Array(bucketCount)
        .fill(null)
        .map(() => ({
            used: false,
            min: Infinity,
            max: -Infinity
        }));

    // Place numbers into buckets
    for(let num of nums) {

        let idx =
            Math.floor((num - minVal) / bucketSize);

        buckets[idx].used = true;

        buckets[idx].min =
            Math.min(buckets[idx].min, num);

        buckets[idx].max =
            Math.max(buckets[idx].max, num);
    }

    // Find maximum gap
    let prevMax = minVal;

    let maxGap = 0;

    for(let bucket of buckets) {

        if(!bucket.used) continue;

        maxGap = Math.max(
            maxGap,
            bucket.min - prevMax
        );

        prevMax = bucket.max;
    }

    return maxGap;
};
