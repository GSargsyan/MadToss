var ws = new WebSocket("ws://localhost/chat");

ws.onopen = function () {
	console.log('connected!!!');
}

ws.onmessage = function (event) {
	  console.log(event.data);
}

function checkSubmit(event) {
	if (event.keyCode === 13) { // If enter was preseed
		msg = byId('chat-input').value;
		console.log(msg);
		if (msg != "" || msg != "\n")
		{
			console.log('inside');
			ws.send(msg)
		}
	}
}
