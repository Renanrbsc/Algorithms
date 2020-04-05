#-- Abstração --#

Definição: Abstração pode ser definida como a capacidade de representar cenários complexos usando termos simples.

Abstração é a habilidade de concentrar nos aspectos essenciais de um contexto qualquer, ignorando características menos importantes ou acidentais. A abstração enquanto pilar da programação orientada a objetos consiste em trabalhar um objeto dentro da programação se preocupando somente com suas principais propriedades, sem se apegar a pontos acidentais.

Abstrair é simplificar.Abstração é concentrar-se no que um objeto é e faz antes de se decidir como ele será implementado. O uso de abstração preserva a liberdade para tomar decisões de desenvolvimento ou de implementação apenas quando há um melhor entendimento do problema a ser resolvido.

#-- Herança --#

Definição: A Herança é um conceito do paradigma da orientação à objetos que determina que uma classe (filha) pode herdar atributos e métodos de uma outra classe (pai) e, assim, evitar que haja muita repetição de código.

Imagine que já exista uma classe que defina o comportamento de um dado objeto da vida real, por exemplo, animal. Uma vez que eu sei que o leão é um animal, o que se deve fazer é aproveitar a classe animal e fazer com que a classe leão derive (herde) da classe animal.

Ou seja, herança acontece quando duas classes são próximas, têm características mútuas mas não são iguais e existe uma especificação de uma delas. Portanto, em vez de escrever todo o código novamente é possível poupar algum tempo e dizer que uma classe herda da outra e depois basta escrever o código para a especificação dos pontos necessários da classe derivada (classe que herdou).

#-- Polimorfismo --#

Polimorfismo significa “algo que assume muitas formas", ou seja, essa ferramenta permite, caso seja necessário, que o software seja facilmente modificado e realize diferentes ações conforme é chamado. 

Polimorfismo permite que os objetos de diferentes tipos, cada um com seus comportamentos específicos, possam serem tratados a partir de uma classe, comum a todos as diferentes classes, mais abstratas. Ou seja, um objeto, de uma classe A mais abstrata, pode assumir o papel de diferentes tipos de objetos de classes derivadas, mais concretas.

#-- Composição --#

A composição geralmente é uma boa escolha quando um objeto faz parte de outro objeto. Por exemplo, uma calculadora tem componentes que fazem parte dela (display, teclado, unidade lógica) que podem ser programados de forma distinta. Ao fim da programação dessas classes menos complexas podemos utiliza-los para criar a calculador. O relacionamento de composição geralmente encontrado quando uma classe A (menos complexa) “…é parte de…” uma classe B (mais complexa).

Ou seja, na verdade, o nosso mundo é um punhado de objetos, compostos de outros objetos dentro, além de lidar com outros objetos de fora. 

Damos a isso o nome de composição: combinação de objetos, quando instanciamos objetos de uma classe dentro de outra, quando usamos objetos de uma classe dentro de outros objetos.

#-- Emcapsulamento --#

Esse recurso envolve agrupar métodos e atributos em pacotes que contém diferentes formas de acesso. Por exemplo, certos métodos e atributos são empacotados como públicos e podem ser acessados por qualquer classe outros pacotes vão ter alguma restrição de acesso – os métodos e atributos só poderão ser acessadas por uma classe filha ou nenhuma outra classe pode acessar.

Tal abordagem permite o programador criar de forma fácil um interface de aplicação para as classes e também para que elas possam esconder os métodos que são utilizados para o próprio funcionamento. Por exemplo, os métodos utilizados para o funcionamento da classe são definido como privados e os métodos que devem ser utilizados por classes mais complexas são definidos como públicos.





