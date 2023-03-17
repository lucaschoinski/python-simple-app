dataBase = []


def deletaAluno():  # Deleta aluno do dataBase
    quant_alunos = len(dataBase)
    if quant_alunos == 0:
        print('Você não tem nenhum aluno para listar, por gentileza escolha outra opção:')
        menuGeral()
    else:
        print('Temos esses alunos cadastrados na base atualmente: ')
        i = 0
        for aluno in dataBase:
            i += 1
            print(f"{i} - {aluno['nome']}")
        while True:  # Valida aluno que vai ser deletado
            try:
                print('Digite o número correspondente ao aluno que deseja deletar: ')
                aluno_deletar = int(input('Pode digitar: '))
                if 0 <= aluno_deletar <= i:
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Dado inválido!')
        while True:
            try:
                nome_aluno_deletar = dataBase[aluno_deletar - 1]['nome']
                print(
                    f'Você confirma a exclusão do usuário: {nome_aluno_deletar}')
                print('1 - Sim\n2 - Não')
                confirma_exclusao = int(input('Pode digitar: '))
                if confirma_exclusao == 1 or confirma_exclusao == 2:
                    dataBase.pop(aluno_deletar - 1)
                    print(f'Aluno {nome_aluno_deletar} foi removido da base!')
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Dado inválido!')


def atualizaAluno():  # Atualiza nome e idade de um aluno!
    quant_alunos = len(dataBase)
    if quant_alunos == 0:
        print('Você não tem nenhum aluno para listar, por gentileza escolha outra opção:')
        menuGeral()
    else:
        print('Temos esses alunos cadastrados na base atualmente: ')
        i = 0
        for aluno in dataBase:
            i += 1
            print(f"{i} - {aluno['nome']}")
        while True:  # Valida aluno que vai ser atualizado
            try:
                print('Digite o número correspondente ao aluno que deseja atualizar: ')
                aluno_atualizar = int(input('Pode digitar: '))
                if 0 <= aluno_atualizar <= i:
                    nome_a_ser_atualizado = dataBase[aluno_atualizar - 1]['nome']
                    idade_a_ser_atualizada = dataBase[aluno_atualizar - 1]['idade']
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Dado inválido!')
        while True:  # Valida opcao que vai ser atualizada
            try:
                print('Qual dado você quer atualizar?')
                print('1 - Nome\n2 - Idade')
                dado_atualizar = int(input('Pode digitar: '))
                if dado_atualizar == 1 or dado_atualizar == 2:
                    dado_a_ser_atualizado = nome_a_ser_atualizado if dado_atualizar == 1 else idade_a_ser_atualizada
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Dado inválido!')
            # Cofirmação de atualização
        if dado_atualizar == 1:
            while True:
                print('Digite nome e sobrenome atualizado do aluno')
                nome_atualizado = input('Pode digitar: ')
                nome_atualizado_splited = nome_atualizado.split(' ')
                if len(nome_atualizado_splited) > 1 and nome_atualizado_splited[1] != '':
                    dado_atualizado = nome_atualizado
                    label = 'nome'
                    break
                else:
                    print('Dado inválido!')
        elif dado_atualizar == 2:
            while True:
                try:
                    print('Digite a idade atualizada do aluno')
                    idade_atualizada = int(input('Pode digitar: '))
                    if idade_atualizada >= 10 and idade_atualizada <= 150:
                        dado_atualizado = idade_atualizada
                        label = 'idade'
                        break
                    else:
                        print('Idade inválida!')
                except ValueError:
                    print('Dado inválido!')
        while True:  # Pede confirmação de atualizacao e atualiza ou não dado
            try:
                print(
                    f'Você confirma a alteração de {dado_a_ser_atualizado} para {dado_atualizado}?')
                print('1 - Sim\n2 - Não')
                confirma_atualizacao = int(input('Pode digitar: '))
                if confirma_atualizacao == 1:
                    atualizando = {label: dado_atualizado}
                    dataBase[aluno_atualizar - 1].update(atualizando)
                    print('Nome atualizado com sucesso!')
                    break
                elif confirma_atualizacao == 2:
                    print(
                        'Entendido! Caso queira alterar mais tarde basta retornar nesse menu :)')
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Dado inválido!')


def cadastraAluno():  # Função para cadastrar aluno
    print('Vamos cadastrar um aluno!')
    while True:  # Valida nome
        try:
            nome = str(input('Digite o nome e sobrenome do aluno: '))
            nome_splited = nome.split(' ')
            if len(nome_splited) > 1 and nome_splited[1] != '':
                break
            else:
                print(
                    'Ops! Parece que você não digitou o sobrenome, por gentileza digite nome e sobrenome do aluno!')
        except ValueError:
            print('Dado inválido!')
    while True:  # Valida idade
        try:
            idade = int(input('Digite a idade do aluno: '))
            if idade >= 10 and idade <= 150:
                break
            else:
                print('Idade inválida')
        except ValueError:
            print('Dado inválido!')

    dataBase.append({'nome': nome, 'idade': idade})
    print(f'O usuário {nome} foi cadastrado com sucesso!')


def listarAlunos():  # Função para listar alunos na tela
    quant_alunos = len(dataBase)
    if quant_alunos == 0:
        print('Você não tem nenhum aluno para listar, por gentileza escolha outra opção:')
        menuGeral()
    print(f'No total temos {quant_alunos} alunos')
    print('Sendo eles')
    for aluno in dataBase:
        nome = aluno.get('nome')
        idade = aluno.get('idade')
        print(f'nome: {nome} | idade: {idade}')


def menuGeral():  # Apresenta opções
    while True:
        try:
            print(
                '1 - Cadastrar usuario\n2 - Listar usuários\n3 - Atualizar usuários\n4 - Deletar usuário')
            opcao = input("Pode digitar: ")
            if opcao == '1':
                cadastraAluno()
                break
            elif opcao == '2':
                listarAlunos()
                break
            elif opcao == '3':
                atualizaAluno()
                break
            elif opcao == '4':
                deletaAluno()
                break
            else:
                print('Opção inválida, digite novamente: ')
        except ValueError:
            print('Dado inválido, digite novamente: ')


def verMais():  # Apresenta menu geral e ver mais
    while True:
        print('Gostaria de ver mais uma opção?')
        print('1 - Sim\n2 - Não')
        try:
            ver_mais = input('Pode digitar: ')
            if ver_mais == '1':
                menuGeral()
            elif ver_mais == '2':
                print('Até a próxima!')
                break
            else:
                print('Opção inválida, digite novamente.')
        except ValueError:
            print('Opção inválida, digite novamente.')


print('Olá seja bem vindo ao meu código!')
print('O que você deseja fazer?')

menuGeral()
verMais()
