confirmação = 'S'
planilha_produto = []
produtos_adicionados = 0
print('-' *28)
print('BAR DO RAIMUNDO - APLICATIVO')
print('-' *28)

while confirmação in 'Ss':
    print('''
Digite o número correspondente para cada ação.
[ 1 ] - ADICIONAR ESTOQUE DE PRODUTO
[ 2 ] - VER PRODUTOS ADICIONADOS
[ 3 ] - ADICIONAR INADIPLENTES
[ 4 ] - VER INADIPLENTES
''')
    escolha = int(input(''))


    if escolha == 1:
        produto = input('Digite o nome do produto: ')
        quantidade_produto = int(input('Digite a quantidade que você comprou: '))
        valor_produto = float(input('Digite o valor do produto: (EM UNIDADE) R$'))
        valor_conjunto = valor_produto * quantidade_produto
        print(f'No total, foi gasto {valor_conjunto} na compra de {quantidade_produto} {produto}.')
        print('Produto adicionado á planilha com sucesso!')
        confirmação = input('Deseja continuar? [sim / não]').lower()
        planilha_produto = produto
        produtos_adicionados += 1
        

    if escolha == 2:
        for compras in range(0, produtos_adicionados):
            print(f'''      
PRODUTOS: {planilha_produto}
PREÇO: {valor_conjunto}
QUANTIDADE: {quantidade_produto}
PRINT: {planilha_produto}''')


        
# NÃO ESTÁ ACABADO.