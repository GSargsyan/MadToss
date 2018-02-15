MAX_CHANCE = 99;
MIN_CHANCE = 1;

function submitCoinToss(coinSide) {
	disableTossButtons();
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			enableTossButtons();
			response = JSON.parse(this.responseText);
			updateStats(response);
		}
	};
	xhttp.open("POST", "/toss", true);
	xhttp.setRequestHeader("Content-Type", "application/json");
	data_str = {amount: getAmount(), chance: getChance(), betOn: coinSide};
	xhttp.send(JSON.stringify(data_str));
}

function disableTossButtons() {
	byId('heads-button').disabled = true;
	byId('tails-button').disabled = true;
}

function enableTossButtons() {
	byId('heads-button').disabled = false;
	byId('tails-button').disabled = false;
}

function changeBalance(newValue) {
	balanceElem = byId('balance');
	oldValue = balanceElem.innerHTML;
	overallTime = 0.5; // seconds

	diff = newValue - oldValue;
	steps = 5;
	stepSize = diff / steps;
}

function getChance() {
	return byId('chance').innerHTML;
}

function getAmount() {
	return byId('amount').innerHTML;
}

function changeChance(newValue) {
	byId('chance').innerHTML = newValue;
}

function addToChance(value) {
	chanceElem = byId('chance');
	newValue = parseInt(chanceElem.innerHTML) + value;
	if (MIN_CHANCE < newValue && newValue < MAX_CHANCE)
		chanceElem.innerHTML = parseInt(chanceElem.innerHTML) + value;
}

function updateStats(params) {
	byId('balance').innerHTML = Number(params.newBalance).toFixed(8);
}
// changeBalance(0.00002);
