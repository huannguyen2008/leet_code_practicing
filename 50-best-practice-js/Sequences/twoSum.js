/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSumBruteForce = function (nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = 1; j < nums.length; j++) {
            if (i !== j) {
                if (nums[j] === target - nums[i]) {
                    return [i,j]
                }
            }
        }
    }
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSumHashMap = function (nums, target) {
    let map = new Map()
    for (let i = 0; i < nums.length; i++) {
        let remain = target - nums[i]
        if (map.has(remain)) {
            return [map.get(remain), i]
        }
        map.set(nums[i], i)
    }
};

console.log(twoSumBruteForce([2, 7, 11, 15], 13))
console.log(twoSumHashMap([2, 7, 11, 15], 13))