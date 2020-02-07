#include <stdbool.h> // biblioteca de booleano
#include<stdlib.h> //cabeçalho padrão de entrada/saída de dados
#include<stdio.h> // bliblioteca de funcoes do tipo alocacao de memoria
#define TAM 10 //constante valor imutavel

int tamanho=0, lista[TAM];

void insere(int valor) {//struct para verificar e adicionar valor na lista
	int i;
	if(tamanho==TAM-1) {	//verifica se a lista nao esta cheia
		printf("\n\tERRO: A lista esta cheia\n");
		return;
	}

	for(i=tamanho; i>0 && valor<lista[i-1]; i--) {// faz com que os elementos deem um passo para tras
		lista[i]=lista[i-1];
	}

	lista[i]=valor;//elemento é adicionado na posição que o loop parou
	tamanho++;
	printf("\nElemento inserido com sucesso!\n\n");
}

void remover(int valor) {//struct para remover valor da lista
	int i,j,cont=0;

	if(tamanho==0) {//verifica se a lista esta vazia
		printf("\n\tErro: Lista vazia!");
		return;
	}

	for(i=0; i<tamanho && valor>=lista[i] ;i++) {
		if(valor==lista[i]) {
			for(j=i;j<tamanho-1;j++) {//mantem i de contador, j é modificado e incrementado
				lista[j]=lista[j+1];//faz os elementos darem um passo a frente
			}
			tamanho--;
			i--;//faz o i voltar para o caso de haver numero repetidos
			cont++;
		}
	}
	if(cont!=0)
		printf("\nElemento removido com sucesso!");
	else
		printf("\n\tERRO: valor nao esta na lista");
}

void exibir() {// struct Exibe a lista
	int i;

	if(tamanho==0){
		printf("\n\tErro: Lista vazia!");
		return;
	}

	for(i=0;i<=tamanho-1;i++) {
		printf("\nValor %d - posicao na lista %d ", lista[i],i+1);
	}
}

void menu() { //struct do menu

	printf("\n==============================================");
	printf("\n   MENU - Lista Estatica Sequencial");
	printf("\n==============================================");
	printf("\n	 Digite a opcao desejada:");
	printf("\n==============================================");
	printf("\n	 1 = Inserir Valor");
	printf("\n	 2 = Remover Valor");
	printf("\n	 3 = Mostrar Lista");
	printf("\n	 4 = Sair");
	printf("\n==============================================");
    printf("\n   ALUNO 1: RENAN BERTI RIBAS - REG: 1");
    printf("\n   ALUNO 2: GIULIA LEON - REG: 2 ");
    printf("\n   ALUNO 3: GUILHERME LAZARO - REG: 3");
    printf("\n   ALUNO 4: JOAO LUCAS NORIS - REG: 4 ");
	printf("\n==============================================");
	printf("\n\n");
}

int main() { // processo principal, onde chama as struct e usa o loop

	int opcao,valor;
  bool i = true; // variavel para loop

	do { //loop
    menu(); //chama menu
    printf("\nDigite uma opcao: ");
		scanf ("%d", &opcao); //opcao do usuario

		switch(opcao) { // condiçao que verifica e abre menu escolhido
			case 1:
				printf("\nDigite o valor a ser inserido ");
        scanf("%d", &valor);
				insere(valor); //chama struct de inserir valor
				printf("\n\nEscolha outra opcao para continuar...\n\n");
				break;

			case 2:
				printf("\nDigite o valor a ser removido ");
				scanf("%d", &valor);
				remover(valor); //chama struct de remover valor
				printf("\n\nEscolha outra opcao para continuar...\n\n");
				break;

			case 3:
        exibir(); //chama struct de exibir valores
				printf("\n\nEscolha outra opcao para continuar...\n\n");
				break;

			case 4:
				printf("\n\n#####  Fim do Programa!!  #####\n\n");
				i=false; //finaliza o loop da variavel booleana
				break;
		}
	}
	while(i==true); // loop do{
}