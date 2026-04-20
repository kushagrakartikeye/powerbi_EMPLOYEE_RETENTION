import pandas as pd

df = pd.read_csv('data.csv')

df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)

df['Attrition_Flag'] = df['Attrition'].map({'Yes': 1, 'No': 0})

def salary_slab(x):
    if x < 3000:
        return 'Low'
    elif x < 7000:
        return 'Medium'
    else:
        return 'High'

df['SalarySlab'] = df['MonthlyIncome'].apply(salary_slab)

df.to_csv('cleaned_employee_data.csv', index=False)

print("Done ✅")