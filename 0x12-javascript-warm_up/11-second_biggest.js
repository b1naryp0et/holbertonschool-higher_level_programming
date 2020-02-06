#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('0');
} else {
  const array = [];
  let i = 2;
  for (i; i < process.argv.length; i++) {
    array.push(Number(process.argv[i]));
  }
  array.sort();
  console.log(array[array.length - 2]);
}
