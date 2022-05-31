class User:
    status = 'manager account'
    account = 'PREMIUM'

    def __init__(self, nameUser, ageUser):
        self.name = nameUser
        self.age = ageUser

    def show_setting(self):
        print('Showing Settings.')

    @classmethod
    def not_show_setting(cls):
        print('Not showing settings.')

    @classmethod
    def show_status(cls):
        print(cls.status, end=' | ')
        print(cls.account)

    @staticmethod # Assistant Method
    def is_adult():
        try:
            if ageOBSERVE >= 18:
                print('This user is adult.')
            else:
                print('This user not is adult.')
        except NameError:
            pass


resp = input('([Yes]/No): ')
if resp in 'Yy':
    # User.show_setting() # It won't work because it needs the self parameter
    name = str(input('Digite o nome: '))
    ageOBSERVE = int(input('Digite a idade: '))
    user1 = User(name, ageOBSERVE)
    print('The user', user1.name, 'have', user1.age, 'years old.')
else:
    User.not_show_setting()

print(f'Status is :', end=' ')
User.show_status()
User.is_adult()
