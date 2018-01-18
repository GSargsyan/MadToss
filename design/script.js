var now = new Date();
var currentMinute = now.getMinutes();
var currentSecond = now.getSeconds();
var currentHour = now.getHours();

var minuteDegrees = 0.1 * now.getSeconds() + 6 * now.getMinutes();
var hourDegrees = now.getHours() * 360 / 24;

function init_clock() {
	setInterval("tickMinutes()", 100);
}

document.body.onload = init_clock();

function tickMinutes() {
	var minuteHand = byId("clock-minute-hand");
	minuteHand.style.transform = "rotate(" + minuteDegrees + "deg)";
	minuteDegrees += 0.01;
}

function byId(id) {
	return document.getElementById(id);
}
