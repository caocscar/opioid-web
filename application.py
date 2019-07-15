from flask import Flask, render_template, request
from opioid_dict import src_dict, center_dict, cities, counties, names, name_cases, name_case_ls
from create_D3_files import create_county_files

application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@application.route('/')
def homepage():
    data = {
      'counties': counties,
    }
    placenames=[]
    for each in cities:
        placenames.append(each)
    for each in counties:
        placenames.append(each)
    placenames.sort()

    return render_template("index.html", data=data, cities=cities, counties=counties, placenames = placenames)


@application.route('/dashboard', methods=['GET'])
def generate_report_given_name():
    arguments=['city', 'county', 'src', 'T0' , 'T1' ]
    source = request.args.get('src', default = "EMS", type = str)
    city = request.args.get('city')
    county = request.args.get('county')
    T0 = request.args.get('T0', default = 14, type = int)
    T1 = request.args.get('T1', default = None, type = int)

    if county:
        cityorcounty = "County"
        name = county
        src = source
    if city:
        cityorcounty = "City"
        name = city
        src = source


    create_county_files(name, source, T0, T1, cityorcounty)


    source = source.upper()


    if city:
        city = city.title()
        for each in name_cases:
            if city in each.keys():
                city = each[city]
    if county:
        county = county.title()

    if city in cities:
        if '(City)' in city:
            propername = city[:-7]
        else:
            propername = city
        folder = 'cities'
        county_flag = ''
        data = {
            'placename': city,
            'propername': propername,
            'cityorcounty': "city",
            'county':center_dict["City"][propername]["county"],
            'src': source,
            'county_flag': county_flag,
            'titlename': src_dict[source],
            'f_geojson': f'geojson/{folder}/{propername}.geojson',
            'center': center_dict["City"][propername]['center'],
            'zoom' : center_dict["City"][propername].get('zoom', 10)}

    if county in counties:
        folder = 'counties'
        county_flag = 'County'
        data = {
            'placename': county,
            'cityorcounty': "county",
            'src': source,
            'county_flag': county_flag,
            'titlename': src_dict[source],
            'f_geojson': f'geojson/{folder}/{county}.geojson',
            'center': center_dict["County"][county]['center'],
            'zoom' : center_dict["County"][county].get('zoom', 10)}



    return render_template("county_src_report.html", data=data, T0=T0, T1=T1)


# @application.route('/<string:county>/<string:src>/', defaults={'T0':14, 'T1':None}, methods=['GET'])
# @application.route('/<string:county>/<string:src>/<int:T0>', defaults={'T1':None}, methods=['GET'])
# @application.route('/<string:county>/<string:src>/<int:T0>/<int:T1>', methods=['GET'])
# def one_page_report(county, src, T0, T1):
#     county = county.title()
#     src = src.upper()
#     create_county_files(county, src, T0, T1)
#     if county in cities:
#         folder = 'cities'
#         county_flag = ''
#     else:
#         folder = 'counties'
#         county_flag = 'County'
#     data = {
#         'county': county,
#         'src': src,
#         'county_flag': county_flag,
#         'titlename': src_dict[src],
#         'f_geojson': f'geojson/{folder}/{county}.geojson',
#         'center': center_dict[county]['center'],
#         'zoom': center_dict[county].get('zoom',10),
#     }
#     return render_template("county_src_report.html", data=data)

#%% Run Flask app
# python application.py
if __name__ == '__main__':
    application.run(debug=True)
