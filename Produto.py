import Caixa_Vendas
class produto():
    def __init__(self,nome_produto,cor,preco,referencia,departamento,quantidade):
        self._nome_produto = nome_produto
        self._cor = cor
        self._referencia = referencia
        self._preco = preco
        self._derpartamento = departamento
        self._quantidade  = quantidade
        with open(f"estoques\\referencia.txt", "a")as produto_novo8:
            produto_novo8.write(f"\nreferencia:({referencia})")
        with open(f"estoques\\preco.txt", "a")as produto_novo9:
            produto_novo9.write(f"\npreço:({preco})")
        with open(f"estoques\\quantidade.txt", "a")as produto_novo10:
            produto_novo10.write(f"\nquantidade:({quantidade})")
        with open(f"funcoes_estoques\\referencia_preco.txt", "a")as produto_novo1:
            produto_novo1.write(f"\nreferencia:({referencia}),preço:({preco})")
        with open(f"funcoes_estoques\estoques.txt","a")as produto_novo:
            produto_novo.write(f"\nnome:({nome_produto}),cor:({cor}),preço:({preco}),referencia:({referencia}),departamento:({departamento}))")
        print("<<< Produto cadastrado com sucesso >>> ")
        if(departamento == "moda_intima"):
            with open(f"funcoes_estoques\moda_intima.txt", "a")as produto_novo:
                produto_novo.write(f"\nnome:({nome_produto}),cor:({cor}),preço:({preco}),referencia:({referencia})")
        if(departamento == "moda_masculino"):
            with open(f"funcoes_estoques\moda_masculino.txt", "a")as produto_novo:
                produto_novo.write(f"\nnome:({nome_produto}),cor:({cor}),preço:({preco}),referencia:({referencia})")
        if (departamento == "moda_feminino"):
            with open(f"funcoes_estoques\moda_feminino.txt", "a")as produto_novo:
                produto_novo.write(f"\nnome:({nome_produto}),cor:({cor}),preço:({preco}),referencia:({referencia})")
        if (departamento == "moda_infantil"):
            with open(f"funcoes_estoques\moda_infantil.txt", "a")as produto_novo:
                produto_novo.write(f"\nnome:({nome_produto}),cor:({cor}),preço:({preco}),referencia:({referencia})")
        if (departamento == "moda_cama_mesa_banho"):
            with open(f"funcoes_estoques\moda_cama_mesa_banho.txt", "a")as produto_novo:
                produto_novo.write(f"\nnome:({nome_produto}),preço:({preco}),referencia:({referencia})")
