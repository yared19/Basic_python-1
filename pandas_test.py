import pandas as pd
#list of balances
balances = [ 1000, 2500, 4300, 1200, 5000]
#a pandas series
balance_series = pd.Series(balances, name="Account balance")

print(balances)
print(balance_series[3])
highBalance = balance_series[balance_series>1200]

print(highBalance)

#DataFrame
data = {
    "Customer ID": [101,102,103,104,105],
    "Name": ["Fitsum","Birhanu", "Yared", "Billise",None],
    "Account Balance": [3000,15000, 40000,None, 8000000],
    "Account Type": ["Savings", "Checking",None,"Savings", "Checking"]
 }

#create a data frame
bank_df = pd.DataFrame(data)
print(bank_df)
print(bank_df.head())
print(bank_df[bank_df["Account Balance"]>20000])
print(bank_df[["Name", "Account Balance"]])
bank_df["Interet Earned"] = bank_df["Account Balance"] * 0.075
print(bank_df)
bank_df.loc[bank_df["Name"]=="Billise","Account Type"] = "Premium Savings"
print(bank_df) 

#check if there are missing data
print(bank_df.isnull())

print(bank_df.isnull().sum())

#dropping the missing data row
bank_df_dropped = bank_df.dropna()
print(bank_df_dropped)

# Filling missing account balances with 0

bank_df["Account Balance"].fillna(0, inplace=True)
# Filling missing names with "Unknown"
bank_df["Name"].fillna("Unknown", inplace=True)
print(bank_df)

# Forward fill for Account Type
bank_df["Account Type"].fillna(method="ffill", inplace=True)
print(bank_df)

bank_df["Account Balance"]=bank_df["Account Balance"].astype(float)
print(bank_df)

# Binning account balances
bins = [0, 1000, 30000, 50000, 10000000]
labels = ["Low", "Medium", "High", "Premium"]
bank_df["Balance Category"] = pd.cut(bank_df["Account Balance"],
bins=bins, labels=labels)
print(bank_df)

# Normalizing Account Balance (0-1 range)
bank_df["Normalized Balance"] = (bank_df["Account Balance"] -
bank_df["Account Balance"].min()) / (bank_df["Account Balance"].max() - bank_df["Account Balance"].min())
print(bank_df)
