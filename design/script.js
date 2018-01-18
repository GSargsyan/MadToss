var deg = 0;

function init_clock() {
	setInterval("tickMinute()", 100);
	var now = new Date();
}

document.body.onload = init_clock();

function tickMinute() {
	var minuteHand = byId("clock-minute-hand");
	minuteHand.style.transform = "rotate(" + deg + "deg)";
	deg += 0.01;
}

function byId(id) {
	return document.getElementById(id);
}
