import pandas as pd
import numpy as np

np.random.seed(2026)

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 101, 107, 108, 109, 110, 111, 112, 113, 114],
    'Name': ['Anna', 'Ivan', 'Olga', 'Petr', 'Elena', 'Sergey', 'Anna', 'Dmitry', 'Maria', 'Alex', 'Kate', 'Max', 'Svetlana', 'Denis', 'Vera'],
    'Age': ['25', '30', 'invalid_age', '28', '35', '40', '25', '22', '29', '31', '38', '26', '42', '27', '33'],
    'Salary': ['1200', 'unknown', '1500', np.nan, '1800', '2000', '1200', '900', '1100', '1300', '1600', '950', '2200', '1400', '1700'],
    'Department': [' IT ', 'HR', 'Sales ', 'IT', 'Marketing', 'hr', ' IT ', 'Sales', 'IT', 'HR', 'Marketing', 'Sales', 'IT', 'HR', 'Marketing'],
    'HireDate': ['2020-05-12', '2019-03-15', 'bad_date', '2021-01-10', '2018-07-22', '2022-11-05', '2020-05-12', '2023-02-14', '2021-08-19', '2019-10-30', '2017-06-01', '2022-04-18', '2016-09-09', '2023-05-20', '2018-12-11'],
    'Gender': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'PerformanceScore': ['3.5', '4.0', '2.5', '3.0', '4.5', 'not_num', '3.5', '3.0', '4.0', '3.5', '4.8', '2.8', '4.2', '3.1', '3.9']
}

df = pd.DataFrame(data)

print("--- TASK 1 ---")
print("Количество строк и столбцов:", df.shape)
print("Типы данных:\n", df.dtypes)
print("Строки, где Salary присутствует:", df[df['Salary'].notna()])

print("\n--- TASK 2 ---")
print("Пропущенные значения:\n", df.isnull().sum())
df['Salary'] = df['Salary'].replace('unknown', np.nan)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
median_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(median_salary)

print("\n--- TASK 3 ---")
df['Department'] = df['Department'].str.strip().str.title()
df['Department'] = df['Department'].replace({'Hr': 'HR'})
print("Департаменты:", df['Department'].unique())

print("\n--- TASK 4 ---")
df = df.drop_duplicates(subset=['EmployeeID'], keep='first')
print("Строк после удаления дубликатов:", len(df))

print("\n--- TASK 5 ---")
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].median()).astype('Int64')
df['Department'] = df['Department'].astype('category')
df['Gender'] = df['Gender'].astype('category')
df['PerformanceScore'] = pd.to_numeric(df['PerformanceScore'], errors='coerce').fillna(3.0)

print("\n--- TASK 6 ---")
df['HireDate'] = pd.to_datetime(df['HireDate'], errors='coerce').fillna(pd.to_datetime('2020-01-01'))
df['Year'] = df['HireDate'].dt.year
df['Month'] = df['HireDate'].dt.month
df['Weekday'] = df['HireDate'].dt.day_name()
df['YearsWorked'] = 2026 - df['HireDate'].dt.year

print("\n--- TASK 7 ---")
df = df.rename(columns={'Salary': 'MonthlySalary', 'HireDate': 'EmploymentStartDate'})
dept_info = pd.DataFrame({'Department': ['IT', 'HR', 'Marketing'], 'Location': ['Bishkek', 'Osh', 'Karakol']})
merged_df = pd.merge(df, dept_info, on='Department', how='left')

print("\n--- TASK 8 ---")
print("Финальная форма:", merged_df.shape)
print("Все задачи по Pandas успешно выполнены!")
