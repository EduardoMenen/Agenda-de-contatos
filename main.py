agenda = []
def carregar_agenda():
    try:
        with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                if len(partes) == 3:
                    contato = {
                        "Nome": partes[0].strip(),
                        "Telefone": partes[1].strip(),
                        "Email": partes[2].strip()
                        }
                    agenda.append(contato)
    except FileNotFoundError:
        pass

carregar_agenda()

def cadastro():
    dados = {}
    dados['Nome'] = input('Nome: ').title().strip()
    dados['Telefone'] = input('Telefone: ').strip()
    dados['Email'] = input('Email: ').strip()
    agenda.append(dados.copy())
    try:
        with open('contatos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{agenda[-1]['Nome']}, {agenda[-1]['Telefone']}, {agenda[-1]['Email']}\n")
        print("✅ Contato cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar:", e)

def listagem():
    try:
        with open('contatos.txt', 'r', encoding='utf-8') as contatos:
            lista = contatos.read()
            print(lista)
    except FileNotFoundError:
        print("Lista de contatos não identifica.")

def pesquisa(contato):
    encontrou = False
    for c in agenda:
        if c['Nome'] == contato:
            encontrou = True
            print('-=' * 15)
            print(f"{c['Nome']}, {c['Telefone']}, {c['Email']}")
    if not encontrou:
        print('-=' * 15)
        print('Contato não encontrado.')

def remover(nome):
    encontrou = False
    for c in agenda:
        if c['Nome'] == nome:
            encontrou = True
            
    if not encontrou:
        print('-=' * 15)
        print('O contato a ser excluido não foi encontrado')

while True:
    print('-=' * 15)
    print()
    print('''1 - Cadastrar novo contato
2 - Exibir lista de contatos
3 - Pesquisar contato por nome
4 - Remover contato por nome
5 - Sair do programa''')
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listagem()
    elif opcao == 3:
        pesquisar = str(input('Digite o nome a ser pesquisado: ')).title().strip()
        pesquisa(pesquisar)
    elif opcao == 4:
        remova = str(input('Digite o nome do contato a ser excluído: '))
        remover(remova)
    elif opcao == 5:
        print('Programa finalizado. Volte sempre!')
        break