import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/leonism/sample-superstore/master/data/superstore.csv')

def info():
	print("Information about The store:")
	print()
	print("STATS:")
	print(df.describe())
	print()
	print("ROWS:",df.shape[0])
	print("COLUMNS:", df.shape[1])
	print()
	print("Data Types")
	print(df.dtypes)
info()
