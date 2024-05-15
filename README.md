# Quiz de Perguntas e Respostas

Este é um simples programa de quiz de perguntas e respostas em Python. O usuário é apresentado a uma série de perguntas de múltipla escolha e deve selecionar a resposta correta para cada uma. No final, a pontuação do usuário é exibida.

## Estrutura do Código

O código consiste em uma lista de perguntas, cada uma com várias opções de resposta e a resposta correta indicada. O programa exibe cada pergunta ao usuário, aceita sua resposta e verifica se está correta, atualizando a pontuação do usuário em conformidade.

### Lista de Perguntas

A lista `perguntas` contém dicionários, cada um representando uma pergunta com suas respectivas opções e resposta correta:

```python
perguntas = [
    {
        "Pergunta": "Qual é a capital da França?",
        "Opções": {"a": "Londres", "b": "Paris", "c": "Madri", "d": "Berlim"},
        "resposta_correta": "b",
    },
    {
        "Pergunta": "Qual é a maior montanha do mundo?",
        "Opções": {"a": "Monte Everest", "b": "K2", "c": "Kilimanjaro", "d": "Aconcágua"},
        "resposta_correta": "a",
    }
]
```

### Lógica do Quiz:
##
```python
pontos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    
    for opcao in pergunta['Opções'].items():
        print(f"{opcao[0]}) {opcao[1]}")
    
    while True:
        resposta_usuario = input('Resposta: ').lower()
        if resposta_usuario in pergunta['Opções']:
            break
        else:
            print("Opção inválida. Por favor, insira uma opção válida (a, b, c ou d).")
    
    resposta_correta = pergunta['resposta_correta']
    
    if resposta_usuario == resposta_correta:
        pontos += 1
        print('Correto! 👍')
    else:
        print('Você errou! ❌')
    
print(f'Sua pontuação foi {pontos} respostas corretas de um total de {len(perguntas)} perguntas')
```
### Execução do Programa:
##
- O programa imprime a pergunta.
- Em seguida, imprime as opções de resposta.
- O usuário insere sua resposta.
- O programa verifica se a resposta está correta.
- Atualiza a pontuação do usuário.
- Após todas as perguntas, o programa imprime a pontuação final do usuário.

### Exemplo de Saída:
##
```terminal
Qual é a capital da França?
a) Londres
b) Paris
c) Madri
d) Berlim
Resposta: b
Correto! 👍
Qual é a maior montanha do mundo?
a) Monte Everest
b) K2
c) Kilimanjaro
d) Aconcágua
Resposta: c
Você errou! ❌
Sua pontuação foi 1 respostas corretas de um total de 2 perguntas
```
### Contribuição:
##
Se você gostaria de contribuir com melhorias para este Quiz, sinta-se à vontade para abrir uma issue ou enviar uma solicitação de pull request. Todas as contribuições são bem-vindas!

### Contato:
##
GitHub: Alexandre-Cunha <br>
Email: alexandrebarreto853@gmail.com
