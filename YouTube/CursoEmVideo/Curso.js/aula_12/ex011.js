var idade = 13 // Você pode alterar a idade com os números que você quiser
console.log(`Você tem ${idade} anos.`)
if(idade < 16) {
    console.log("Não vota")
} else if(idade < 18 || idade > 65) {
    console.log("Voto opcional")
} else {
    console.log("Voto obrigatório")
}