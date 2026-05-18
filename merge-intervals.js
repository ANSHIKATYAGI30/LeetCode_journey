/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    
    // Sort by starting time
    intervals.sort((a, b) => a[0] - b[0]);

    let result = [];

    for (let interval of intervals) {

        // If no overlap, add interval
        if (
            result.length === 0 ||
            result[result.length - 1][1] < interval[0]
        ) {
            result.push(interval);
        } 
        else {
            // Merge intervals
            result[result.length - 1][1] = Math.max(
                result[result.length - 1][1],
                interval[1]
            );
        }
    }

    return result;
};
