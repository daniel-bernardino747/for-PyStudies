class User:
    info_user = dict()
    database = list()

    def __init__(self, nameu, cpfu, ageu, salaryu):
        self.name = nameu
        self.cpf = cpfu
        self.age = ageu
        self.salary = salaryu

    def add_user(self, infos_users):
        self.info_user['Name'] = infos_users.name
        self.info_user['CPF'] = infos_users.cpf
        self.info_user['Age'] = infos_users.age
        self.info_user['Salary'] = infos_users.salary
        self.database.append(self.info_user.copy())
        self.info_user.clear()


class Seller(User):
    def __init__(self, nameu, cpfu, ageu, salaryu, sales_amount):
        super().__init__(nameu, cpfu, ageu, salaryu)
        self.all_sales = 0
        self.all_sales += sales_amount

    def describe(self):
        print(self.name)
        print(self.cpf)
        print(self.age)
        print(self.salary)
        print(self.all_sales)


while True:
    name = str(input('Username: '))
    cpf = str(input('CPF: '))
    age = int(input('Age: '))
    salary = float(input('Salary: '))
    user01 = User(name, cpf, age, salary)
    User.add_user(user01, user01)
    sales = int(input('Inform the sales amount at the last visit in program: '))
    user02 = Seller(name, cpf, age, salary, sales)
    decide = str(input('Continue? '))
    if decide in 'Yy':
        pass
    else:
        break

print(user01.name, user01.cpf, user01.age, user01.salary)
print(User.info_user)
print(User.database)
user02.describe()
# s1 = Secretary()
# v1 = Seller()

# print(s1.show_cpf())
# print(v1.show_cpf())

