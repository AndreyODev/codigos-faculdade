const h1 = document.getElementById('texto');
const botao = document.getElementById('botao');

botao.addEventListener('click', () => {
    if (h1.textContent === 'Clique no botão para reescrever o texto') {
        h1.textContent = 'Texto reescrito, clique de novo';
        h1.style.color = 'red';
    } else {
        h1.textContent = 'Clique no botão para reescrever o texto';
        h1.style.color = 'black';
    }
});