#include <iostream>
#include <string>

using namespace std;

const int Tamanho_Maximo = 100; // Tamanho máximo da árvore

/*No código abaixo foi criado uma estrutura
para agrupar diversos tipos de dados dentro No*/
struct No {
    int valor, altura;
    int esq, dir; // Índices dos filhos no array
};

No arvore[Tamanho_Maximo]; // Array fixo para armazenar os nós
int quant_No = 0; // Quantidade de nós

// Criar um novo nó na árvore
int criarNo(int valor) {
    if (quant_No >= Tamanho_Maximo) return -1; // Evita o estouro dp array
    arvore[quant_No] = {valor, 1, -1, -1}; // O valor representa o número inserido, já o número 1 representa a altura e o -1 os filhos da esquerda e direita
    return quant_No++;
}

// Retorna a altura do nó pelo índice
int altura(int indice) {
    return (indice == -1) ? 0 : arvore[indice].altura;  //Nessa linha de código é usado o operador ternario. O operador ternario é usado para compactar o if else em uma linha/
}
/*Sem utilizar o operador ternario:
int altura(int indice){
    if (indice == -1){
        return 0;
    }
    else {
        arvore[indice].altura
    }
}
*/

// Atualiza a altura do nó baseado nos filhos
void atualizarAltura(int indice) {
    if (indice != -1)
        arvore[indice].altura = 1 + max(altura(arvore[indice].esq), altura(arvore[indice].dir));
}

// Fator de balanceamento
int fatorBalanceamento(int indice) {
    return altura(arvore[indice].esq) - altura(arvore[indice].dir);
}

// Rotação à direita
int rotacaoDireita(int noDesbalanceado) {
    /*O filho da esquerda do nó desbalanceado trocara de posição com o nó desbalanceado*/
    int novoTopo = arvore[noDesbalanceado].esq;

    /*A subárvore da direita do novo topo precisa ser armazenada temporariamente*/
    int subArvoreTemporaria = arvore[novoTopo].dir;

    /*
       Realizando a rotação:
       1 - O nó desbalanceado passa a ser o filho da direita do novo topo
       2 - A subárvore temporária (antes à direita do novo topo) se torna a
          subárvore esquerda do nó desbalanceado.
    */
    arvore[novoTopo].dir = noDesbalanceado;
    arvore[noDesbalanceado].esq = subArvoreTemporaria;

    /*Atualiza a altura, pois a estrutura da árvore foi modificada*/
    atualizarAltura(noDesbalanceado);
    atualizarAltura(novoTopo);

    /*Retorna o novo topo da subárvore balanceada*/
    return novoTopo;
}
// Rotação à esquerda
int rotacaoEsquerda(int noDesbalanceado) {
    /*O filho da direita do nó desbalanceado trocara de posição com o nó desbalanceado*/
    int novoTopo = arvore[noDesbalanceado].dir;

    /*A subárvore esquerda do novo topo precisa ser armazenada temporariamente*/
    int subArvoreTemporaria = arvore[novoTopo].esq;

    /*
       Realizando a rotação:
       1 - O nó desbalanceado passa a ser o filho da esquerda do novo topo
       2 - A subárvore temporária (antes à esquerda do novo topo) se torna a
          subárvore direita do nó desbalanceado.
    */
    arvore[novoTopo].esq = noDesbalanceado;
    arvore[noDesbalanceado].dir = subArvoreTemporaria;

    /*Atualiza a altura, pois a estrutura da árvore foi modificada*/
    atualizarAltura(noDesbalanceado);
    atualizarAltura(novoTopo);

    /*Retorna o novo topo da subárvore balanceada*/
    return novoTopo;
}

// Balancear um nó
int balancear(int indice) {
    atualizarAltura(indice);
    int fb = fatorBalanceamento(indice);

    if (fb > 1) { // Desbalanceado à esquerda
        if (fatorBalanceamento(arvore[indice].esq) < 0)
            arvore[indice].esq = rotacaoEsquerda(arvore[indice].esq);
        return rotacaoDireita(indice);
    }
    if (fb < -1) { // Desbalanceado à direita
        if (fatorBalanceamento(arvore[indice].dir) > 0)
            arvore[indice].dir = rotacaoDireita(arvore[indice].dir);
        return rotacaoEsquerda(indice);
    }
    return indice;
}

// Inserir um valor na árvore
int inserir(int raiz, int valor) {
    if (raiz == -1)
        return criarNo(valor);

    if (valor < arvore[raiz].valor)
        arvore[raiz].esq = inserir(arvore[raiz].esq, valor);
    else
        arvore[raiz].dir = inserir(arvore[raiz].dir, valor);

    return balancear(raiz);
}

// Exibir a árvore
void mostrar(int raiz, int nivel = 0) {
    if (raiz == -1) return;

    mostrar(arvore[raiz].dir, nivel + 1);
    cout << string(nivel * 4, ' ') << arvore[raiz].valor << "(" << arvore[raiz].altura << ")" << endl;
    mostrar(arvore[raiz].esq, nivel + 1);
}

int main() {
    int raiz = -1;
    int opcao, valor;

    do {
        cout << "\n1 - Inserir\n2 - Mostrar Arvore\n3 - Sair\nEscolha: ";
        cin >> opcao;

        switch (opcao) {
            case 1:
                cout << "Valor: ";
                cin >> valor;
                raiz = inserir(raiz, valor);
                break;
            case 2:
                mostrar(raiz);
                break;
        }
    } while (opcao != 3);

    return 0;
}
