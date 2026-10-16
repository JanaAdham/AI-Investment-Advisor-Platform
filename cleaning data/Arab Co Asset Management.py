import pandas as pd
df=pd.read_csv(r"D:\project1\stock_price 2021 2026\raw\ACAMD_Arab Co Asset Management\ACAMD.csv")
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
df["date"] = pd.to_datetime(df["date"], errors="coerce")
print(df["date"].dtype)
print(df)
df.to_csv("stock_ACAMD.csv",index=False)