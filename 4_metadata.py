import pandas as pd
from tqdm import tqdm
import requests
from time import sleep

df = pd.read_csv("list_final.csv", sep=";")
print(df)
df.columns = ["Name", "Ticker"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.59"
}  # This is chrome, you can set whatever browser you like

for i, row in tqdm(df.iterrows()):
    try:
        if type(row["Name"]) == 'float':
            print(row["Ticker"], " already available in DB")
            continue
        else:
            symbol = row["Ticker"]
            response = requests.get(
                f"https://query2.finance.yahoo.com/v1/finance/search?q={symbol}",
                headers=headers,
            ).json()
            print(response)
            name = response["quotes"][0]["longname"]
            df.at[i, "Name"] = name
            sleep(1)
    except Exception as e:
        print(e)
        df.at[i, "Name"] = "Uncertain"


df.to_csv("list_final_with_name.csv", sep=",")
