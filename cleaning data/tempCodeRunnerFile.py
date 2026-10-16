import pandas as pd 
df=pd.read_csv(r"D:\project1\AI-Investment-Advisor-Platform\cleaning data\all_cleaned.csv")
print(df["date"].dtype)