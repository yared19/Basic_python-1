import kagglehub
import pandas as pd

path = kagglehub.dataset_download("henriqueyamahata/bank-marketing")
print("Downloaded to:", path)

data = pd.read_csv(path+"/bank-additional-full.csv",sep=";")

df=pd.DataFrame(data)

print(df.head())

print(df.isnull().sum())


