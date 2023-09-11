import csv
import pandas as pd


def convert_currency_to_float(curr):
    return float(curr[1:])
def csv_converter(df):
    df = df.loc[df["product"] == "pink morsel"]
    df['price'] = df['price'].apply(convert_currency_to_float)
    df['Sales'] = df.apply(lambda row:
      row['quantity'] * row['price'],
      axis=1
    )
    df.rename(columns={'date': 'Date'}, inplace=True)
    df.rename(columns={'region': 'Region'}, inplace=True)

    df.drop(columns=['product', 'price', 'quantity'], inplace=True)
    df = df.loc[:, ['Sales', 'Date', 'Region']]
    return df

def main():
    dataframe1 = pd.read_csv('daily_sales_data_0.csv')
    dataframe2 = pd.read_csv('daily_sales_data_1.csv')
    dataframe3 = pd.read_csv('daily_sales_data_2.csv')
    dataframes = [dataframe1, dataframe2, dataframe3]
    dataframes = csv_converter(pd.concat(dataframes))
    dataframes.to_csv('output.csv', index=False)
    print(dataframes)

if __name__ == "__main__":
    main()
