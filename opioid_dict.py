src_dict = {'EMS':'EMS', 'ED':'Emergency Departments', 'ME':'Medical Examiner'}
race_dict = {'B':'Black',
             'African American':'Black',
             'Black or African American':'Black',
             'African American / Black':'Black',
             'W':'White',
             'White, Not Recorded':'White',
             'Patient Refused':'Unknown',
             '1':'Unknown',
             '2':'Unknown',
             '6':'Unknown',
             '7':'Unknown',
             '8':'Unknown',
             'A':'Unknown',
             'D':'Unknown',
             'U':'Unknown',
             'Not Recorded':'Unknown',
             'Not Applicable':'Unknown',
             'H':'Hispanic or Latino',
             'White, Hispanic or Latino':'Hispanic or Latino',
             'White,Hispanic or Latino':'Hispanic or Latino',
             'Hispanic or Latino, White':'Hispanic or Latino',
             'Hispanic, White':'Hispanic or Latino',
             'Asian, White':'Other',
             'White, Asian':'Other',
             'Asian, Black or African American':'Other',
             'Black or African American, White':'Other',
             'White, Black or African American':'Other',
             'White,Black or African American':'Other',
             'Black or African American, Hispanic or Latino':'Other',
             'Hispanic or Latino, Black or African American':'Other',
             'White, Native Hawaiian or Other Pacific Islander, Asian':'Other',
             'Native Hawaiian or Other Pacific Islander, White':'Other',
             'White, Native Hawaiian or Other Pacific Islander':'Other',
             'White,Native Hawaiian or Other Pacific Islander,Hispanic or Latino,Black or African American,Asian,American Indian or Alaska Native':'Other',
             'White, Native Hawaiian or Other Pacific Islander, Hispanic or Latino, Black or African American, Asian, American Indian or Alaska Native':'Other',
             'Black or African American, American Indian or Alaska Native':'Other',
             'White, Hispanic or Latino, Asian, American Indian or Alaska Native':'Other',
             'Unspecified':'Other',
             'American Indian / Alaskan Native':'American Indian or Alaska Native',
             }
gender_dict = {'F':'Female',
               'M':'Male',
               'U':'Unknown',
               'Unknown (Unable to Determine)':'Unknown',
               'Not Applicable':'Unknown',
               }
center_dict = { "City" :
    {'Ann Arbor': {
        'center': '{lat: 42.28, lng: -83.73}',
        'zoom' : 12,
        'minwidth': 550,
        'minheight':400
    },
    'Ypsilanti':{
        'center': '{lat: 42.24, lng: -83.61}',
        'zoom' : 13,
        'minwidth' : 500,
        'minheight' : 400
    },
    'Detroit': {
        'center': '{lat: 42.35, lng: -83.10}',
        'zoom': 11,
        'minwidth': 550,
        'minheight': 400
    },
    'Bay City': {
        'center': '{lat: 43.58, lng: -83.88}',
        'zoom': 12, #optimal: 13
        'minwidth': 150, #optimal: 450
        'minheight': 200 #optimal: 700
    },
    'Flint': {
        'center': '{lat:43.01, lng:-83.70}',
        'zoom': 12, #optimal: 12
        'minwidth': 250, #optimal: 450
        'minheight': 300 #optimal: 550
    },
    'Grand Rapids': {
        'center': '{lat:42.96, lng:-85.66}',
        'zoom': 12, #optimal: 12
        'minwidth': 300, #optimal: 550
        'minheight': 300, #optimal: 600
    },
    'Pontiac': {
        'center': '{lat:42.65, lng:-83.29}',
        'zoom': 12, #optimal: 12
        'minwidth': 150, #optimal: 300
        'minheight': 200, #optimal: 400
    },
    'Kalamazoo':{
        'center': '{lat:42.29, lng: -85.58}',
        'zoom': 12,
        'minwidth':150,
        'minheight': 200
    },
    'Muskegon':{
        'center':  '{lat:43.23, lng: -86.25}',
        'zoom': 12,
        'minwidth':150,
        'minheight': 200
    },

    'Saginaw':{
        'center': '{lat: 43.42, lng: -83.95}',
        'zoom': 12,
        'minwidth': 150,
        'minheight': 200
    }},

    'County':
    {'Alcona': {
        'center': '{lat:44.68, lng:-83.58}',
        'minwidth': 450,
        'minheight': 400
    },
    'Alger': {
        'center': '{lat:46.42, lng:-86.49}',
        'zoom': 9,
        'minwidth': 950,
        'minheight': 600
    },
    'Allegan': {
        'center': '{lat:42.59, lng:-85.91}',
        'minwidth': 550,
        'minheight': 350
    },
    'Alpena': {
        'center': '{lat:45.03, lng:-83.58}',
        'minwidth': 500,
        'minheight': 400
    },
    'Antrim': {
        'center': '{lat:45.01, lng:-85.14}',
        'minwidth': 450,
        'minheight': 450
    },
    'Arenac': {
        'center': '{lat:44.04, lng:-83.87}',
        'minwidth': 450,
        'minheight': 300
    },
    'Baraga': {
        'center': '{lat:46.69, lng:-88.34}',
        'minwidth': 550,
        'minheight': 600
    },
    'Barry': {
        'center': '{lat:42.60, lng:-85.31}',
        'minwidth': 350,
        'minheight': 350
    },
    'Bay': {
        'center': '{lat:43.7, lng:-83.93}',
        'minwidth': 350,
        'minheight': 550
    },
    'Benzie': {
        'center': '{lat:44.65, lng:-86.04}',
        'minwidth': 350,
        'minheight': 300
    },
    'Berrien': {
        'center': '{lat:42.00, lng:-86.52}',
        'minwidth': 450,
        'minheight': 500
    },
    'Branch': {
        'center': '{lat:41.92, lng:-85.06}',
        'minwidth': 350,
        'minheight': 350
    },
    'Calhoun': {
        'center': '{lat:42.25, lng:-85.00}',
        'minwidth': 450,
        'minheight': 350
    },
    'Cass': {
        'center': '{lat:41.92, lng:-85.99}',
        'minwidth': 350,
        'minheight': 350
    },
    'Charlevoix': {
        'center': '{lat:45.48, lng:-85.22}',
        'zoom': 9,
        'minwidth': 400,
        'minheight': 400
    },
    'Cheboygan': {
        'center': '{lat:45.49, lng:-84.47}',
        'minwidth': 400,
        'minheight': 650
    },
    'Chippewa': {
        'center': '{lat:46.34, lng:-84.36}',
        'zoom': 9,
        'minwidth': 650,
        'minheight': 500
    },
    'Clare': {
        'center': '{lat:44.00, lng:-84.85}',
        'minwidth': 400,
        'minheight': 400
    },
    'Clinton': {
        'center': '{lat:42.94, lng:-84.60}',
        'minwidth': 350,
        'minheight': 350
    },
    'Crawford': {
        'center': '{lat:44.68, lng:-84.61}',
        'minwidth': 350,
        'minheight': 400
    },
    'Delta': {
        'center': '{lat:45.85, lng:-86.91}',
        'minwidth': 700,
        'minheight': 650
    },
    'Dickinson': {
        'center': '{lat:45.98, lng:-87.88}',
        'minwidth': 400,
        'minheight': 550
    },
    'Eaton': {
        'center': '{lat:42.60, lng:-84.84}',
        'minwidth': 350,
        'minheight': 350
    },
    'Emmet': {
        'center': '{lat:45.53, lng:-84.93}',
        'minwidth': 300,
        'minheight': 600
    },
    'Genesee': {
        'center': '{lat:43.00, lng:-83.69}',
        'minwidth': 350,
        'minheight': 450
    },
    'Gladwin': {
        'center': '{lat:43.99, lng:-84.39}',
        'minwidth': 350,
        'minheight': 400
    },
    'Gogebic': {
        'center': '{lat:46.43, lng:-89.70}',
        'zoom': 9,
        'minwidth': 550,
        'minheight': 400
    },
    'Grand Traverse': {
        'center': '{lat:44.75, lng:-85.57}',
        'minwidth': 400,
        'minheight': 500
    },
    'Gratiot': {
        'center': '{lat:43.29, lng:-84.61}',
        'minwidth': 350,
        'minheight': 350
    },
    'Hillsdale': {
        'center': '{lat:41.88, lng:-84.59}',
        'minwidth': 350,
        'minheight': 400
    },
    'Houghton': {
        'center': '{lat:46.85, lng:-88.61}',
        'zoom': 9,
        'minwidth': 300,
        'minheight': 500
    },
    'Huron': {
        'center': '{lat:43.87, lng:-83.04}',
        'minwidth': 650,
        'minheight': 450
    },
    'Ingham': {
        'center': '{lat:42.60, lng:-84.37}',
        'minwidth': 350,
        'minheight': 400
    },
    'Ionia': {
        'center': '{lat:42.94, lng:-85.07}',
        'minwidth': 350,
        'minheight': 350
    },
    'Iosco': {
        'center': '{lat:44.34, lng:-83.60}',
        'minwidth': 450,
        'minheight': 400
    },
    'Iron': {
        'center': '{lat:46.17, lng:-88.55}',
        'minwidth': 650,
        'minheight': 550
    },
    'Isabella': {
        'center': '{lat:43.64, lng:-84.85}',
        'minwidth': 400,
        'minheight': 400
    },
    'Jackson': {
        'center': '{lat:42.25, lng:-84.42}',
        'minwidth': 450,
        'minheight': 350
    },
    'Kalamazoo': {
        'center': '{lat:42.25, lng:-85.53}',
        'minwidth': 350,
        'minheight': 350
    },
    'Kalkaska': {
        'center': '{lat:44.69, lng:-85.09}',
        'minwidth': 400,
        'minheight': 400
    },
    'Kent': {
        'center': '{lat:43.03, lng:-85.55}',
        'minwidth': 400,
        'minheight': 550
    },
    'Keweenaw': {
        'center': '{lat:47.70, lng:-88.49}',
        'zoom': 9,
        'minwidth': 600,
        'minheight': 550
    },
    'Lake': {
        'center': '{lat:43.99, lng:-85.80}',
        'minwidth': 350,
        'minheight': 400
    },
    'Lapeer': {
        'center': '{lat:43.10, lng:-83.22}',
        'minwidth': 350,
        'minheight': 450
    },
    'Leelanau': {
        'center': '{lat:45.11, lng:-85.84}',
        'minwidth': 450,
        'minheight': 700
    },
    'Lenawee': {
        'center': '{lat:41.93, lng:-84.06}',
        'minwidth': 450,
        'minheight': 400
    },
    'Livingston': {
        'center': '{lat:42.60, lng:-83.91}',
        'minwidth': 400,
        'minheight': 400
    },
    'Luce': {
        'center': '{lat:46.50, lng:-85.55}',
        'minwidth': 500,
        'minheight': 550
    },
    'Mackinac': {
        'center': '{lat:45.98, lng:-84.99}',
        'zoom': 9,
        'minwidth': 650,
        'minheight': 300
    },
    'Macomb': {
        'center': '{lat:42.67, lng:-82.91}',
        'minwidth': 300,
        'minheight': 450
    },
    'Manistee': {
        'center': '{lat:44.34, lng:-86.10}',
        'minwidth': 450,
        'minheight': 400
    },
    'Marquette': {
        'center': '{lat:46.45, lng:-87.62}',
        'zoom': 9,
        'minwidth': 400,
        'minheight': 500
    },
    'Mason': {
        'center': '{lat:44.00, lng:-86.28}',
        'minwidth': 350,
        'minheight': 400
    },
    'Mecosta': {
        'center': '{lat:43.64, lng:-85.32}',
        'minwidth': 350,
        'minheight': 400
    },
    'Menominee': {
        'center': '{lat:45.54, lng:-87.58}',
        'zoom': 9,
        'minwidth': 250,
        'minheight': 500
    },
    'Midland': {
        'center': '{lat:43.65, lng:-84.39}',
        'minwidth': 350,
        'minheight': 400
    },
    'Missaukee': {
        'center': '{lat:44.34, lng:-85.09}',
        'minwidth': 400,
        'minheight': 400
    },
    'Monroe': {
        'center': '{lat:41.91, lng:-83.48}',
        'minwidth': 450,
        'minheight': 400
    },
    'Montcalm': {
        'center': '{lat:43.29, lng:-85.20}',
        'minwidth': 550,
        'minheight': 350
    },
    'Montmorency': {
        'center': '{lat:45.03, lng:-84.13}',
        'minwidth': 400,
        'minheight': 400
    },
    'Muskegon': {
        'center': '{lat:43.30, lng:-86.13}',
        'minwidth': 500,
        'minheight': 400
    },
    'Newaygo': {
        'center': '{lat:43.55, lng:-85.80}',
        'minwidth': 350,
        'minheight': 550
    },
    'Oakland': {
        'center': '{lat:42.66, lng:-83.39}',
        'minwidth': 450,
        'minheight': 500
    },
    'Oceana': {
        'center': '{lat:43.64, lng:-86.29}',
        'minwidth': 400,
        'minheight': 400
    },
    'Ogemaw': {
        'center': '{lat:44.33, lng:-84.13}',
        'minwidth': 400,
        'minheight': 400
    },
    'Ontonagon': {
        'center': '{lat:46.68, lng:-89.38}',
        'zoom': 9,
        'minwidth': 400,
        'minheight': 400
    },
    'Osceola': {
        'center': '{lat:43.99, lng:-85.33}',
        'minwidth': 350,
        'minheight': 400
    },
    'Oscoda': {
        'center': '{lat:44.68, lng:-84.13}',
        'minwidth': 400,
        'minheight': 400
    },
    'Otsego': {
        'center': '{lat:45.03, lng:-84.61}',
        'minwidth': 400,
        'minheight': 400
    },
    'Ottawa': {
        'center': '{lat:42.99, lng:-86.03}',
        'minwidth': 400,
        'minheight': 450
    },
    'Presque Isle': {
        'center': '{lat:45.41, lng:-83.82}',
        'minwidth': 650,
        'minheight': 450
    },
    'Roscommon': {
        'center': '{lat:44.34, lng:-84.61}',
        'minwidth': 400,
        'minheight': 400
    },
    'Saginaw': {
        'center': '{lat:43.35, lng:-84.03}',
        'minwidth': 500,
        'minheight': 450
    },
    'St. Clair': {
        'center': '{lat:42.84, lng:-82.70}',
        'minwidth': 450,
        'minheight': 650
    },
    'St. Joseph': {
        'center': '{lat:41.92, lng:-85.54}',
        'minwidth': 400,
        'minheight': 350
    },
    'Sanilac': {
        'center': '{lat:43.42, lng:-82.81}',
        'minwidth': 450,
        'minheight': 550
    },
    'Schoolcraft': {
        'center': '{lat:46.13, lng:-86.24}',
        'zoom' : 9,
        'minwidth': 550,
        'minheight': 800
    },
    'Shiawassee': {
        'center': '{lat:42.95, lng:-84.15}',
        'minwidth': 350,
        'minheight': 400
    },
    'Tuscola': {
        'center': '{lat:43.48, lng:-83.40}',
        'minwidth': 450,
        'minheight': 550
    },
    'Van Buren': {
        'center': '{lat:42.24, lng:-86.06}',
        'minwidth': 450,
        'minheight': 350
    },
    'Washtenaw': {
        'center': '{lat:42.25, lng:-83.84}',
        'minwidth': 450,
        'minheight': 400
    },
    'Wayne': {
        'center': '{lat:42.24, lng:-83.21}',
        'minwidth': 500,
        'minheight': 450
    },
    'Wexford': {
        'center': '{lat:44.28, lng:-85.58}',
        'minwidth': 400,
        'minheight': 400
    }}
}


name_case_ls = ['Saginaw', 'Kalamazoo', 'Muskegon']
name_cases = [{'Saginaw' : 'Saginaw (City)'}, {'Kalamazoo' : 'Kalamazoo (City)'}, {'Muskegon' : 'Muskegon (City)'}]
counties=[]
cities = []


placenames={}
names={}

for county in center_dict["County"].keys():
    counties.append(county)

for city in center_dict["City"].keys():
    if city in name_case_ls:
        city = city + " (City)"
        cities.append(city)
    else:
        cities.append(city)


for eachcounty in counties:
    if eachcounty[0] not in placenames:
        placenames[eachcounty[0]]=[eachcounty]
    else:
        placenames[eachcounty[0]].append(eachcounty)


for eachcity in cities:
    if eachcity[0] not in placenames:
        placenames[eachcity[0]] = [eachcity]
        placenames[eachcity[0]].sort()
    else:
        placenames[eachcity[0]].append(eachcity)
        placenames[eachcity[0]].sort()


keyalphabet=sorted(placenames.keys())

for letter in keyalphabet:
    names[letter]=placenames[letter]
