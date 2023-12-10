import pandas as pd
import numpy

def getTransactions(date1, date2):
    # date1 = '2024-01-01'
    # date2 = '2024-06-30'

    df = pd.read_csv("example.csv")

    #filter by date
    dateFilter = df[
        (df['date_of_transaction'] >= date1) & (df['date_of_transaction'] <= date2)]

    finalArray = dateFilter.to_numpy()

    return finalArray
