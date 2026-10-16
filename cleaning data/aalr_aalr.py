import pandas as pd
df=pd.read_csv(r"D:\project1\stock_price 2021 2026\raw\AALR_AALR\AALR.csv")
rename={"Date":"date",
        "Open":"open",
        "High":"high",
        "Low":"low",
        "Close":"close",
        "Volume":"volume",
        "Dividends":"dividends",
        "Stock Splits":"stock_splits",
        "Capital Gains":"capital_gains"}
df.rename(columns=rename,inplace=True)
df.drop_duplicates()
df["date"]=df["date"].str.replace("00:00:00+02:00","",regex=False)
df["date"]=df["date"].str.replace("00:00:00+03:00","",regex=False)
# print(df)
# df["date"]=pd.DataFrame(df["date"])
#3shan a5le date typy is date 
df["date"] = pd.to_datetime(df["date"], errors="coerce")
print(df["date"].dtype)
df.to_csv("stock_aalr.csv",index=False)