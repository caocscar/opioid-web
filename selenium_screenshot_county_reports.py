# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:02:15 2017

@author: caoa
"""

from selenium import webdriver
import time
import os
import json
from itertools import product

#%%
appState = {
    "recentDestinations": [
        {"id": "Save as PDF",
         "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
}
profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
           'savefile.default_directory': os.path.join(os.getcwd(),'pdfs'),
          }
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--window-position=-1900,0")
options.add_experimental_option('prefs', profile) 
options.add_argument('--kiosk-printing')
driver = webdriver.Chrome(options = options)

#%% python -m http.server 5000
counties = ['Kent','Muskegon','Washtenaw','Wayne']
sources = ['EMS','ED','ME']
combos = product(counties, sources)
for county, src in combos:
    print(county,src)
    driver.get(f'localhost:5000/{county}/{src}')
    time.sleep(2)
    driver.execute_script('window.print();')
    time.sleep(1)
    filepath = os.path.join('pdfs',f'{county}_{src}.pdf')
    if os.path.isfile(filepath):
        os.remove(filepath)
    os.rename(os.path.join('pdfs',f'{src}.pdf'),filepath)
driver.quit()

#%% Trim all pdfs to one page