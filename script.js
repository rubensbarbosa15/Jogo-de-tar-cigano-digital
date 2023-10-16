document.addEventListener("DOMContentLoaded", function () {
    const salvarBtn = document.getElementById("salvar-dados-btn");
    const gerarCartaBtn = document.getElementById("gerar-carta-btn");

    salvarBtn.addEventListener("click", async function () {
        const formData = new FormData(document.getElementById("user-form"));

        // Enviar dados do usuário ao servidor para salvar
        const response = await fetch("/salvar_dados", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            alert("Dados salvos com sucesso!");
        } else {
            alert("Erro ao salvar os dados. Tente novamente.");
        }
    });

    gerarCartaBtn.addEventListener("click", async function () {
        // Solicitar ao servidor para escolher uma carta
        const response = await fetch("/escolher_carta", {
            method: "POST",
        });

        if (response.ok) {
            const data = await response.json();

            // Exibir a carta escolhida e seu significado
            const cartaNome = document.getElementById("carta-nome");
            const cartaSignificado = document.getElementById("carta-significado");
            cartaNome.textContent = data.carta;
            cartaSignificado.textContent = data.significado;

            // Exibir o resultado
            const cartaResult = document.getElementById("carta-result");
            cartaResult.style.display = "block";

            // Esconder o botão "Gerar Carta"
            gerarCartaBtn.style.display = "none";
        } else {
            alert("Erro ao escolher a carta. Tente novamente.");
        }
    });
});
