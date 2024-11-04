import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Sample data: Monthly transaction amounts in a bank
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Transaction Amount': [20000, 25000, 22000, 27000, 28000,
30000, 31000, 35000, 33000, 36000, 34000, 37000]}
#calculate equation for trendline
month=[0,1,2,3,4,5,6,7,8,9,10,11]
df = pd.DataFrame(data)
z = np.polyfit(month, df["Transaction Amount"], 1)
p = np.poly1d(z)
# Plotting
plt.plot(df['Month'], df['Transaction Amount'], marker='o',
linestyle='-', color='b')
plt.plot(month, p(month),
linestyle='-', color='r')
plt.title('Monthly Transaction Amounts')
plt.xlabel('Month')
plt.ylabel('Transaction Amount ($)')
plt.grid(False)
plt.show()

data = {'Account Type': ['Savings', 'Checking', 'Credit', 'Loan'],
'Number of Accounts': [15000, 10000, 5000, 3000]}
df = pd.DataFrame(data)
# Plotting
plt.bar(df['Account Type'], df['Number of Accounts'], color='teal')
plt.title('Number of Accounts by Account Type')
plt.xlabel('Account Type')
plt.ylabel('Number of Accounts')
plt.grid(True)
plt.show()


# Simulate some transaction amount data
transaction_amounts = np.random.power(1000, 200) # 1000 transactions with a mean of $1000
# Plotting
plt.hist(transaction_amounts, bins=20, color='purple',
edgecolor='black')
plt.title('Distribution of Daily Transaction Amounts')
plt.xlabel('Transaction Amount ($)')
plt.ylabel('Frequency')
plt.show()


# Sample data
data = {'Account Type': ['Savings', 'Savings', 'Checking', 'Checking',
'Credit', 'Credit', 'Loan', 'Loan'],
'Transaction Amount': [2000, 3000, 1500, 1600, 7000, 9200,
5000, 6050]}
df = pd.DataFrame(data)
# Plotting
sns.boxplot(x='Account Type', y='Transaction Amount', data=df)
plt.title('Transaction Amount by Account Type')
plt.show()

# Sample correlation data
data = {'ATM Transactions': [50, 30, 20], 'Online Payments': [30, 20,
15], 'In-branch Transactions': [20, 15, 10]}
df = pd.DataFrame(data, index=['Savings', 'Checking', 'Credit'])
# Plotting
sns.heatmap(df, annot=True, cmap='YlGnBu')
plt.title('Transaction Type Distribution by Account Type')
plt.xlabel('Transaction Type',loc="center")
plt.ylabel('Account Type')
plt.show()

# Sample data: Revenue contribution by region
data = {'Region': ['North', 'South', 'East', 'West'],
'Revenue': [50000, 70000, 60000, 80000]}
df = pd.DataFrame(data)
# Plotting
plt.pie(df['Revenue'], labels=df['Region'], autopct='%1.1f%%',
startangle=140)
plt.title('Revenue Contribution by Region')
plt.show()