import pandas as pd
import os

def load_concat(folder_path):
    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            ticker = os.path.splitext(file)[0] # file name without '.csv'
            df = pd.read_csv(os.path.join(folder_path,file))
            df['ticker'] = ticker
            all_data.append(df)

    return pd.concat(all_data, ignore_index=True)

PATH = './data'
ETFS_PATH = os.path.join(PATH, 'etfs') 
STOCKS_PATH = os.path.join(PATH, 'stocks')

etfs_df = load_concat(ETFS_PATH)
stocks_df = load_concat(STOCKS_PATH)

print("ETFs df shape:", etfs_df.shape)
print("Number of ETF's tickers:", len(etfs_df['ticker'].unique()))
print("Stocks df shape:", stocks_df.shape)
print("Number of stocks' tickers:", len(stocks_df['ticker'].unique()))

