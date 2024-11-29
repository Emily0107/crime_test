import pandas as pd

def findMean() :
    file = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(file)
    
    return df['Vict Age'].mean()

def findMedian():
    file = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(file)

    return df['Vict Age'].median()

print(findMean())
print(findMedian())

