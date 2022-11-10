import pandas as pd

def september(month_col):
    if month_col == "SEP":
        return 1
    else: 
        return 0
    
def weather(temp_col):
    if temp_col <= 60:
        return 'Cold'
    elif temp_col > 60 and temp_col  < 90:
        return 'Moderate'
    elif temp_col >= 90:
        return 'Hot'
    
def score(dataframe, score_col):
    mean_df = construction_df[[score_col, 'attend']].groupby(score_col).mean()
    mean_df = mean_df.rename(columns={"attend": "score" })
    
    dataframe = pd.merge(dataframe, 
                         mean_df, 
                         on =score_col, 
                         how ='left')
    
    dataframe = dataframe.rename(columns={"score": score_col + "_score" })
    return dataframe

def weekend(day_col):
    if day_col == 'Friday' or day_col == 'Saturday' or day_col == 'Sunday':  
        return 1
    else:
        return 0