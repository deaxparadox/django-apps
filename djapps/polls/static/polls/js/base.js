console.log("This is Polls Application")


const closeMessage = function() {
    const button = document.querySelector("#message-close");
    const messageContaier = document.querySelector("#message-container");
    button.onclick = function(e) {
        messageContaier.style.display = "none";
    }
}

closeMessage();