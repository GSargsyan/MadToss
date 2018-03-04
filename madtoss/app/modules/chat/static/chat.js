var ws = new WebSocket("ws://localhost/chat");

ws.onopen = function () {
	alert('connected!!!');
}

ws.onmessage = function (event) {
	  alert(event.data);
}
