import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import datetime as dt

import env

import os


def get_logs():
    '''
    This function will return Codeup curriculum and cohort logs.
    '''
    # returns a local csv if it exists
    if os.path.isfile('curriculum.csv'):
        df = pd.read_csv('curriculum.csv')
    else:
        sql = ''' SELECT * FROM logs LEFT JOIN cohorts ON cohorts.id = logs.cohort_id; '''
        url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/curriculum_logs'
        df = pd.read_sql(sql, url)
        
        df.to_csv('curriculum.csv')
    
    return df



def prepare_df(df):
    '''
    This function adds course names matching the program_id, 
    drops unwanted columns, 
    combines date and time strings into one datetime object, 
    and sets index to datetime.
    '''
    # create a dataframe with course names, which will be joined to the main df
    courses = pd.DataFrame({'program_id':[1, 2, 3, 4], 
                                'course_name':['PHP Full Srack Web Dev', 'Java Full Stack Web Dev', 'Data Science', 'Front End Web Dev'], 
                                'course_subdomain':['php', 'java', 'ds', 'fe']})
    
    # add the course names to the log files
    df = df.merge(courses, how='left', left_on='program_id', right_on='program_id')
    
    # drop duplicate columns
    df = df.drop(columns=['Unnamed: 0', 'deleted_at'])

    # combine string date and time into one column
    df['datetime'] = df.date + ' ' + df.time
    # convert string type into datetime type
    df['datetime'] = pd.to_datetime(df.datetime)
    df['start_date'] = pd.to_datetime(df.start_date)
    df['end_date'] = pd.to_datetime(df.end_date)

    # set index to datetime
    df = df.set_index('datetime').sort_index()

    # since the datetime object came from a string, we don't know the timezone
    df = df.tz_localize('America/Chicago', ambiguous=True)
    df['hour'] = df.index.hour
    df['weekday'] = df.index.day_name() 
    
    return df



def value_counts_and_frequencies(s: pd.Series, dropna=True) -> pd.DataFrame:
    return pd.merge(
        s.value_counts(dropna=False).rename('count'),
        s.value_counts(dropna=False, normalize=True).rename('probability'),
        left_index=True,
        right_index=True)