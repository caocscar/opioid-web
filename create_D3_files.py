# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:25 2019

@author: umhs-caoa
"""
import pandas as pd
import os
from opioid_dict import race_dict, gender_dict

pd.options.display.max_rows = 30

wdir = os.path.join('static','data')
savedir = os.path.join('static','data')

racelist = ['White','Black','Hispanic or Latino','Asian','American Indian or Alask Native',
         'Native Hawaiian or Other Pacific Islander','Other','Unknown',
         ]
genderlist = ['Female','Male','Unknown']

headers = ['index','value']
bins = [0,25,35,45,55,999]
labels = ['<25','25-34','35-44','45-54','55+']

ED = pd.read_csv(os.path.join(wdir,'web_ED.csv'))
ED['date'] = pd.to_datetime(ED['date'])
lastday_ED = ED['date'].max()
# age groups
ED['age_grp'] = pd.cut(ED['age'], bins=bins, labels=labels)
# race labels
ED['race'].replace(race_dict, inplace=True)
# gender labels
ED['gender'].replace(gender_dict, inplace=True)

EMS = pd.read_csv(os.path.join(wdir,'web_EMS.csv'))
EMS['date'] = pd.to_datetime(EMS['date'])
lastday_EMS = EMS['date'].max()
# age groups
EMS['age_grp'] = pd.cut(EMS['age'], bins=bins, labels=labels)
# race labels
EMS['race'].replace(race_dict, inplace=True)
# gender labels
EMS['gender'].replace(gender_dict, inplace=True)

Wash_EMS = pd.read_csv(os.path.join(wdir,'web_EMS_Washtenaw.csv'))
Wash_EMS['date'] = pd.to_datetime(Wash_EMS['date'])
lastday_WEMS = Wash_EMS['date'].max()
# age groups
Wash_EMS['age_grp'] = pd.cut(Wash_EMS['age'], bins=bins, labels=labels)
# race labels
Wash_EMS['race'].replace(race_dict, inplace=True)
# gender labels
Wash_EMS['gender'].replace(gender_dict, inplace=True)

#%%
def get_firstday(start, daily, lastday):
    if start >= 20000000:
        start = str(start)
        return f'{start[:4]}-{start[4:6]}-{start[6:]}'
    else:
        return (lastday + pd.DateOffset(days=-start+1)).strftime('%Y-%m-%d')

def create_county_files(county, src, start):
    if src == 'ED':
        cty = ED[ED['county'] == county]
        lastday = lastday_ED
    elif src == 'EMS' and county == 'Washtenaw':
        cty = Wash_EMS[Wash_EMS['county'] == county]
        lastday = lastday_WEMS
    elif src == 'EMS':
        cty = EMS[EMS['county'] == county]
        lastday = lastday_EMS
    # daily
    earliestday = cty['date'].min().strftime('%Y-%m-%d')
    daterange = pd.date_range(earliestday, lastday, freq='D')
    ts = cty.set_index('date')
    daily = ts['county'].resample('D').count()
    daily = daily.reindex(daterange, fill_value=0)
    daily = daily.to_frame().reset_index()
    daily.columns = ['date','value']
    daily['avg'] = daily['value'].rolling(7, min_periods=1).mean().round(2)
    firstday = get_firstday(start, daily, lastday)
    create_daily_file(firstday, daily)
    # date filtering
    cty_date = cty[cty['date'].between(firstday,lastday)]
    # age, race, gender, gps file
    create_age_file(cty_date)
    create_race_file(cty_date, src)
    create_gender_file(cty_date)
    create_gps_file(cty_date, start, lastday)

def create_daily_file(firstday, daily):
    daily_subset = daily[daily['date'] >= firstday]        
    daily_subset.to_csv(os.path.join(savedir,'county_src_daily.csv'), index=False)

def create_age_file(cty_date):
    age = cty_date['age_grp'].value_counts(sort=False)
    age.sort_index(inplace=True)
    age = age.reset_index()
    age.to_csv(os.path.join(savedir,'county_src_age.csv'), index=False, header=headers)

def create_race_file(cty_date, src):
    race = cty_date['race'].value_counts()
    race = race.reindex(racelist, fill_value=0)
    race = race.reset_index()
    race.to_csv(os.path.join(savedir,'county_src_race.csv'), index=False, header=headers)
    
def create_gender_file(cty_date):
    gender = cty_date['gender'].value_counts()
    gender = gender.reindex(genderlist, fill_value=0)
    gender = gender.reset_index()
    gender.to_csv(os.path.join(savedir,f'county_src_gender.csv'), index=False, header=headers)        

def create_gps_file(cty_date, start, lastday):
    if start <= 7:
        cty_date['opacity'] = 1
    else:
        delta = lastday - cty_date['date']
        cty_date['opacity'] = 1 - 2 * delta.dt.days / 100
        cty_date.loc[cty_date['opacity'] < 0, 'opacity'] = 0
    with open(os.path.join(savedir,'county_src_gps.js'),'w') as fout:
        fout.write('var event_pts = ')
        cty_date[['lat','lng','opacity']].to_json(fout, orient='records')
        
#%%
if __name__ == '__main__':
    create_county_files('Muskegon','ED', 20190101)


