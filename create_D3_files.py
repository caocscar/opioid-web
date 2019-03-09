# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:25 2019

@author: umhs-caoa
"""
import pandas as pd
import os
from datetime import date

pd.options.display.max_rows = 20

wdir = os.path.join('static','data')
savedir = os.path.join('static','data')

def create_daily(county, src, start):
    src = 'ED'
    county = 'Muskegon'
    file = f'{county}_{src}_daily.csv'
    daily = pd.read_csv(os.path.join(wdir,file))
    if start >= 20000000:
        start = str(start)
        yr = start[:4]
        mth = start[4:6]
        day = start[6:]
        startdate = f'{yr}-{mth}-{day}'
    else:
        maxdate = daily['date'].max()
        enddate = date(int(maxdate[:4]), int(maxdate[5:7]), int(maxdate[8:]))
        startdate = (enddate + pd.DateOffset(days=-start+1)).strftime('%Y-%m-%d')
    daily_subset = daily[daily['date'] >= startdate]        
    daily_subset.to_csv(os.path.join(savedir,'county_src_daily.csv'))

#%%
if __name__ == '__main__':
    create_daily('Muskegon','ED',20190101)

#%%
#for county in counties:    
#    cty = df[df['county'] == county]
#    firstday = cty['admit_dt'].min().strftime('%Y-%m-%d')
#    daterange = pd.date_range(start=firstday, end=lastday, freq='D')
#    # daily
#    ts = cty.set_index('admit_dt')
#    daily = ts['alexid'].resample('D').count()
#    daily = daily.reindex(daterange, fill_value=0)
#    daily = daily.to_frame().reset_index()
#    daily.columns = ['date','value']
#    daily['avg'] = daily['value'].rolling(7, min_periods=1).mean().round(2)
#    daily.to_csv(os.path.join(savedir,f'{county}_{src}_daily.csv'), index=False)
#    # age
#    age = cty['age_grp'].value_counts(sort=False)
#    age.sort_index(inplace=True)
#    age = age.reset_index()
#    age.to_csv(os.path.join(savedir,f'{county}_{src}_age.csv'), index=False, header=headers)
#    # race
#    cty['race'].replace(race_dict, inplace=True)
#    race = cty['race'].value_counts()
#    race2 = race.reindex(['Caucasian','African American','Other','Not Recorded'], fill_value=0)
#    race2 = race2.reset_index()
#    race2.to_csv(os.path.join(savedir,f'{county}_{src}_race.csv'), index=False, header=headers)
#    # gender
#    cty['gender'].replace(gender_dict, inplace=True)
#    gender = cty['gender'].value_counts()
#    gender.index.name = 'index'
#    gender.name = 'value'
#    gender.sort_index(inplace=True)
#    gender = gender.reset_index()
#    gender.to_csv(os.path.join(savedir,f'{county}_{src}_gender.csv'), index=False, header=headers)
