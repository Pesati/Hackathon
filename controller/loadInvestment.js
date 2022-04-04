var bodyparser = require('body-parser');
var fs=require('fs');
var data=fs.readFileSync('./API/investments.json', 'utf8');
var investments = JSON.parse(data)
