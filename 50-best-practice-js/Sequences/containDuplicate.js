/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateSorted = function (nums) {
    const sorted = nums.sort()
    for (let i = 0; i < sorted.length; i++) {
        if (nums[i - 1] === nums[i]) {
            return true
        }
    }
    return false
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateWithMap1 = function (nums) {
    let map = new Map()
    for (let i = 0; i < nums.length; i++) {
        if (map.has(nums[i])) {
            return true
        }
        map.set(nums[i], i)
    }
    return false
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicateWithMap2 = function (nums) {
    let map = new Map()
    for (let i = 0; i < nums.length; i++) {
        if (map.get(nums[i])) {
            return true
        }
        map.set(nums[i], true)
    }
    return false
};

console.log(containsDuplicateWithMap2([1, 3, 2, 1]))