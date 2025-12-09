#include <iostream>

using namespace std;
const int MAX = 5;  // Tamanho máximo da pilha

// Criando a estrutura da Pilha
// A estrutura contém dois componentes:
// -elementos
// -topo
struct Pilha{
    int elementos[10]; // Vetor que armazena os elementos da pilha
    int topo; // Índice do topo da pilha
};

// Função para configurar o topo da pilha
// Inicializa o topo como -1, indicando que a pilha está vazia
void Configurar_topo(Pilha &p){
    p.topo = -1;  // Topo inicializado como -1 (pilha vazia)
}

// Função para verificar se a pilha está vazia
// A pilha é vazia se o topo for igual a -1
bool Pilha_vazia(Pilha p){
  return p.topo == -1;  // Retorna true se a pilha estiver vazia
}

// Função para verificar se a pilha está cheia
// A pilha está cheia quando o topo atinge o valor máximo (MAX - 1)
bool Pilha_cheia(Pilha p) {
    return p.topo == MAX - 1;  // Retorna se a pilha estiver cheia
}

// Função para inserir (empilhar) um valor na pilha
void Inserir(Pilha &p, int valor) {
    if (Pilha_cheia(p)) {  // Verifica se a pilha já está cheia
        cout << "Pilha cheia!\n";  // Exibe uma mensagem se a pilha estiver cheia
    } else {
        p.topo++;  // Aumenta o topo
        p.elementos[p.topo] = valor; // Coloca o valor na posição do topo
        cout << "Elemento adicionado: " << valor << endl;
    }
}

// Função para remover (desempilhar) o valor do topo da pilha
void Remover(Pilha &p) {
    if (Pilha_vazia(p)) {  // Verifica se a pilha está vazia
        cout << "Pilha vazia!\n";
    } else {
        cout << "Elemento removido: " << p.elementos[p.topo] << endl;  // Exibe o valor que foi removido
        p.topo--;  // Diminui o topo
    }
}

// Função para exibir o valor que está no topo da pilha
void Topo_Elemento(Pilha p) {
    if (Pilha_vazia(p)) {  // Verifica se a pilha está vazia
        cout << "Pilha vazia!\n";
    } else {
        cout << "Elemento que está no topo: " << p.elementos[p.topo] << endl;
    }
}

// Função para exibir todos os elementos da pilha
void Mostrar_pilha (Pilha p) {
    if (Pilha_vazia(p)) {  // Verifica se a pilha está vazia
        cout << "Pilha vazia!\n";
    } else {
        cout << " Elementos da pilha: ";
        for (int i = 0; i <= p.topo; i++) { // Laço para percorrer todos os elementos da pilha
            cout << p.elementos[i] << " ";
        }
        cout << endl;  // Nova linha após exibir todos os elementos
    }
}

// Função principal (main) onde as operações da pilha são feitas
int main() {
    Pilha p;  // Criando uma instância da pilha
    Configurar_topo(p); // Começando o topo da pilha com -1
    // Empilha (adiciona) alguns valores na pilha
    Inserir(p, 1);  // Coloca o valor 1 na pilha
    Inserir(p, 2);  // Coloca o valor 2 na pilha
    Inserir(p, 3);  // Coloca o valor 3 na pilha

    Mostrar_pilha(p);  // Exibe os valores da pilha
    Topo_Elemento(p);  // Exibe o valor que está no topo da pilha

    Remover(p);  // Remove (desempilha) o valor do topo (valor 3)
    Mostrar_pilha(p);  // Exibe os valores da pilha novamente após o desempilhamento

    return 0;
}
