document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("user-form");
    const cadastroBtn = document.getElementById("cadastro-btn");
    const mensagem = document.getElementById("mensagem");

    cadastroBtn.addEventListener("click", async function () {
        const formData = new FormData(form);

        // Enviar dados do usuário ao servidor para cadastro
        const response = await fetch("/cadastro", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();

            // Exibir a mensagem de boas-vindas
            mensagem.innerHTML = data.mensagem;
            mensagem.style.display = "block";

            // Esconder o formulário
            form.style.display = "none";
        } else {
            alert("Erro ao cadastrar. Tente novamente.");
        }
    });
});
