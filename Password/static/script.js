function copyPassword() {
    let password = document.getElementById("password").innerText;
    let message = document.getElementById("copy-message");

    let tempInput = document.createElement("textarea");
    tempInput.value = password;
    document.body.appendChild(tempInput);

    tempInput.select();
    document.execCommand("copy");

    document.body.removeChild(tempInput);

    message.innerText = "Пароль скопирован!";
    message.classList.add("show");

    setTimeout(function () {
        message.classList.remove("show");
    }, 2000);
}