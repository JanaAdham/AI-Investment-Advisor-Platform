import pandas as pd
df=pd.read_csv(r"D:\project1\stock_price 2021 2026\raw\SWDY_El Sewedy Electric\SWDY.csv")

rename={
    "Date":"date",
    "Open":"open",
    "High":"high",
    "Low":"low",
    "Close":"close",
    "Volume":"volume",
    "Dividends":"dividends",
    "Stock Splits":"stock_splits",
    "Capital Gains":"capital_gains"
}
df.rename(columns=rename,inplace=True)
df.drop_duplicates()

df["date"]=df["date"].str.replace("00:00:00+02:00","",regex=False)
df["date"]=df["date"].str.replace("00:00:00+03:00","",regex=False)
df.rename(columns={"Hight":"hight"},inplace=True)
print(df)
df.to_csv("stock_swdy.csv",index=False)