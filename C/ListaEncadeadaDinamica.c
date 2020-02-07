#include <stdbool.h> // biblioteca de booleano
#include <stdio.h> //cabeçalho padrão de entrada/saída de dados
#include <stdlib.h> // bliblioteca de funcoes do tipo alocacao de memoria

typedef struct ponteiro PONTEIRO;

struct ponteiro{ //def ponteiro, definindo variaveis
  int numero;
  struct ponteiro *proximo;
};

PONTEIRO* criar_ponteiro(){ //criando ponteiro apontando a memoria para dados da lista
  PONTEIRO *novo = (PONTEIRO*)malloc(sizeof(PONTEIRO));
  return novo;
}

PONTEIRO* inserir_no_inicio(PONTEIRO* Lista,int dado){ // def para alocar dado no inicio
  PONTEIRO *novo_ponteiro=criar_ponteiro();
  novo_ponteiro->numero=dado;

  if(Lista == NULL){ //lista sem dado, chave/ponteiro ligada a null
    Lista=novo_ponteiro;
    novo_ponteiro->proximo=NULL;
  }else{ // lista com dado, chave/ponteiro ligada ao ultimo dado lançado
    novo_ponteiro->proximo=Lista;
    Lista=novo_ponteiro;
  }
  return Lista;
}

void imprimir_lista(PONTEIRO* Lista){ //def para imprimir na tela conforme lista cheia ou vazia
  PONTEIRO *imprimir=Lista;

  if(imprimir == NULL){ // lista vazia
    printf("[  ] -> NULL\n");

  }
  while(imprimir!=NULL){ //lista com dados
    printf("%d -> ",imprimir->numero);
    imprimir=imprimir->proximo;
  }
}

int main()
{
  printf("ALUNO 1: RENAN BERTI RIBAS - REG: 1\n");
  printf("ALUNO 2: GIULIA LEON - REG: 2 \n");
  printf("ALUNO 3: GUILHERME LAZARO - REG:  3\n");
  printf("ALUNO 4: JOAO LUCAS NORIS- REG: 4\n\n");

  bool i = true; // variavel do loop
  int variavel;
  PONTEIRO *Lista=NULL;// verifica lista dados
    imprimir_lista(Lista); // imprime a struct na condicao de null, n contem dado na lista

  do{ //loop de inputs sem fim
    printf("Digite um numero: "); //lanca valor tipo inteiro
    scanf ("%d",&variavel);
    Lista=inserir_no_inicio(Lista,variavel);//armazena na lista usando a struct de colocar no inicio

    imprimir_lista(Lista); // imprime lista agora contendo dados
    printf("\n");
  }
  while(i==true); //condiçao loop sem final
}