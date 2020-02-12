#!/usr/bin/node
const fs = require('fs');
process.on('uncaughtException', error => console.log(error));
fs.writeFileSync(process.argv[2], process.argv[3], 'utf8');
