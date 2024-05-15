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
