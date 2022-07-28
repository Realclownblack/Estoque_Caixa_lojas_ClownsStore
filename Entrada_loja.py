
import funcoes_menu_clownsblack_store
def inicio_loja():
    print("__"*55)
    print("🤡 Clowns_Black_Store                                      🛍️[1]Store - RH[2]Trabalar_conosco - 🔒[3]Login")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    print("                                                                                                          ")
    escolha_usuario = int(input("<<< Escolha uma opção acima >>> "))
    if(escolha_usuario == 1):
        funcoes_menu_clownsblack_store.loja_compras()
    elif(escolha_usuario == 2):
        funcoes_menu_clownsblack_store.cadastra_curriculo()
    elif(escolha_usuario == 3):
        funcoes_menu_clownsblack_store.login_funcionario()

if __name__ == '__main__':
    inicio_loja()