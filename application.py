from flask import Flask, render_template, url_for
import os
from opioid_dict import *
from create_D3_files import create_daily

application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@application.route('/<string:county>/<string:src>/', defaults={'startdate':7}, methods=['GET'])
@application.route('/<string:county>/<string:src>/<int:startdate>', methods=['GET'])
def one_page_report(county, src, startdate):
    # TODO filter master file to date range
    create_daily(county, src, startdate)
    county = county.capitalize()
    src = src.upper()
    data = {
        'county': county,
        'src': src,
        'titlename': src_dict[src],
        'f_gps': f'data/{county}_{src}_address_geocode.js',
        'f_daily': 'data/county_src_daily.csv',
        'f_age': f'data/{county}_{src}_age.csv',
        'f_race': f'data/{county}_{src}_race.csv',
        'f_gender': f'data/{county}_{src}_gender.csv',
        'f_geojson': f'data/geojson/{county}.geojson',
        'center': center_dict[county],
    }
    return render_template("county_src_report.html", data=data)

#%% Run Flask app
# python application.py    
if __name__ == '__main__':
    application.run(debug=True)
