#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (let j = 0; j < list.length; j++) {
    if (list[j] === searchElement) {
      x = x+1;
    }
  }
  return x;
};
