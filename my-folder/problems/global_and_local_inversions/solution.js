/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isIdealPermutation = function(nums) {
    for (let i = 0; i < nums.length; i++)
        if (i - nums[i] > 1 || i - nums[i] < -1) return false
    return true
};

