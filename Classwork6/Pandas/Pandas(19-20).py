import pandas as pd
import random
df = pd.DataFrame({"Столбец 1": [random.randint(-10,11) for _ in range(2)], "Столбец 2":[random.randint(-10,11) for _ in range(2)]}, index=['Число 1', "Число 2"])
df['Столбец 3']=df["Столбец 1"]+df["Столбец 2"]
df['Столбец 4']=df[:].mean(axis=1)
print(df)