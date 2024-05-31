/** product: calculate the product of an array of numbers. */

function product(nums) {
  if (nums.length <= 0) return 1;
  const num = nums.pop();
  return num * product(nums);
}

/** longest: return the length of the longest word in an array of words. */

function longest(words) {
  if (words.length === 1) return words[0].length;
  const word = words.pop().length;
  const longestWord = longest(words);
  return word >= longestWord ? word : longestWord;
}

/** everyOther: return a string with every other letter. */

function everyOther(str) {
  if (str.length === 0) return "";
  return str[0] + everyOther(str.slice(2));
}

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str) {
  if (str.length <= 1) return true;
  if (str[0] !== str[str.length - 1]) return false;
  return isPalindrome(str.slice(1, -1));
}

/** findIndex: return the first index of val in arr (or -1 if val is not present). */

function findIndex(arr, val) {
  if (arr.length === 0) return -1;
  if (arr[0] === val) return 0;
  const subIndex = findIndex(arr.slice(1), val);
  return subIndex === -1 ? -1 : 1 + subIndex;
}

/** revString: return a copy of a string, but in reverse. */

function revString(str) {
  if (str.length <= 0) return "";
  return str[str.length - 1] + revString(str.slice(0, -1));
}

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj) {
  let arr = [];
  for (let key in obj) {
    if (typeof obj[key] === "string") {
      arr.push(obj[key]);
    }
    if (typeof obj[key] === "object") {
      arr.push(...gatherStrings(obj[key]));
    }
  }
  return arr;
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val, left = 0) {
  console.log(arr);
  if (arr.length === 0) {
    return -1;
  }
  const midpoint = Math.floor((arr.length - 1) / 2);
  if (arr[midpoint] === val) {
    return left + midpoint;
  } else if (arr[midpoint] < val) {
    return binarySearch(arr.slice(midpoint + 1), val, left + midpoint + 1);
  } else return binarySearch(arr.slice(0, midpoint), val, left);
}
module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch,
};
