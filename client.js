let username = sessionStorage.getItem("username");
if (!username) {
    window.location.href = "/";  // Redirect if no username
}

let socket = io.connect("wss://" + location.host);

socket.on("connect", function() {
    socket.emit("join", { user: username });
});

socket.on("message", function(data) {
    let messages = document.getElementById("messages");
    let messageElement = document.createElement("p");
    messageElement.innerText = `${data.user}: ${data.msg}`;
    messages.appendChild(messageElement);
});

function sendMessage() {
    let messageInput = document.getElementById("messageInput");
    let msg = messageInput.value.trim();

    if (msg !== "") {
        socket.emit("message", { user: username, msg: msg });
        messageInput.value = "";
    }
}
