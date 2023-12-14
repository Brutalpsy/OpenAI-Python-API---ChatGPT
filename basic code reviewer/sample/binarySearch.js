// time O(log n)
// space O(1)
const binarySearchRecursive = (array, start, end, numberToFind) => {
  let mid = Math.floor((start + end) / 2);

  if (numberToFind > array[array.length - 1]) {
    return -1;
  } else if (array[mid] === numberToFind) {
    return numberToFind;
  } else if (numberToFind > array[mid]) {
    return binarySearchRecursive(array, mid + 1, end, numberToFind);
  } else if (numberToFind < array[mid]) {
    return binarySearchRecursive(array, start, mid - 1, numberToFind);
  }
};

// time O(log n)
// space O(1)
const binarySearchIterative = (array, numberToFind) => {
  let left = 0;
  let right = array.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (numberToFind === array[mid]) {
      return numberToFind;
    } else if (numberToFind > array[mid]) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
};

let array = [1, 2, 3, 4, 5, 6];
console.log(binarySearchRecursive(array, 0, array.length - 1, 5));
console.log(binarySearchIterative(array, 5));
