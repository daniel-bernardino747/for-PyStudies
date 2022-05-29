# __init__ precisa colocar as características do controle remoto
# __init__ são as informações básicas para criar

# self ele faz refêrencia à classe, ao controle remoto
class ControleRemoto:
    def __init__(self, cor='preto', altura='16cm', profundidade='2.5cm', largura='4.6cm'):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        # O self criou um atributo do ControleRemoto

    def passar_canal(self, botao):
        if botao == '+':
            print('Passar para próximo canal')
        elif botao == '-':
            print('Passar para canal anterior')


controle_remoto1 = ControleRemoto()
print(controle_remoto1.cor)
controle_remoto1.passar_canal('+')
print()

# esse controle_remoto1 é uma instância da classe do controleremoto()
controle_remoto2 = ControleRemoto('cinza')
print(controle_remoto2.cor)
controle_remoto2.passar_canal('-')
