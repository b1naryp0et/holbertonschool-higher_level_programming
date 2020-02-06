#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) { console.log('Missing size'); }
const arry = [];
for (let i = 0; i < process.argv[2]; i++) {
  arry.push('X');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log(arry.join(''));
}
