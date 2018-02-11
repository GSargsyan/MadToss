function submitCoinToss() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert(this.responseText);
		}
	};
	xhttp.open("POST", "/toss", true);
	xhttp.setRequestHeader("Content-Type", "application/json");
	
	// var clientSeed = gen_client_seed(16);
	// data_str = {clientSeed: clientSeed}
	// xhttp.send(JSON.stringify(data_str));
	xhttp.send();
}

function changeBalance(newValue) {
	balanceElem = byId('balance');
	oldValue = balanceElem.innerHTML;
	overallTime = 0.5; // seconds

	diff = newValue - oldValue;
	alert(diff);
}
// changeBalance(0.00002);
