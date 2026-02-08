import pandas as pd
import matplotlib.pyplot as plt

# dataset load
data = pd.read_csv("matches.csv")

print("First 5 rows:")
print(data.head())

# total matches
print("Total matches:", len(data))

# most winning team
print("\nMost wins:")
print(data["winner"].value_counts().head())

# toss winner stats
print("\nToss winners:")
print(data["toss_winner"].value_counts().head())

# matches per season
season = data["season"].value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.plot(season.index, season.values)
plt.title("Matches per season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.show()