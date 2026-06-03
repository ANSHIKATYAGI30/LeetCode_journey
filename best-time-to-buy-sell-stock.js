/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        // keep track of minimum buying price
        minPrice = Math.min(minPrice, price);

        // calculate profit if sold today
        maxProfit = Math.max(maxProfit, price - minPrice);
    }

    return maxProfit;
};
