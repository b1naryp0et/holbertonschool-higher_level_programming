#!/usr/bin/node
const numargs = require('numargs');
if (numargs.argv.length === 2) {
  console.log('No argument');
} else if (numargs.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
