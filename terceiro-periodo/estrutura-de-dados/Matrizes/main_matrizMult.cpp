#include <iostream>
using namespace std;

const int TAM = 3;

void multiplicaMatrizes(int matriz1[TAM][TAM], int matriz2[TAM][TAM], int resultado[TAM][TAM]) {
    for (int i = 0; i < TAM; i++) {
        for (int j = 0; j < TAM; j++) {
            resultado[i][j] = 0;
            for (int k = 0; k < TAM; k++) {
                resultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
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
    int matrizA[TAM][TAM] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrizB[TAM][TAM] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int resultado[TAM][TAM];

    multiplicaMatrizes(matrizA, matrizB, resultado);
    imprimirMatriz(resultado);

    return 0;
}
