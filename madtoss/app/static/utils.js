var now = new Date();
var currentMinute = now.getMinutes();
var currentSecond = now.getSeconds();
var currentHour = now.getHours();

var minuteDegrees = 0.1 * now.getSeconds() + 6 * now.getMinutes();
var hourDegrees = 30 * now.getHours() + now.getMinutes() * 0.5;

var tickInterval = 100; // milliseconds

function init_clock() {
	setInterval("tickClock()", tickInterval);
}

document.body.onload = init_clock();

function tickClock() {
	var minuteHand = byId("clock-minute-hand");
	hourDegrees = 30 * (new Date()).getHours() + (new Date()).getMinutes() * 0.5;
	var hourHand = byId("clock-hour-hand");

	minuteHand.style.transform = "rotate(" + minuteDegrees + "deg)";
	hourHand.style.transform = "rotate(" + hourDegrees + "deg)";

	minuteDegrees += 0.0001 * tickInterval;
}

function byId(id) {
	return document.getElementById(id);
}

function changeChance(newValue) {
	byId('chance').innerHTML = newValue;
}

function addToChance(value) {
	chance_elem = byId('chance');
	chance_elem.innerHTML = parseInt(chance_elem.innerHTML) + value;
}
