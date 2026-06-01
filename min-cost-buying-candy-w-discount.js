/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(cost) {
    
    // Sort in descending order
    cost.sort((a, b) => b - a);

    let total = 0;

    // Every 3rd candy is free
    for (let i = 0; i < cost.length; i++) {
        if ((i + 1) % 3 !== 0) {
            total += cost[i];
        }
    }

    return total;
};
