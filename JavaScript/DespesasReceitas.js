const usuarios = [
    {
        nome: 'Salvio',
        receitas: [115.3, 48.7, 98.3, 14.5],
        despesas: [85.3, 13.5, 19.9]
    },
    {
        nome: 'Marcio',
        receitas: [24.6, 214.3, 45.3],
        despesas: [185.3, 12.1, 120.0]
    },
    {
        nome: 'Lucia',
        receitas: [9.8, 120.3, 340.2, 45.3],
        despesas: [450.2, 29.9]
    }
];

function calculaSaldo(receitas, despesas) {
    function somaNumeros(numeros) {
        let sum = 0;
        for ( i = 0 ; i < numeros.length ; i++){
            sum += numeros[i]
        }
        return sum
    }

    let somaReceitas = somaNumeros(receitas);
    let somaDespesas = somaNumeros(despesas);

    return somaReceitas - somaDespesas
}

for (var i = 0 ; i < usuarios.length ; i++ ){
    console.log( calculaSaldo(usuarios[i].receitas, usuarios[i].despesas) )
}