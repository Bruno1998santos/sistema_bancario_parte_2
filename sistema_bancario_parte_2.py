# Desafio de Código D.I.O | Bruno Santos 

import time,os

def menu ():
    os.system('cls')
    opção = int (input('''
                       
    \t    MENU
    
    [1] CADASTRAR USUÁRIO                  
    [2] CADASTRAR CONTA
    [3] LISTAR CONTAS                 
    [4] DEPÓSITAR                  
    [5] SACAR                  
    [6] EXTRATO                 
    [7] SAIR
    
    Informe a opção desejada:\t'''))
    return opção

def cadastro (cpf,lista):
    if len(cpf) == 11:
        for dicionario in lista:
            for id,dados in dicionario.items():
                if cpf == id:
                    print ('CPF cadastrado')
                    return
                        
        dados = {
            cpf:
            {'nome':input ('Informe o nome: '),
            'data_nascimento':input ('Informe a data de nascimento: '),
            'endereço':input ('Informe o endereço: ')}}
        print ('Cadastro Realizado com sucesso ! ')
        return dados
    else:
        print ('\nCPF informado não tem 11 dígitos\n')
        
def cadastrar_conta (cpf, agencia, conta, lista):
    for dicionario in lista:
        for id,dados in dicionario.items():
            if id == cpf:
                conta +1
                cadastro = {cpf:{'agencia':agencia,'conta':conta}}
                
                print (cadastro)
                return cadastro
            
    print('CPF não Cadastrado !')    
                
def listar_conta (cpf,lista_contas):
    contas_especificas = {}
    if len(cpf) == 11:
        for dicionario in lista_contas :
            for conta_id, dados_conta in dicionario.items():
                if conta_id == cpf:
                    contas_especificas[conta_id] = dados_conta
                else:        
                    print (f'O CPF não possui contas cadatradas !')
                    
            if contas_especificas:
                    
                for conta_id, dados_conta in contas_especificas.items():
                        # Acessar e imprimir os dados da conta
                        print(f"Conta ID: {conta_id}")
                        print(f"Agência: {dados_conta['agencia']}")
                        print(f"Conta: {dados_conta['conta']}")
                        print("-" * 20)
                       
    else:
        print ('CPF inválido !')                                        

def depositar (saldo, valor):
    if valor > 0 :
        saldo +=valor
        return saldo,valor
    else:
        print ('Valor inválido !')

def extrato(saldo,lista_saques, lista_depositos):
    print (f'SALDO ATUAL : R${saldo:.2f}\n')
    
    print (f'{'='*30}')
    print('\n\tDEPÓSITOS\n')
    if sum (lista_depositos) > 0:
        i = 0
        for  valores in lista_depositos:
            i+=1
            print (f'{i}{'.'*20}R${valores:.2f}')
    else:    
        print ('Sem movimentações')
        
    print (f'{'='*30}')    
                
    print('\n\tSAQUES\n')    
    if sum (lista_saques) >0:
        e = 0
        for saques in lista_saques:
            e +=1
            print (f'{e}{'.'*20}R${saques:.2f}')        
    else:    
        print ('Sem movimentações')               

def sacar (saldo,valor_saque, limite_valor, limite_qtda):
    if limite_qtda < 3:
        if valor_saque <=saldo and valor_saque <=limite_valor:
            saldo-=valor_saque
            limite_qtda +=1
            print ('Saque Realizado !')
            time.sleep(2)
            return saldo,valor_saque,limite_qtda
        
        elif valor_saque > saldo:
            print (f'Saldo Insuficiente. | Saldo atual: R$ {saldo:.2f} !')
            time.sleep(2)
            return saldo,valor_saque == 0,limite_qtda
            
        
        elif valor_saque > limite_valor:
            print (f'Valor de saque ultrapassa o limite de valor de saque.|Limite: R$ {limite_valor:.2f}')
            time.sleep(2)
            return saldo,valor_saque == 0,limite_qtda   
        else:
            print ('Sem Saldo !')
            time.sleep(2)          
            return saldo,0,limite_qtda
    else:
        print('Excedeu o limite de saque!')
        time.sleep(2)      
        return saldo,valor_saque == 0,limite_qtda
def main ():
    
    lista_cadastro = []
    lista_contas = []
    AGENCIA = '0001'
    conta = 20000
    saldo = 0.0
    lista_depositos = []
    lista_saques = []
    limite_valor = 500.00
    limite_qtda = 0
    
    while True:    
    
        
        time.sleep(1)
        
        opcao = menu () # Inicio do Programa - Inicia o MENU e recebe o valor do menu
        
        
        match opcao:
            
            case 1:
                os.system('cls')
                print ('\nCadastro\n')
                cpf=input('Informe o CPF:\t')
                registro = cadastro (cpf,lista_cadastro)
                lista_cadastro.append(registro)

            case 2:
                conta +=1
                os.system('cls')
                print ('\nCADASTRO CONTA\n')
                cpf = input('Informe o CPF:\t')
                cadastro_da_conta = cadastrar_conta(cpf, AGENCIA, conta, lista_cadastro)
                lista_contas.append (cadastro_da_conta)
                       
            case 3:
                os.system('cls')
                print ('\nLISTAR CONTAS\n')
                listar_conta (input('Informe o CPF:\t'),lista_contas)
                           
            case 4: 
                os.system('cls')
                print ('\nDEPÓSITAR\n')
                valor = float (input('Informe o valor do depósito:\t'))
                saldo,deposito = depositar (saldo,valor)
                lista_depositos.append(deposito)

            case 5:
                os.system('cls')
                print ('\nSACAR\n')
                valor_saque = float (input('Informe o valor do saque:\t'))
                saldo,extrato_saque,limite_qtda = sacar (saldo,valor_saque, limite_valor, limite_qtda )
                lista_saques.append(extrato_saque)
                
            case 6:
                os.system('cls')
                print ('\nEXTRATO\n')
                extrato(saldo,lista_saques, lista_depositos)
                time.sleep(2)     
                
            case 7:
                os.system('cls')
                print ('Até mais')
                break
            case _: 
                print ('Opção Inválida')
                
                    
main ()