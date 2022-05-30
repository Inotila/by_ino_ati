// this function removes the alert after 5 seconds
setTimeout(function () {
    let messages = document.getElementById("alert-message");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);