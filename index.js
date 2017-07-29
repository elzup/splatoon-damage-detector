const cv = require('opencv')
const camWidth = 640
const camHeight = 480
const camFps = 1000
const camInterval = 1000 / camFps
const { Parser } = require('binary-parser')

const camera = new cv.VideoCapture(1)
// camera.setWidth(camWidth)
// camera.setHeight(camHeight)

const pointMe = { x: 100, y: 500 }
const pointEn = { x: 250, y: 650 }

cv.readImage('./output/cam-bad.png', (err, im) => {
	detection(im)
})

// setInterval(function() {
// 	camera.read((err, im) => {
// 		// console.log(im.get());
// 		im.ellipse(pointMe.x, pointMe.y, 20, 20)
// 		im.ellipse(pointEn.x, pointEn.y, 20, 20)
// 		detection(im)
// 	})
// }, camFps)

function parseColor(num) {
	console.log(num.toString(2))
	const cbits = num.toString(2).substr(-24)
	console.log(cbits)
	console.log(cbits.substr(-24, 8))
	console.log(cbits.substr(-16, 8))
	const r = parseInt(cbits.substr(-24, 8), 2)
	const g = parseInt(cbits.substr(-16, 8), 2)
	const b = parseInt(cbits.substr(-8), 2)
	return { r, g, b }
}

function detection(im) {
	for (var p in im) {
		if (typeof im[p] === 'function') {
			console.log(p)
		}
	}
	console.log(im.getData())
	const colMe = im.get(pointMe.x, pointMe.y)
	const colEn = im.get(pointEn.x, pointEn.y)
	const buf = Buffer.allocUnsafe(4)
	buf.writeFloatBE(colMe)
	console.log(buf)
}
