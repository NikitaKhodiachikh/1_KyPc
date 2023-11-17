import pandas as pd
football = pd.read_csv("football.csv")
football.info()
print()

SprinitSpeedMax = football[football["Wage"] > football["Wage"].mean()]
print(round(SprinitSpeedMax))
SprinitSpeedMin = football[football["Wage"] < football["Wage"].mean()]
print(SprinitSpeedMin)


