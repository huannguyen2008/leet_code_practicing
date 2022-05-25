/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function (prices) {
    let profit = 0
    let minPrices = prices[0]
    for (let i = 0; i < prices.length; i++) {
        let p = prices[i]
        if (minPrices > p) {
            minPrices = p
        } else if((p - minPrices) > profit) {
            profit = p - minPrices
        }
    }
    return profit
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]))