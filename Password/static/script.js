function copyPassword() {
    let password = document.getElementById("password").innerText;
    let message = document.getElementById("copy-message");

    navigator.clipboard.writeText(password);

    message.innerText = "Пароль скопирован!";
    message.classList.add("show");

    setTimeout(function () {
        message.classList.remove("show");
    }, 2000);
}