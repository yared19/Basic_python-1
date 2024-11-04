import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

path = kagglehub.dataset_download("henriqueyamahata/bank-marketing")
print("Downloaded to:", path)

data = pd.read_csv(path+"/bank-additional-full.csv",sep=";")

df=pd.DataFrame(data)