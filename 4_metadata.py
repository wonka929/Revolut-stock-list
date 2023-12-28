import pandas as pd
from tqdm import tqdm
import requests
from time import sleep

df = pd.read_csv("list_final.csv", sep=",")
print(df)
df.columns = ["Name", "Ticker"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
}  # This is chrome, you can set whatever browser you like

for i, row in tqdm(df.iterrows()):
    try:
        symbol = row["Ticker"]
        response = requests.get(
            f"https://query2.finance.yahoo.com/v1/finance/search?q={symbol}",
            headers=headers,
        ).json()
        name = response["quotes"][0]["longname"]
        df.at[i, "Name"] = name
        sleep(1)
    except:
        df.at[i, "Name"] = "Nessuno"

df.to_csv("list_final_with_name.csv", sep=",")
