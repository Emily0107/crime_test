import pandas as pd

def checkVictSex():
    file = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(file)
    column = 'Vict Sex'

    if len(df[column].isnull()) > 0:
        return False
    elif len(df[column].unique()) > 2: # which is, unique value not just M or F
        return False
    else:
        return True

def checkVictAge():
    file = 'Crime_Data_from_2020_to_Present.csv'
    df = pd.read_csv(file)
    column = 'Vict Age'

    if len(df[column].isnull()) > 0:
      return False
    elif len(df[column].unique()) > 100: 
      return False
    else:
      return True



