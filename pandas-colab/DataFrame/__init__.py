import pandas as pd

"""database = dict()
names = list()
ages = list()
emails = list()

for a in range(0, 1):
  name = str(input('Name: '))
  age = int(input('Age: '))
  email = str(input('E-mail: '))
  names.append(name)
  ages.append(age)
  emails.append(email)

database['Name'] = names[:]
database['Age'] = ages[:]
database['E-mail'] = emails[:]
df_1 = pd.DataFrame(database)
display(df_1) # print(df_1)"""

df_2 = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df_2)
