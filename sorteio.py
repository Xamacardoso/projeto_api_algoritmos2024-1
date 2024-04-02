import os, time, random

def main():
    arquivo = open('alunos-algoritmos-20241.csv', 'r')
    linhas = arquivo.readlines() # linhas recebe ['item1\n', item2\n'...]
    alunos = []
    for aluno in linhas:
        alunos.append(aluno.rstrip()) # adiciona cada aluno à lista alunos sem o \n

    arquivo.close()
    lista_grupos = []

    opcao = ''

    while opcao != '0':
        os.system('cls')
        print(f'''
        1 - (Re)Carregar alunos
        2 - Excluir aluno
        3 - (Re)Sortear grupos
        4 - Listar alunos que serão sorteados
        5 - Listar Grupos
        6 - Gravar resultado em arquivo
        0 - Sair
            
        Alunos disponíveis para sorteio: {len(alunos)}
        ''')

        opcao = str(input('>>> Qual a sua opção: '))
        os.system('cls')
        # Recarregar ou carregar a lista de alunos
        if opcao == '1':
            
            print('Carregando Alunos...')
            time.sleep(1)

            # carrega todos os alunos que estao NO ARQUIVO CSV
            arquivo = open('alunos-algoritmos-20241.csv', 'r')
            linhas = arquivo.readlines()
            alunos = []
            for aluno in linhas:
                alunos.append(aluno.rstrip())
            arquivo.close()

            print('Lista de alunos carregada!')
            time.sleep(0.7)
            os.system('cls')

        # excluir um ou mais alunos
        elif opcao == '2':
            
            excluir_outro = 's'
            while excluir_outro.lower() == 's':
                os.system('cls')
                indice = 0
                # mostra todos os alunos disponiveis para sorteio
                for indice in range(len(alunos)):
                    print(f'{indice+1}: {alunos[indice]}')
                
                print('\nQual aluno deseja excluir? (Digite o número correspondente ao aluno, que aparece na tela) ')
                escolha = int(input()) # usuario escolhe o numero do aluno
                del alunos[escolha-1] # deleta o aluno da lista de disponiveis
                
                print('Aguarde...')
                time.sleep(0.5)
                print('Aluno excluído com sucesso!')

                excluir_outro = str(input('Deseja excluir outro aluno? (s/n) '))
                while excluir_outro.lower() != 's' and excluir_outro.lower() != 'n':
                    print('Digite uma opção válida! (s ou n)')
                    excluir_outro = str(input('Deseja excluir outro aluno? (s/n) '))
                
                os.system('cls')
                
            
        # Sortear grupos
        elif opcao == '3':
            
            # cria uma copia da lista de alunos, para eu ter o original intacto se eu modificar aux
            aux = alunos[:]

            # se o usuario botar que sejam menos de 1 grupo ou mais grupos que a quantidade de pessoas, esse bloco é exibido
            quantidade_grupos = int(input('Quantos grupos deseja? '))
            if quantidade_grupos > len(aux) or quantidade_grupos < 1:
                print('Quantidade de grupos inválida!! Digite um valor que seja maior que 0 e menor que o tamanho da lista de alunos!')
                quantidade_grupos = int(input('Quantos grupos deseja? '))

            divisao_grupos = len(aux) // quantidade_grupos
            
            # esvazia a lista de grupos, possibilitando o 're-sorteio'
            lista_grupos = []

            # para cada grupo
            for i in range(quantidade_grupos):
                grupo = []
                # se for o ultimo grupo, pega as pessoas que faltam e botam nele
                if i+1 == quantidade_grupos:
                    for integrantes in range(len(aux)):
                        sorteado = random.choice(aux) # escolhe uma pessoa aleatória
                        grupo.append(sorteado) # bota no grupo que ta sendo trabalhado
                        aux.remove(sorteado) # remove a pessoa da lista auxiliar

                # se nao for o ultimo grupo, pega o número necessario e botam nele. ex: 21/4 ficam grupos de 5 pessoas
                else:
                    for integrantes in range(divisao_grupos):
                        sorteado = random.choice(aux)
                        grupo.append(sorteado)
                        aux.remove(sorteado)
                        
                lista_grupos.append(sorted(grupo))
            
            print('Sorteando...')
            time.sleep(1)
            print('Grupos sorteados!')
            time.sleep(0.75)
            os.system('cls')
        
        # ver alunos que participarão do sorteio
        elif opcao == '4':
            
            print('Alunos que participarão, ordenados por nome:\n')
            indice_alunos = 1

            # mostra todos os alunos ainda disponiveis, 1 aluno por linha em ordem alfabetica
            for aluno in sorted(alunos):
                print(f'{indice_alunos} - {aluno}')
                indice_alunos += 1

            input('\nPressione ENTER para sair...')
            os.system('cls')

        # ver grupos
        elif opcao == '5':
        
            # caso ainda nao exista nenhum grupo formado, nada acontece no sorteio
            if lista_grupos == []:
                print('Nenhum grupo foi sorteado ainda!')
                input('Pressione ENTER para sair...')
                os.system('cls')

            else:  
                os.system('cls')   
                print('======== G R U P O S ========\n')
                
                # mostra em qual grupo está
                for grupos in range(len(lista_grupos)):
                    print(f'- G R U P O  {grupos+1} -\n')
                    # mostra os integrantes de cada grupo em ordem
                    for integrante in range(len(lista_grupos[grupos])):
                        print(f'{integrante+1} - {lista_grupos[grupos][integrante]}')
                        
                        # se o integrante for o ultimo, ele quebra a linha
                        if integrante+1 == len(lista_grupos[grupos]):
                            print('')

                input('Pressione ENTER para sair...')
                os.system('cls')



        # gravar em arquivo
        elif opcao == '6':

            if lista_grupos == []:
                print('Nenhum grupo foi sorteado ainda!')
                input('Pressione ENTER para sair...')
                os.system('cls')

            else:    
                print('Gravando resultado em arquivo...')
                resultado = open('resultado.txt', 'w')
                # mostra em qual grupo está
                for grupos in range(len(lista_grupos)):
                    resultado.write(f'- G R U P O  {grupos+1} -\n')
                    resultado.write('\n')
                    # mostra os integrantes de cada grupo em ordem
                    for integrante in range(len(lista_grupos[grupos])):
                        resultado.write(f'{integrante+1} - {lista_grupos[grupos][integrante].rstrip()} -\n')
                        
                        # se o integrante for o ultimo, ele quebra a linha
                        if integrante+1 == len(lista_grupos[grupos]):
                            resultado.write('\n')

                resultado.close()

                time.sleep(0.7)
                print('Arquivo gravado com sucesso!')
                input('Pressione ENTER para sair...')
                os.system('cls')

        # sair
        elif opcao == '0':
            print('>>> Saindo...')
            time.sleep(0.2)

        else:
            print('>>> Opção Inválida! <<<')
            input('Pressione ENTER para sair...')

main()
