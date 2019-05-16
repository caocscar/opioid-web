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
center_dict = {'Detroit': '{lat: 42.35, lng: -83.09}',
    'Bay City': '{lat: 43.58, lng: -83.88}',
    'Flint': '{lat:43.013, lng:-83.69}',
    'Grand Rapids': '{lat:42.95, lng:-85.69}',
    'Pontiac': '{lat:42.65, lng:-83.3}',
    'Alcona': '{lat:44.68, lng:-83.58}',
    'Alger': '{lat:46.43, lng:-86.61}',
    'Allegan': '{lat:42.59, lng:-85.91}',
    'Alpena': '{lat:45.03, lng:-83.68}',
    'Antrim': '{lat:45.03, lng:-85.14}',
    'Arenac': '{lat:44.09, lng:-83.87}',
    'Baraga': '{lat:46.67, lng:-88.35}',
    'Barry': '{lat:42.59, lng:-85.31}',
    'Bay': '{lat:43.64, lng:-84.03}',
    'Benzie': '{lat:44.65, lng:-86.04}',
    'Berrien': '{lat:41.85, lng:-86.42}',
    'Branch': '{lat:41.93, lng:-85.05}',
    'Calhoun': '{lat:42.26, lng:-85.0}',
    'Cass': '{lat:41.93, lng:-85.99}',
    'Charlevoix': '{lat:45.22, lng:-85.06}',
    'Cheboygan': '{lat:45.44, lng:-84.48}',
    'Chippewa': '{lat:46.29, lng:-84.57}',
    'Clare': '{lat:44.0, lng:-84.85}',
    'Clinton': '{lat:42.99, lng:-84.6}',
    'Crawford': '{lat:44.65, lng:-84.61}',
    'Delta': '{lat:45.99, lng:-86.9}',
    'Dickinson': '{lat:45.98, lng:-87.87}',
    'Eaton': '{lat:42.59, lng:-84.84}',
    'Emmet': '{lat:45.53, lng:-84.92}',
    'Genesee': '{lat:43.00, lng:-83.69}',
    'Gladwin': '{lat:44.0, lng:-84.39}',
    'Gogebic': '{lat:46.38, lng:-89.7}',
    'Grand Traverse': '{lat:44.62, lng:-85.58}',
    'Gratiot': '{lat:43.29, lng:-84.61}',
    'Hillsdale': '{lat:41.93, lng:-84.59}',
    'Houghton': '{lat:47.05, lng:-88.61}',
    'Huron': '{lat:43.82, lng:-83.04}',
    'Ingham': '{lat:42.59, lng:-84.37}',
    'Ionia': '{lat:42.99, lng:-85.07}',
    'Iosco': '{lat:44.34, lng:-83.6}',
    'Iron': '{lat:46.19, lng:-88.55}',
    'Isabella': '{lat:43.64, lng:-84.85}',
    'Jackson': '{lat:42.26, lng:-84.42}',
    'Kalamazoo': '{lat:42.26, lng:-85.53}',
    'Kalkaska': '{lat:44.68, lng:-85.09}',
    'Kent': '{lat:43.03, lng:-85.53}',
    'Keweenaw': '{lat:47.31, lng:-88.17}',
    'Lake': '{lat:44.0, lng:-85.8}',
    'Lapeer': '{lat:43.1, lng:-83.22}',
    'Leelanau': '{lat:44.85, lng:-85.85}',
    'Lenawee': '{lat:41.93, lng:-84.06}',
    'Livingston': '{lat:42.59, lng:-83.91}',
    'Luce': '{lat:46.5, lng:-85.55}',
    'Mackinac': '{lat:46.08, lng:-84.89}',
    'Macomb': '{lat:42.67, lng:-82.92}',
    'Manistee': '{lat:44.32, lng:-86.05}',
    'Marquette': '{lat:46.37, lng:-87.69}',
    'Mason': '{lat:44.0, lng:-86.28}',
    'Mecosta': '{lat:43.64, lng:-85.32}',
    'Menominee': '{lat:45.5, lng:-87.55}',
    'Midland': '{lat:43.65, lng:-84.39}',
    'Missaukee': '{lat:44.32, lng:-85.09}',
    'Monroe': '{lat:41.93, lng:-83.57}',
    'Montcalm': '{lat:43.31, lng:-85.18}',
    'Montmorency': '{lat:45.0, lng:-84.13}',
    'Muskegon': '{lat:43.30, lng:-86.17}',
    'Newaygo': '{lat:43.55, lng:-85.8}',
    'Oakland': '{lat:42.66, lng:-83.39}',
    'Oceana': '{lat:43.64, lng:-86.29}',
    'Ogemaw': '{lat:44.32, lng:-84.13}',
    'Ontonagon': '{lat:46.68, lng:-89.37}',
    'Osceola': '{lat:44.0, lng:-85.33}',
    'Oscoda': '{lat:44.68, lng:-84.13}',
    'Otsego': '{lat:45.03, lng:-84.61}',
    'Ottawa': '{lat:42.99, lng:-86.03}',
    'Presque Isle': '{lat:45.29, lng:-83.93}',
    'Roscommon': '{lat:44.34, lng:-84.61}',
    'Saginaw': '{lat:43.35, lng:-84.03}',
    'St. Clair': '{lat:42.89, lng:-82.7}',
    'St. Joseph': '{lat:41.93, lng:-85.54}',
    'Sanilac': '{lat:43.42, lng:-82.81}',
    'Schoolcraft': '{lat:46.23, lng:-86.24}',
    'Shiawassee': '{lat:42.97, lng:-84.15}',
    'Tuscola': '{lat:43.48, lng:-83.4}',
    'Van Buren': '{lat:42.26, lng:-86.06}',
    'Washtenaw': '{lat:42.26, lng:-83.84}',
    'Wayne': '{lat:42.26, lng:-83.31}',
    'Wexford': '{lat:44.34, lng:-85.58}',
}
cities = ['Bay City','Detroit','Flint','Grand Rapids','Pontiac']
counties = [county for county in center_dict.keys() if county not in cities]
