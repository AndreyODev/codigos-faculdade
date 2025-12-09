#include <iostream>
using namespace std;

const int TAM = 3;

void somaMatrizes(int matriz1[TAM][TAM], int matriz2[TAM][TAM], int resultado[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            resultado[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }
}

void imprimirMatriz(int matriz[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int matrizA[TAM][TAM] = {{1, 5, 3}, {4, 5, 9}, {7, 3, 2}};
    int matrizB[TAM][TAM] = {{4, 6, 7}, {6, 9, 4}, {7, 4, 1}};
    int resultado[TAM][TAM];

    somaMatrizes(matrizA, matrizB, resultado);
    imprimirMatriz(resultado);

    return 0;
}
