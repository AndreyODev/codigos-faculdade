#include <iostream> // Biblioteca para entrada e saída
using namespace std;

const int MAX = 100; // Tamanho máximo do heap

// Estrutura que representa o elemento do heap
struct Elemento {
    int chave;
};

Elemento heap[MAX];
int tamanho = 0;     // Número atual de elementos no heap


// Usei o código de subida do slide, porém troquei o nome da variável
// Função recursiva que realiza a operação de subida no heap
void subir(Elemento T[], int indiceAtual) {
    int indicePai = indiceAtual / 2; // Calcula o índice do pai
    if (indicePai >= 1) {
        // Se a chave do elemento atual for maior que a do pai, troca os dois
        if (T[indiceAtual].chave > T[indicePai].chave) {
            Elemento temp = T[indiceAtual];
            T[indiceAtual] = T[indicePai];
            T[indicePai] = temp;
            // Chamada recursiva para continuar subindo
            subir(T, indicePai);
        }
    }
}

// Insere um novo valor no heap e aplica a subida
void inserir(int valor) {
    if (tamanho + 1 >= MAX) { // Verifica se o heap está cheio
        cout << "Heap cheio!" << endl;
        return;
    }
    tamanho++; // Aumenta o tamanho do heap
    heap[tamanho].chave = valor; // Insere o valor na próxima posição
    subir(heap, tamanho); // Ajusta a posição com a operação de subida
}

// Exibe os elementos do heap
void mostrar() {
    for (int i = 1; i <= tamanho; i++) {
        cout << heap[i].chave << " ";
    }
    cout << endl;
}

int main() {
    int quantidade;
    cout << "Quantos números deseja inserir? ";
    cin >> quantidade;

    // Lê os valores do usuário e os insere no heap
    for (int i = 0; i < quantidade; i++) {
        int valor;
        cout << "Informe o número: ";
        cin >> valor;
        inserir(valor);
    }

    // Mostra o heap construído
    cout << "Heap: ";
    mostrar();

    return 0;
}
