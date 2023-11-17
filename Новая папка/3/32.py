import pandas as pd
football = pd.read_csv("football.csv")
football.info()
print()
rich = football["Wage"].max()
low = football["Value"].min()
total = football["Wage"].sum()
print(f'{rich} {low} {total}')