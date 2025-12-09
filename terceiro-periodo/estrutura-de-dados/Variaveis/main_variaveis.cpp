#include <iostream>

using namespace std;

int main(){
    char letra[] = "Andrey";
    int vida = 1;
    double decimal2 = 2.499;
    float decimal3 = 2.499;
    bool vivo = true;
    string nome = "Jeferson";

    cout << "Digite o numero de vidas: ";
    cin >> vida;
    cout << "Digite uma letra: ";
    cin >> letra;
    cout << "Dinheiro: ";
    cin >> decimal2;
    cout << "Digite seu nome: ";
    cin >> nome;

    cout << nome << "\n";
    cout << letra << "\n";
    cout << decimal2 << "\n";
    cout << decimal3 << "\n";
    cout << vivo << "\n";
    cout << vida << "\n";
    return 0;
}


