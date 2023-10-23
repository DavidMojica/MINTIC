#Usar el cmd -> pip install pandas
import pandas as pd
data = {'Name':["David", "Yen", "Mateo", "Javier"], 'Age': [22,19,18,20]}
df = pd.DataFrame(data)
print(df)
#Output
#       Name  Age
# 0    David   22
# 1      Yen   19
# 2    Mateo   18
# 3  Javier   20