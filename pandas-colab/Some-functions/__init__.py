import pandas as pd
import numpy as np

"""df_2 = pd.DataFrame(
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
display(df_2.describe(include='number')) # print(df_2.describe(include='number'))
display(df_2.describe(include='object')) # print(df_2.describe(include='object'))
display(df_2.describe(include='all')) # print(df_2.describe(include='all'))"""

df1 = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
print(df1)
df1.idxmax()

df2 = pd.DataFrame(
    {"col1": np.random.randn(3), "col2": np.random.randn(3), "col3": np.random.randn(3)}, index=["a", "b", "c"]
)
print(df2)

for col, ser in df2.iterrows():
    print(col)
    print(ser[0])

for col, ser in df2.items():
    print(col)
    print(ser[0])
