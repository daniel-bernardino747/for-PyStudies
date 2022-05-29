# Vamos criar uma classe para Clientes da Netflix
class Cliente:
    def __init__(self, name, email, plan):
        self.name = name
        self.email = email
        lista_planos = ['basic', 'premium']
        if plan in lista_planos:
            self.plan = plan
        else:
            raise Exception('Plano inválido')


cliente0003 = Cliente('Lira', 'lira@gmail.com', 'sd')
print(cliente0003.name)
