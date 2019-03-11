# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:25 2019

@author: umhs-caoa
"""
import pandas as pd
import os
from opioid_dict import race_dict, gender_dict

pd.options.display.max_rows = 20

wdir = os.path.join('static','data')
savedir = os.path.join('static','data')

headers = ['index','value']

ED = pd.read_csv(os.path.join(wdir,'web_ED.csv'))
ED['admit_dt'] = pd.to_datetime(ED['admit_dt'])
lastday = ED['admit_dt'].max()
# age groups
bins = [0,25,35,45,55,999]
labels = ['<25','25-34','35-44','45-54','55+']
ED['age_grp'] = pd.cut(ED['age'], bins=bins, labels=labels)
# race labels
ED['race'].replace(race_dict, inplace=True)
# gender labels
ED['gender'].replace(gender_dict, inplace=True)

#%%
def get_firstday(start, daily):
    if start >= 20000000:
        start = str(start)
        return f'{start[:4]}-{start[4:6]}-{start[6:]}'
    else:
        return (lastday + pd.DateOffset(days=-start+1)).strftime('%Y-%m-%d')

def create_county_files(county, src, start):
    cty = ED[ED['county'] == county]
    # daily
    earliestday = cty['admit_dt'].min().strftime('%Y-%m-%d')
    daterange = pd.date_range(earliestday, lastday, freq='D')
    ts = cty.set_index('admit_dt')
    daily = ts['alexid'].resample('D').count()
    daily = daily.reindex(daterange, fill_value=0)
    daily = daily.to_frame().reset_index()
    daily.columns = ['date','value']
    daily['avg'] = daily['value'].rolling(7, min_periods=1).mean().round(2)
    firstday = get_firstday(start, daily)
    create_daily_file(firstday, daily)
    # date filtering
    cty_date = cty[cty['admit_dt'].between(firstday,lastday)]
    # age, race, gender, gps file
    create_age_file(cty_date)
    create_race_file(cty_date)
    create_gender_file(cty_date)
    create_gps_file(cty_date, start)

def create_daily_file(firstday, daily):
    daily_subset = daily[daily['date'] >= firstday]        
    daily_subset.to_csv(os.path.join(savedir,'county_src_daily.csv'), index=False)

def create_age_file(cty_date):
    age = cty_date['age_grp'].value_counts(sort=False)
    age.sort_index(inplace=True)
    age = age.reset_index()
    age.to_csv(os.path.join(savedir,'county_src_age.csv'), index=False, header=headers)

def create_race_file(cty_date):
    race = cty_date['race'].value_counts()
    race2 = race.reindex(['Caucasian','African American','Other','Not Recorded'], fill_value=0)
    race2 = race2.reset_index()
    race2.to_csv(os.path.join(savedir,'county_src_race.csv'), index=False, header=headers)
    
def create_gender_file(cty_date):
    gender = cty_date['gender'].value_counts()
    gender.sort_index(inplace=True)
    gender = gender.reset_index()
    gender.to_csv(os.path.join(savedir,f'county_src_gender.csv'), index=False, header=headers)        

def create_gps_file(cty_date, start):
    if start <= 7:
        cty_date['opacity'] = 1
    else:
        delta = lastday - cty_date['admit_dt']
        cty_date['opacity'] = 1 - 2 * delta.dt.days / 100
        cty_date.loc[cty_date['opacity'] < 0, 'opacity'] = 0
    with open(os.path.join(savedir,'county_src_gps.js'),'w') as fout:
        fout.write('var event_pts = ')
        cty_date[['lat','lng','opacity']].to_json(fout, orient='records')
        
#%%
if __name__ == '__main__':
    create_county_files('Muskegon','ED', 20190101)


