const botao = document.querySelector("button");

botao.addEventListener("click", async () => {

    const cnpj = document.querySelector('[name="cnpj"]').value;
    const cpf = document.querySelector('[name="cpf"]').value;
    const password = document.querySelector('[name="password"]').value;

    const resposta = await fetch("/api/cadastro", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cnpj: cnpj,
            cpf: cpf,
            password: password
        })
    });

    const dados = await resposta.json();

    console.log(dados);
});