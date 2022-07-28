class funcionario():
    def __init__(self,_nome_funcionario="DANILO",_carteira_de_trabalho="32553257",_setor="GERENCIA"):
        self.__nome_funciionario_ = _nome_funcionario
        self.__carteira_de_trabalho_ = _carteira_de_trabalho
        self.__setor_ = _setor
        with open(f"funcionario_registrado\{_nome_funcionario}txt","a",encoding="utf8")as registrando_funcionario:
            registrando_funcionario.write(f"\n{_nome_funcionario}\n{_carteira_de_trabalho}\n{_setor}\n")
        print(f"<<< Funcionario {_nome_funcionario} registrado com sucesso")








