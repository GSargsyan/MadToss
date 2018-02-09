client_seed = '';

function submit_coin_toss() {
	console.log('inside');
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert(this.responseText);
		}
	};
	xhttp.open("POST", "/toss", true);
	xhttp.send();
}
