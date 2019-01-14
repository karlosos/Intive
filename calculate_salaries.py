import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

salary = pd.read_csv("salary.csv")
# empty fields in salary change to NA
salary['salaryBrutto'] = pd.to_numeric(salary['salaryBrutto'], errors='coerce')
salary_original = salary.copy()
# erase all rows with NA values
salary = salary.dropna()

workedYears = salary.drop('salaryBrutto', axis = 1)

# teaching
lm = LinearRegression()
lm.fit(workedYears, salary.salaryBrutto)

# here I could test only values from range salary_original[47:]
# like Krzysztof has proposed
# prediction
X = salary_original.drop('salaryBrutto', axis = 1)
Y = lm.predict(X)

salary_prediction = salary_original.copy()
salary_prediction.salaryBrutto = Y

salary_prediction.index.names = ['id']
salary_prediction.columns = ['worked_years', 'salary']

salary_prediction[47:].to_csv('salary_predicted.csv')
