/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
    if (s.length % 2 === 1) {
        return false
    }
    let stack = []
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(' || s[i] === '[' || s[i] === '{') {
            stack.push(s[i])
        }
        else if (s[i] === ')' && stack[stack.length - 1] === '(') {
            stack.pop()
        }
        else if (s[i] === ']' && stack[stack.length - 1] === '[') {
            stack.pop()
        }
        else if (s[i] === '}' && stack[stack.length - 1] === '{') {
            stack.pop()
        }
        else {
            stack.push(s[i])
        }
    }
    return !stack.length;

};

console.log(isValid('()()()()'))
console.log(isValid("([}}])"))