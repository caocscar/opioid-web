# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:25 2019

@author: umhs-caoa
"""
import pandas as pd
import numpy as np
import os
from opioid_dict import aggregation_dict, name_correction_dict
from datetime import datetime

pd.options.display.max_rows = 30
pd.options.display.max_columns = 10

wdir = os.path.join('static','data')
savedir = os.path.join('static','data')

racelist = ['White','Black','Hispanic or Latino','Asian','American Indian or Alask Native',
         'Native Hawaiian or Other Pacific Islander','Other','Unknown',
         ]
genderlist = ['Female','Male','Unknown']

headers = ['index','value']

files = ['web_EMS.csv','web_EMS_Washtenaw.csv','web_ME.csv','web_ME_Wayne.csv']
list_df = []
for file in files:
    tmp = pd.read_csv(os.path.join(wdir,file))
    tmp['date'] = pd.to_datetime(tmp['date'])
    dataset = file.split('_')[1]
    tmp['src'] = dataset.strip('.csv')
    list_df.append(tmp)
df = pd.concat(list_df,ignore_index=True,sort=True)
df.replace({'city': name_correction_dict}, inplace=True)

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

def create_county_files(name, src, cityorcounty, T0, T1=None):
    column = 'city' if cityorcounty.lower() == "city" else 'county'
    cty = df[(df[column].str.contains(name)) & (df['src'] == src)]
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
    # rate and change table
    dayswin = (pd.to_datetime(T_end) - pd.to_datetime(T_start)).days + 1
    evtrte = len(cty_date)/dayswin
    create_rte_table_file(cty,T_start,dayswin,evtrte)
    # age, race, gender, gps file
    create_age_file(cty_date)
    create_race_file(cty_date)
    create_gender_file(cty_date)
    create_gps_file(cty_date, T0, T_end)
    create_evt_table_file(cty_date,name,src)
    create_ctyzip_freq_table(cty_date)

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

def create_evt_table_file(cty_date,name,src):
    cty_date = cty_date.sort_values(by=['date', 'zipcode'])
    if src == "EMS":
        tmpTab = cty_date[['date','city','zipcode']]
        tmpTab.columns = ['Date','City','Zip Code']
    elif src == "ME" and name in ["Wayne","Detroit"]:
        tmpTab = cty_date[['date','city','location','suspected_indicator']]
        tmpTab.columns = ['Date','City','Location','Suspected Overdose Indicator']
    elif src == "ME":
        tmpTab = cty_date[['date','city','location']]
        tmpTab.columns = ['Date','City','Location']
    tmpTab = tmpTab.replace({'City':r'.*\d.*'},{'City':np.NaN}, regex=True)
    tmpTab.to_csv(os.path.join(savedir,'county_src_evttab.csv'), index=False)


def create_rte_table_file(cty,T_start,days,evtrte):
    pp_end = pd.to_datetime(T_start) + pd.DateOffset(days=-1)
    pp_start = pp_end + pd.DateOffset(days=-days+1)
    cty_pp = cty[cty['date'].between(pp_start,pp_end)]
    pp_evtrte = len(cty_pp)/days
    if pp_start < pd.to_datetime("20190101") or pp_evtrte == 0:
        rtetab = pd.DataFrame({'Mean Incidents Per Day':[round(evtrte,1)],'Percent Change Since Last Period':[np.NaN]})
        rtetab.to_csv(os.path.join(savedir,'county_src_ratechange.csv'), index=False)
    else:
        rtetab = pd.DataFrame({'Mean Incidents Per Day':[round(evtrte,1)],'Percent Change Since Last Period':[round((evtrte-pp_evtrte)/pp_evtrte*100,1)]})
        rtetab.to_csv(os.path.join(savedir,'county_src_ratechange.csv'), index=False)
        
def create_ctyzip_freq_table(cty):
    cty['city'] = cty['city'].str.title()
    cty.replace({'city': aggregation_dict}, inplace=True)
    cty_counts = (cty.replace({'city':r'.*\d.*'},{'city':"Unknown"},regex=True))['city'].value_counts().to_frame(name="# Incidents")
    cty_counts["City"] = cty_counts.index
    cty_counts.loc[len(cty_counts)] = [len(cty),"Total"]
    cty_counts["Percent"] = round(cty_counts["# Incidents"]/len(cty)*100,1)
    cty_counts[["City","# Incidents","Percent"]].to_csv(os.path.join(savedir,'county_src_ctyfreqtab.csv'), index=False)
    zip_counts = cty['zipcode'].value_counts().to_frame(name="# Incidents")
    zip_counts["Zip Code"] = zip_counts.index
    zip_counts.loc[len(zip_counts)] = [len(cty),"Total"]
    zip_counts["Percent"] = round(zip_counts["# Incidents"]/len(cty)*100,1)
    zip_counts[["Zip Code","# Incidents","Percent"]].to_csv(os.path.join(savedir,'county_src_zipfreqtab.csv'), index=False)

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
    create_county_files('Wayne','EMS', 'county', 20190101)
