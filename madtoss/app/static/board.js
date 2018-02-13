function submitCoinToss() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert(this.responseText);
		}
	};
	xhttp.open("POST", "/toss", true);
	xhttp.setRequestHeader("Content-Type", "application/json");

	
	// Amount = getAmount()
	data_str = {amount: '0.00001', chance: getChance(), betOn: 'H'};
	xhttp.send(JSON.stringify(data_str));
}

function changeBalance(newValue) {
	balanceElem = byId('balance');
	oldValue = balanceElem.innerHTML;
	overallTime = 0.5; // seconds

	diff = newValue - oldValue;
	alert(diff);
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
	chance_elem.innerHTML = parseInt(chanceElem.innerHTML) + value;
}
// changeBalance(0.00002);
