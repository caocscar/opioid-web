from flask import Flask, render_template, url_for
import os
from opioid_dict import src_dict, center_dict
from create_D3_files import create_county_files

application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@application.route('/<string:county>/<string:src>/', defaults={'startdate':7}, methods=['GET'])
@application.route('/<string:county>/<string:src>/<int:startdate>', methods=['GET'])
def one_page_report(county, src, startdate):
    create_county_files(county, src, startdate)
    county = county.capitalize()
    src = src.upper()
    data = {
        'county': county,
        'src': src,
        'titlename': src_dict[src],
        'f_geojson': f'data/geojson/{county}.geojson',
        'center': center_dict[county],
    }
    return render_template("county_src_report.html", data=data)

#%% Run Flask app
# python application.py    
if __name__ == '__main__':
    application.run(debug=True)
