import Entrada_loja
import  Funcionario_loja
import Produto
def Menu_loja_Funcionario(nome_funcionario):
    print("__"*40)
    print("___ Clowns_Black_Store_RH ___".center(80))
    print("__"*40)
    print("< [1] Estoque_Da_Loja > < [2] Caixa_Vendas > < [3] Cadastro_Novos_Funcionario >")
    print("            < [4] Cadastro_Novos_Produtos > < [5] Retorna_Menu >            ")
    print(f"(Funcionario > {nome_funcionario})")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    escolha_funcionario = int(input("<<< Escolher uma opção acima >>>"))
    if(escolha_funcionario == 1):
                while(True):
                    with open("funcoes_estoques\estoques.txt", "r")as estoques:
                        estoques = estoques.read()
                        estoques = estoques.split("\n")
                        for decer in range(len(estoques)):
                            if (decer % 1 == 0):
                                try:
                                    print("__" * 50)
                                    print("___ Clowns_Black_Store_Estoque ___".center(100))
                                    print("__" * 50)
                                    print("< [1] Decer Barrinha > < [2] Sair".center(100))
                                    print("__"*50)
                                    print(f"<<< {estoques[decer+1]} >>>")
                                    print(f"<<< {estoques[decer+2]} >>>")
                                    print(f"<<< {estoques[decer+3]} >>>")
                                    print(f"<<< {estoques[decer+4]} >>>")
                                    print(f"<<< {estoques[decer+5]} >>>")
                                    print("__"*20)
                                except IndexError:
                                    print("<<< Erro 666 >>> Acabou os produtos ".center(100))
                                escolha_usuario = int(input("<<< Escolha Uma Opção acima >>> "))
                                if(escolha_usuario == 1):
                                    True
                                elif(escolha_usuario == 2):
                                    Menu_loja_Funcionario(nome_funcionario)

    elif(escolha_funcionario == 2):
        print("não tem")
    elif(escolha_funcionario == 3):
                    while(True):
                        print("__" * 40)
                        print("___ Clowns_Black_Store_RH___".center(100))
                        print("__" * 40)
                        print("")
                        print("")
                        nome_digitado = str(input("<<< Digite nome Funcionario >>> ".upper()))
                        print("")
                        print("")
                        carteira_digitada = int(input("<<< Digite Carteira De Trabalho >>> "))
                        print("")
                        print("")
                        setor_funcionario = str(input("<<< Digite Setor Do Funcionario >>> "))
                        print("")
                        print("")
                        with open(f"funcionario_registrado\{nome_digitado}.txt", "r") as banco_funcionarios:
                            banco_funcionarios = banco_funcionarios.read()
                            banco_funcionarios = banco_funcionarios.split("\n")
                        if(nome_digitado,carteira_digitada,setor_funcionario in banco_funcionarios):
                            print("<<< Esse Funcionario ja esta Trabalhando na Clowns_Black_Store >>> ")
                            True
                        else:
                            Funcionario_loja.funcionario(_nome_funcionario=f"{nome_digitado}",_carteira_de_trabalho=f"{carteira_digitada}",_setor=f"{setor_funcionario}")
    elif (escolha_funcionario == 4):
        print("__" * 40)
        print("___ Clowns_Black_Store_Estoque ___".center(80))
        print("__" * 40)
        nome_produto = str(input("<<< Nome do produto >>> "))
        cor_produto = str(input(f"<<< Cor do {nome_produto} >>> "))
        preco_produto = float(input(f"<<< Preço do {nome_produto} >>> "))
        print(f"<<< A Referencia nâo pode ser igual de outro produto coloque {nome_produto} é numero para referencia >>>")
        referencia_produto = str(input(f"<<< Digite referencia do {nome_produto} >>> "))
        while(True):
            print("<<< ([1]moda_intima) - ([2]moda_masculino) - ([3]moda_feminino) - ([4]moda_infantil) - ([5]moda_cama_mesa_banho) >>>")
            departamento_produto = int(input(f"<<< Digite departamento do {nome_produto} >>> "))
            if(departamento_produto == 1):
                departamento_produto = "moda_intima"
            elif(departamento_produto == 2):
                departamento_produto = "moda_masculino"
            elif(departamento_produto == 3):
                departamento_produto = "moda_feminino"
            elif(departamento_produto == 4):
                departamento_produto = "moda_infantil"
            elif(departamento_produto == 5):
                departamento_produto = "moda_cama_mesa_banho"
            else:
                print("<<< Digite Numero do departamento >>>")
                continue
            contidade_produto = int(input(f"<<< Digite contidade do {nome_produto} >>> "))
            Produto.produto(nome_produto,cor_produto, preco_produto, referencia_produto, departamento_produto, contidade_produto)
            Menu_loja_Funcionario(nome_funcionario)
    elif(escolha_funcionario == 5):
        Entrada_loja.inicio_loja()



