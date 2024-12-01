// IMC = peso / (altura * altura)
const button = document.getElementById("button")

function imc() {
    const altura = parseFloat(document.getElementById("altura").value)
    const peso = parseFloat(document.getElementById("peso").value)
    const output = document.getElementById("output")

    let msg;

    if (isNaN(altura) || isNaN(peso)) {
        msg = "Preencha todos os campos!"
    } else {
        const imc = (peso / (altura * altura)).toFixed(1);
        if (imc < 18.5) msg = `O seu imc é ${imc}, você está abaixo do peso.`
        else if (imc < 25) msg = `O seu imc é ${imc}, você está no peso ideal.`
        else if (imc < 30) msg = `O seu imc é ${imc}, você está acima do peso.`
        else if (imc < 35)
            msg = `O seu imc é ${imc}, você está com obesidade grau I.`
        else if (imc < 40)
            msg = `O seu imc é ${imc}, você está com obesidade grau II.`
        else msg = `O seu imc é ${imc}, você está com obesidade grau III.`
    }

    output.textContent = msg
}

button.addEventListener("click", imc)
