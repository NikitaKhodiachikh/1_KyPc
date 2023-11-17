import pandas as pd
football = pd.read_csv("football.csv")
football.info()
print()
print(f'{round(football["Age"].mean())}{"-возрвст "} {football["Wage"].max()}{"-затрплата"}')
