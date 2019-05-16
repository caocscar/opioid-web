# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:25 2019

@author: umhs-caoa
"""
import pandas as pd
import os
from opioid_dict import race_dict, gender_dict, cities
from datetime import datetime

pd.options.display.max_rows = 30

wdir = os.path.join('static','data')
savedir = os.path.join('static','data')

racelist = ['White','Black','Hispanic or Latino','Asian','American Indian or Alask Native',
         'Native Hawaiian or Other Pacific Islander','Other','Unknown',
         ]
genderlist = ['Female','Male','Unknown']

headers = ['index','value']

files = ['web_ED.csv','web_EMS.csv','web_EMS_Washtenaw.csv','web_ME.csv','web_ME_Wayne.csv']
list_df = []
for file in files:
    tmp = pd.read_csv(os.path.join(wdir,file))
    tmp['date'] = pd.to_datetime(tmp['date'])
    dataset = file.split('_')[1]
    tmp['src'] = dataset.strip('.csv')
    list_df.append(tmp)
df = pd.concat(list_df,ignore_index=True)

#%%
def get_firstday(T0, latest_date):
    if T0 >= 20000000:
        T0 = str(T0)
        return f'{T0[:4]}-{T0[4:6]}-{T0[6:]}'
    else:
        return (latest_date + pd.DateOffset(days=-T0+1)).strftime('%Y-%m-%d')
    
def get_lastday(T1, latest_date):
    if T1:
        T1 = str(T1)
        return f'{T1[:4]}-{T1[4:6]}-{T1[6:]}'
    else:
        return latest_date.strftime('%Y-%m-%d')

def create_county_files(county, src, T0, T1=None):
    column = 'city' if county in cities else 'county'   
    cty = df[(df[column] == county) & (df['src'] == src)]      
    # daily file
    latest_date = df.loc[df['src'] == src,'date'].max()
    T_start = get_firstday(T0, latest_date)
    T_end = get_lastday(T1, latest_date)
    if cty.empty:
        earliest_date = pd.to_datetime(T_start)
        cty_date = cty
        daily = pd.Series()
    else:
        earliest_date = cty['date'].min().strftime('%Y-%m-%d')  
        ts = cty.set_index('date')
        daily = ts[column].resample('D').count()
    daterange = pd.date_range(earliest_date, latest_date, freq='D')
    daily = daily.reindex(daterange, fill_value=0)
    daily = daily.to_frame().reset_index()
    daily.columns = ['date','value']
    daily['avg'] = daily['value'].rolling(7, min_periods=1).mean().round(2)
    create_daily_file(T_start, T_end, daily)
    # date filtering
    cty_date = cty[cty['date'].between(T_start,T_end)]
    # age, race, gender, gps file
    create_age_file(cty_date)
    create_race_file(cty_date)
    create_gender_file(cty_date)
    create_gps_file(cty_date, T0, T_end)

def create_daily_file(T_start, T_end, daily):
    daily_subset = daily[daily['date'].between(T_start,T_end)]        
    daily_subset.to_csv(os.path.join(savedir,'county_src_daily.csv'), index=False)

def create_age_file(cty_date):
    age = cty_date['age_grp'].value_counts(sort=False)
    age.sort_index(inplace=True)
    age = age.reset_index()
    age.to_csv(os.path.join(savedir,'county_src_age.csv'), index=False, header=headers)

def create_race_file(cty_date):
    race = cty_date['race'].value_counts()
    race = race.reindex(racelist, fill_value=0)
    race = race.reset_index()
    race.to_csv(os.path.join(savedir,'county_src_race.csv'), index=False, header=headers)
    
def create_gender_file(cty_date):
    gender = cty_date['gender'].value_counts()
    gender = gender.reindex(genderlist, fill_value=0)
    gender = gender.reset_index()
    gender.to_csv(os.path.join(savedir,'county_src_gender.csv'), index=False, header=headers)        

def create_gps_file(cty_date, T0, T_end):
    if T0 <= 14:
        cty_date['opacity'] = 1   
    else:
        enddate = pd.to_datetime(T_end)
        if T0 >= 20000000:
            first_date = datetime.strptime(str(T0),'%Y%m%d')
            numdays = (enddate - first_date).days
        else:
            numdays = T0
        delta = enddate - cty_date['date']
        cty_date['opacity'] = 1 - delta.dt.days / (numdays + 1)
    with open(os.path.join(savedir,'county_src_gps.js'),'w') as fout:
        fout.write('var event_pts = ')
        cty_date[['lat','lng','opacity']].to_json(fout, orient='records')
        
#%%
if __name__ == '__main__':
    create_county_files('Wayne','EMS', 20190224, 20190308)


