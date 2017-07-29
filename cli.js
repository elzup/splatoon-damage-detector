#!/usr/bin/env node
'use strict';
const meow = require('meow');
const splatoonDamageDetector = require('.');

const cli = meow(`
	Usage
	  $ splatoon-damage-detector [input]

	Options
	  --foo  Lorem ipsum [Default: false]

	Examples
	  $ splatoon-damage-detector
	  unicorns & rainbows
	  $ splatoon-damage-detector ponies
	  ponies & rainbows
`);

console.log(splatoonDamageDetector(cli.input[0] || 'unicorns'));
