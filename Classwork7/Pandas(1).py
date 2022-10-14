import pandas as pd
import numpy as np
import statistics as st

df = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, np.nan, 65.26, 110.5, 948.5, np.nan, 5760, 1983.43, np.nan, 250.45, 75.29, 3045.6],
    'sale_amt': [10.5, 20.65, np.nan, 11.5, 98.5, np.nan, 57, 19.43, np.nan, 25.45, 75.29, 35.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]})
df['ord_date'] = pd.to_datetime(df['ord_date'])

print(df, '\n')

# Пункт 0
for column in df.columns:
    mask = df.isna()[column]
    print(column, ':', df[mask].index.values)
print()

# Пункт 1
values = {'ord_no': df['ord_no'].mean(), 'purch_amt': df['purch_amt'].mean(), 'sale_amt': df['sale_amt'].mean(),
          'ord_date': pd.to_datetime(df['ord_date']).mean().strftime("%Y-%m-%d"),
          'customer_id': df['customer_id'].mean(), 'salesman_id': df['salesman_id'].mean(), }
df1 = df.fillna(value=values)
print(df1, "\n")

# Пункт 2
values = {'ord_no': df['ord_no'].median(), 'purch_amt': df['purch_amt'].median(), 'sale_amt': df['sale_amt'].median(),
          'ord_date': pd.to_datetime(df['ord_date']).median().strftime("%Y-%m-%d"),
          'customer_id': df['customer_id'].median(), 'salesman_id': df['salesman_id'].median()}
df2 = df.fillna(value=values)
print(df2, "\n")

# Пункт 3
values = {'ord_no': st.mode(df['ord_no']), 'purch_amt': st.mode(df['purch_amt']), 'sale_amt': st.mode(df['sale_amt']),
          'ord_date': st.mode(pd.to_datetime(df['ord_date'])).strftime("%Y-%m-%d"),
          'customer_id': st.mode(df['customer_id']), 'salesman_id': st.mode(df['salesman_id'])}
df3 = df.fillna(value=values)
print(df3, "\n")

# Пункт 4
for column in df.columns:
    if column != 'ord_date':
        df[column] = df[column].interpolate()
print(df)
