import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

names = ["Doge Coin", "GameStock", "GameStop", "Twitter", "Elon Musk", "WallStreetBets"]
for name in names:
    data = TrendReq(hl="en-US", tz=360)
    data.build_payload(kw_list=[name])
    data = data.interest_over_time()
    data.to_csv(f"./save/{name}.csv", index=False)
    data.to_json(f"./save/{name}.json")

fig, ax = plt.subplots(figsize=(20, 15))
data["WallStreetBets"].plot()
plt.style.use("fivethirtyeight")
plt.title("Total Google Searches for Machine Learning", fontweight="bold")
plt.xlabel("Year", fontweight="bold")
plt.ylabel("Total Count", fontweight="bold")
plt.show()
