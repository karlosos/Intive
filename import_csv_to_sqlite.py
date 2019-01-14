import csv, sqlite3
import pandas

conn = sqlite3.connect("db.sqlite3")

df = pandas.read_csv('salary_predicted.csv')
df.to_sql('cognitive_salary', conn, if_exists='append', index=False)
