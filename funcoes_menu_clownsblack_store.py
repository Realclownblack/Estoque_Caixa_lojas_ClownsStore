import Caixa_Vendas
import Entrada_loja
import Loja_clownblack
def loja_compras():
    cesta_produtos = []
    print("__" * 40)
    print("___ Clowns_Black_Store ___".center(80))
    print("__" * 40)
    print("<<< ([1]moda_intima) - ([2]moda_masculino) - ([3]moda_feminino) - ([4]moda_infantil) - ([5]moda_cama_mesa_banho) >>>")
    escolha_cliente = int("<<< Digite um departamento >>> ")
    if(escolha_cliente == 1):
        print("( <<< moda_intima >>> )".upper())
        while (True):
            with open("estoques\moda_intima.txt", "r") as estoques:
                estoques = estoques.read()
                estoques = estoques.split("\n")
                for decer in range(len(estoques)):
                    if (decer % 1 == 0):
                        try:
                            print("__" * 50)
                            print("___ Clowns_Black_Store_Estoque ___".center(100))
                            print("__" * 50)
                            print("< [1] Decer Barrinha > < [2] Ver cesta > < [3] Sair".center(100))
                            print("__" * 50)
                            print(f"<<< {estoques[decer + 1]} >>>")
                            print(f"<<< {estoques[decer + 2]} >>>")
                            print(f"<<< {estoques[decer + 3]} >>>")
                            print(f"<<< {estoques[decer + 4]} >>>")
                            print(f"<<< {estoques[decer + 5]} >>>")
                            print("__" * 20)
                        except IndexError:
                            print("<<< Erro 666 >>> Acabou os produtos ".center(100))
                        escolha_cliente = int(input("<<< Escolha Referencia do produto para por na cesta >>> "))
                        if (escolha_cliente == 1):
                            continue
                        elif (escolha_cliente == 2):
                            for i in range(len(cesta_produtos)):
                                print(f"{i} >>> {cesta_produtos}")
                            escolha_cliente1 = str(input("Continuar vendo [s] ou finalizar compra [f]".upper()))
                            if(escolha_cliente1 == 'S'):
                                continue
                            elif(escolha_cliente1 == 'F'):
                                Caixa_Vendas.finalizar_compra(cesta_produtos)

                        elif(escolha_cliente in estoques):
                            cesta_produtos.append(escolha_cliente)
                            continue
                        elif(escolha_cliente == 3):
                            Entrada_loja.inicio_loja()
    elif(escolha_cliente == 2):
        print("( <<< moda_masculino >>> )".upper())
        while (True):
            with open("estoques\moda_masculino.txt", "r") as estoques:
                estoques = estoques.read()
                estoques = estoques.split("\n")
                for decer in range(len(estoques)):
                    if (decer % 1 == 0):
                        try:
                            print("__" * 50)
                            print("___ Clowns_Black_Store_Estoque ___".center(100))
                            print("__" * 50)
                            print("< [1] Decer Barrinha > < [2] Ver cesta > < [3] Sair".center(100))
                            print("__" * 50)
                            print(f"<<< {estoques[decer + 1]} >>>")
                            print(f"<<< {estoques[decer + 2]} >>>")
                            print(f"<<< {estoques[decer + 3]} >>>")
                            print(f"<<< {estoques[decer + 4]} >>>")
                            print(f"<<< {estoques[decer + 5]} >>>")
                            print("__" * 20)
                        except IndexError:
                            print("<<< Erro 666 >>> Acabou os produtos ".center(100))
                        escolha_cliente = int(input("<<< Escolha Referencia do produto para por na cesta >>> "))
                        if (escolha_cliente == 1):
                            continue
                        elif (escolha_cliente == 2):
                            for i in range(len(cesta_produtos)):
                                print(f"{i} >>> {cesta_produtos}")
                            escolha_cliente1 = str(input("Continuar vendo [s] ou finalizar compra [f]".upper()))
                            if(escolha_cliente1 == 'S'):
                                continue
                            elif(escolha_cliente1 == 'F'):
                                Caixa_Vendas.finalizar_compra(cesta_produtos)
                        elif(escolha_cliente in estoques):
                            cesta_produtos.append(escolha_cliente)
                            continue
                        elif(escolha_cliente == 3):
                            Entrada_loja.inicio_loja()
    elif(escolha_cliente == 3):
        print("( <<< moda_feminina >>> )".upper())
        while (True):
            with open("estoques\moda_feminina.txt", "r") as estoques:
                estoques = estoques.read()
                estoques = estoques.split("\n")
                for decer in range(len(estoques)):
                    if (decer % 1 == 0):
                        try:
                            print("__" * 50)
                            print("___ Clowns_Black_Store_Estoque ___".center(100))
                            print("__" * 50)
                            print("< [1] Decer Barrinha > < [2] Ver cesta > < [3] Sair".center(100))
                            print("__" * 50)
                            print(f"<<< {estoques[decer + 1]} >>>")
                            print(f"<<< {estoques[decer + 2]} >>>")
                            print(f"<<< {estoques[decer + 3]} >>>")
                            print(f"<<< {estoques[decer + 4]} >>>")
                            print(f"<<< {estoques[decer + 5]} >>>")
                            print("__" * 20)
                        except IndexError:
                            print("<<< Erro 666 >>> Acabou os produtos ".center(100))
                        escolha_cliente = int(input("<<< Escolha Referencia do produto para por na cesta >>> "))
                        if (escolha_cliente == 1):
                            continue
                        elif (escolha_cliente == 2):
                            for i in range(len(cesta_produtos)):
                                print(f"{i} >>> {cesta_produtos}")
                            escolha_cliente1 = str(input("Continuar vendo [s] ou finalizar compra [f]".upper()))
                            if (escolha_cliente1 == 'S'):
                                continue
                            elif (escolha_cliente1 == 'F'):
                                Caixa_Vendas.finalizar_compra(cesta_produtos)
                        elif (escolha_cliente in estoques):
                            cesta_produtos.append(escolha_cliente)
                            continue
                        elif (escolha_cliente == 3):
                            Entrada_loja.inicio_loja()
    elif(escolha_cliente == 4):
        print("( <<< moda_infantil >>> )".upper())
        while (True):
            with open("estoques\infantil.txt", "r") as estoques:
                estoques = estoques.read()
                estoques = estoques.split("\n")
                for decer in range(len(estoques)):
                    if (decer % 1 == 0):
                        try:
                            print("__" * 50)
                            print("___ Clowns_Black_Store_Estoque ___".center(100))
                            print("__" * 50)
                            print("< [1] Decer Barrinha > < [2] Ver cesta > < [3] Sair".center(100))
                            print("__" * 50)
                            print(f"<<< {estoques[decer + 1]} >>>")
                            print(f"<<< {estoques[decer + 2]} >>>")
                            print(f"<<< {estoques[decer + 3]} >>>")
                            print(f"<<< {estoques[decer + 4]} >>>")
                            print(f"<<< {estoques[decer + 5]} >>>")
                            print("__" * 20)
                        except IndexError:
                            print("<<< Erro 666 >>> Acabou os produtos ".center(100))
                        escolha_cliente = int(input("<<< Escolha Referencia do produto para por na cesta >>> "))
                        if (escolha_cliente == 1):
                            continue
                        elif (escolha_cliente == 2):
                            for i in range(len(cesta_produtos)):
                                print(f"{i} >>> {cesta_produtos}")
                            escolha_cliente1 = str(input("Continuar vendo [s] ou finalizar compra [f]".upper()))
                            if (escolha_cliente1 == 'S'):
                                continue
                            elif (escolha_cliente1 == 'F'):
                                Caixa_Vendas.finalizar_compra(cesta_produtos)
                        elif (escolha_cliente in estoques):
                            cesta_produtos.append(escolha_cliente)
                            continue
                        elif (escolha_cliente == 3):
                            Entrada_loja.inicio_loja()
    elif(escolha_cliente == 5):
        print("( <<< moda_cama_mesa_banho >>> )".upper())
        while (True):
            with open("estoques\moda_cama_mesa_banho.txt", "r") as estoques:
                estoques = estoques.read()
                estoques = estoques.split("\n")
                for decer in range(len(estoques)):
                    if (decer % 1 == 0):
                        try:
                            print("__" * 50)
                            print("___ Clowns_Black_Store_Estoque ___".center(100))
                            print("__" * 50)
                            print("< [1] Decer Barrinha > < [2] Ver cesta > < [3] Sair".center(100))
                            print("__" * 50)
                            print(f"<<< {estoques[decer + 1]} >>>")
                            print(f"<<< {estoques[decer + 2]} >>>")
                            print(f"<<< {estoques[decer + 3]} >>>")
                            print(f"<<< {estoques[decer + 4]} >>>")
                            print(f"<<< {estoques[decer + 5]} >>>")
                            print("__" * 20)
                        except IndexError:
                            print("<<< Erro 666 >>> Acabou os produtos ".center(100))
                        escolha_cliente = int(input("<<< Escolha Referencia do produto para por na cesta >>> "))
                        if (escolha_cliente == 1):
                            continue
                        elif (escolha_cliente == 2):
                            for i in range(len(cesta_produtos)):
                                print(f"{i} >>> {cesta_produtos}")
                            escolha_cliente1 = str(input("Continuar vendo [s] ou finalizar compra [f]".upper()))
                            if (escolha_cliente1 == 'S'):
                                continue
                            elif (escolha_cliente1 == 'F'):
                                Caixa_Vendas.finalizar_compra(cesta_produtos)
                        elif (escolha_cliente in estoques):
                            cesta_produtos.append(escolha_cliente)
                            continue
                        elif (escolha_cliente == 3):
                            Entrada_loja.inicio_loja()
def cadastra_curriculo():
    print("__" * 40)
    print("___ Clowns_Black_Store_RH___".center(80))
    print("__" * 40)
    print("")
    nome = str(input(" <<< Digite seu nome >>> "))
    data = int(input(" <<< Digite Data De Nacimento >>> "))
    curriculo = str(input(" <<< Digite Seu Curriculo >>> "))
    with open(f"curriculos\{nome}.txt","a")as curriculo_mandar:
        curriculo_mandar.write(f"({nome} minha data de nacimento {data})\n{curriculo}")
        return 0
def login_funcionario():
    print("__" * 40)
    print("___ Clowns_Black_Store_RH ___".center(80))
    print("__" * 40)
    print("<<< Login >>> ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    nome_login = str(input("<<< Digite seu login >>> ").upper())
    carteira_login = int(input("<<< Digite sua carteira De Trabalho >>> "))
    with open(f"funcionario_registrado\{nome_login}.txt", "r", encoding="utf8")as login_funcionario:
        login_funcionario = login_funcionario.read()
        login_funcionario = login_funcionario.split("\n")
        if (nome_login, carteira_login in login_funcionario):
            Loja_clownblack.Menu_loja_Funcionario(nome_login)