import pandas as pd
import matplotlib
from matplotlib import pyplot as plt


df = pd.read_csv('telecom_churn.csv')

# Номер 3
print("Номер 3")
print(df['Total day calls'].sum())

# Номер 4
print("\n\nНомер 4")
mean_calls = df[df['State']=="CT"]['Total day calls'].mean()
print(mean_calls)


# Номер 5
print("\n\nНомер 5")
new_df = df.groupby('State').agg({"Total day calls":"mean"})
print(new_df)

# Номер 6
print("\n\nНомер 6")
mean = df['Total day calls'].mean()
even_newer_df = new_df[new_df['Total day calls']>mean]
print(mean,even_newer_df, sep='\n')

# Номер 7
print("\n\nНомер 7")
calls = df.groupby('State')[['Total day calls','Total eve calls']].mean()
print(calls)

# Номер 8
print("\n\nНомер 8")
calls['D>E']=(calls['Total day calls']>calls['Total eve calls'])
print(calls)

# Номер 9
print("\n\nНомер 9")
df['good_guys']= (df['International plan']=='Yes') & (df['Voice mail plan']=='Yes')
print(df['good_guys'].mean())

# Номер 10
print("\n\nНомер 10")
print(df['Area code'].nunique())

# Номер 11
print("\n\nНомер 11")
custom = pd.DataFrame(df.groupby(['Customer service calls']).agg(Customers = ('Customer service calls','count')))
print(custom)

# Номер 12
print("\n\nНомер 12")
churn = pd.DataFrame(df.groupby(['Customer service calls']).agg(Churn = ('Churn','mean')))
print(churn)

plt.figure(figsize=(9, 9))
plt.tight_layout()
matplotlib.rcParams['font.size'] = 19

plt.grid(visible=True, which='major', axis='both', alpha=1)
plt.grid(visible=True, which='minor', axis='both', alpha=0.5)
plt.minorticks_on()

plt.title("График")
plt.xlabel('Звонки')
plt.ylabel('Доля отписок')

x_data = churn.index.values
y_data = churn["Churn"].values

plt.plot(x_data,y_data)

plt.savefig("Churn.jpg")

# Номер 13
print("\n\nНомер 13")
print(df['Total intl minutes'].mean())

# Номер 14
print("\n\nНомер 14")

# Номер 15
print("\n\nНомер 15")
print(df.groupby("Churn").agg({'Total day charge':'sum'}))

# Номер 16
print("\n\nНомер 16")
print(df.groupby(["State"]).agg({'Total day charge':'sum'}).sort_values(by="Total day charge"))

# Номер 17
print("\n\nНомер 17")
print(df.groupby(['Area code']).mean(numeric_only=True))

# Номер 17
print("\n\nНомер 17")
print(df.loc[[100,102,104],['State', 'Churn']])