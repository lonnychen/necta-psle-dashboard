#dashboard_config.py

#######################
#FOR 04-dashboard.ipynb
#######################

###########################
#Plotting/table DATA inputs
###########################

#ALL TABS
labels = {'average_5tile': 'PSLE quintile', 'average_300': 'PSLE average', 'n_schools': 'Number of schools'}
lat_lon_centre = {'lat': -6.826866, 'lon': 37.668493} #Morogoro MC council_hq
y_order = {'average_5tile': ['highest', 'fourth', 'middle', 'second', 'lowest']}

#PER-TAB LISTS
#Hover data input to maps: what gets seen during mouse hover
#Custom data input to maps: additional data for maps' `clickData` input to table
hover_data = list()
custom_data = list()
custom_data_DT = list()

#SCHOOLS TAB [0]
#Plotting/table data inputs
hover_data.append({'LATITUDE fix': False, 'LONGITUDE fix': False, 'average_300': True})
custom_data.append(['school_name', 'SCHOOL OWNERSHIP', 'TOTAL STUDENTS', #school info [0:3]
               'region_name', 'council_name', 'context', 'WARD', #location [3:7]
               'num_sitters', 'average_5tile', 'average_300', 'grade', 'pct_passed', 'results_url', #PSLE results [7:13]
               'PTR', 'PBR_std7', 'CG_per_student', #Resources [13:16]
               'approx_ages_mean', 'pop_3km', 'd_closest', 'd_council_hq']) #demographic/geographic [16:19]
custom_data_DT.append(['PRIMARY SCHOOL NAME', 'Ownership', 'Total students',
                  'Region', 'Council', 'Context', 'Ward',
                  'PSLE sitters', 'PSLE quintile', 'PSLE average (300)', 'PSLE average (grade)', 'PSLE % passed (A-C)', 'PSLE results URL',
                  'Pupil-to-Teacher Ratio (PTR)', 'Pupil-to-Book Ratio (PBR) (Std 7)', 'Capitation Grant (CG) per student (TZS)',
                  'Ages mean (approx.)', 'Population within 3km radius', 'Distance to closest other gov. school (km)', 'Distance to council headquarters (km)'])

#REGIONS TAB [1]
#Plotting/table data inputs
hover_data.append({'region_name': False, 'schools_n': True, 'average_300': True})
custom_data.append(['region_name', 'schools_n', 'councils_n', 'students_sum', #region info [0:3]
               'sitters_sum', 'average_300', 'pct_passed', #PSLE results [4:6]
               'PTR', 'PBR_std7', 'CG_per_student', #Resources [7:9]
               'approx_ages_mean', 'pop_3km', 'd_closest', 'd_council_hq']) #Demographics/Geography (Xd) [10:13]
custom_data_DT.append(['REGION', 'Number of schools', 'Number of councils', 'Total students (region)',
                  'PSLE sitters (region)', 'PSLE average (300)', 'PSLE % passed (A-C)',
                  'Pupil-to-Teacher Ratio (PTR)', 'Pupil-to-Book Ratio (PBR) (Std 7)', 'Capitation Grant (CG) per student (TZS)',
                  'Ages mean (approx.)', 'Population within 3km radius', 'Distance to closest other gov. school (km)', 'Distance to council headquarters (km)'])
