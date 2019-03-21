from flask import Flask, render_template, url_for
import os
from opioid_dict import src_dict, center_dict
from create_D3_files import create_county_files
from datetime import date

application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cities = ['Bay City','Detroit','Flint','Grand Rapids','Kalamazoo','Pontiac','Saginaw']

@application.route('/<string:county>/<string:src>/', defaults={'T0':7, 'T1':None}, methods=['GET'])
@application.route('/<string:county>/<string:src>/<int:T0>', defaults={'T1':None}, methods=['GET'])
@application.route('/<string:county>/<string:src>/<int:T0>/<int:T1>', methods=['GET'])
def one_page_report(county, src, T0, T1):
    county = county.title()
    src = src.upper()
    create_county_files(county, src, T0, T1)
    if county in cities and county != 'Kalamazoo':
        folder = 'cities'
        county_flag = ''
    else:
        folder = 'counties'
        county_flag = 'County'
    data = {
        'county': county,
        'src': src,
        'county_flag': county_flag,
        'titlename': src_dict[src],
        'f_geojson': f'geojson/{folder}/{county}.geojson',
        'center': center_dict[county],
    }
    return render_template("county_src_report.html", data=data)

#%% Run Flask app
# python application.py    
if __name__ == '__main__':
    application.run(debug=True)
