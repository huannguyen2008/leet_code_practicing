/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
    let charCounts = {}
    if (s.length !== t.length) {
        return false
    }
    for (let i = 0; i < s.length; i++) {
        charCounts[s[i]] = charCounts[s[i]] ? charCounts[s[i]]+1 : 1
        charCounts[t[i]] = charCounts[t[i]] ? charCounts[t[i]]-1 : -1
    }
    for (let l in charCounts) {
        if (charCounts[l] !== 0) {
            return false
        }
    }
    return true
};

console.log(isAnagram('anagram', 'nagaram'))