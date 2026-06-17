def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
        

def calcular_idade(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento


def calcular_aposentadoria(ano_contrato, idade_atual):
    anos_trabalhados = calcular_idade(ano_contrato)
    anos_para_aposentadoria = 35 - anos_trabalhados
    idade_aposentadoria = idade_atual + anos_para_aposentadoria
    return idade_aposentadoria


def mostrar_dados(dados):
    print('-=' * 30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
    print('-=' * 30)


def cadastrar_trabalhador():
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    dados['nascimento'] = leiaint('Ano de Nascimento: ')
    dados['CTPS'] = leiaint('Número da CTPS (se não tiver, escreva 0): ')
    dados['idade'] = calcular_idade(dados['nascimento'])

    if dados['CTPS'] != 0:
        dados['ano_contrato'] = leiaint('Ano da Contratação: ')
        dados['salario'] = float(input('Digite o seu salário: R$'))
        dados['aposentadoria'] = calcular_aposentadoria(
            dados['ano_contrato'],
            dados['idade']
        )

    return dados