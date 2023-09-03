#dashboard_config.py

#######################
#FOR 04-dashboard.ipynb
#######################

###########################
#Plotting/table DATA inputs
###########################

#Map zoom levels
initial_zoom = 4
school_map_zoom = 17
region_map_zoom = 8

#URLs
tamisemi_url = 'https://www.tamisemi.go.tz/singleministers/basic-education-data-2022'

#Columns > labels
#color_options* #Moved to data_dictionary_dashboard.csv
context_options = {'urban': ' Urban',
                   'rural': ' Rural'}

#Categorical data
category_orders = {'average_5tile': ['highest', 'fourth', 'middle', 'second', 'lowest'],
                   'average_5tile_filtered': ['highest', 'fourth', 'middle', 'second', 'lowest'],
                   'grade': ['A', 'B', 'C', 'D', 'E']}

#Numerical data
floats_to_round = ['pct_passed', 'PTR', 'PBR_std7', 'BPR_std7', 'approx_ages_mean', 'd_closest', 'd_council_hq']

#PER-MAP TRACE LISTS
#Hover data input to maps: what gets seen during mouse hover
hover_data = list()
#Custom data input to maps: additional data for maps' `clickData` input to table
custom_data = list()

#SCHOOLS TRACE [0]
#Plotting/table data inputs
hover_data.append({'LATITUDE fix': False, 'LONGITUDE fix': False, 'average_300': ':.2f'})
custom_data.append(['school_name', 'school_id', #title [0:2]
                    'WARD', 'council_name', 'region_name', #location[2:5]
                    'SCHOOL OWNERSHIP', 'TOTAL STUDENTS', 'results_url', #info [5:8]
                    'num_sitters', 'num_passed', 'pct_passed', 'average_300', 'grade', 'average_5tile', #PSLE results [8:14]
                    'PTR', 'PBR_std7', 'BPR_std7', 'CG_per_student', 'approx_ages_mean', #TAMISEMI [14:19]
                    'LATITUDE fix', 'LONGITUDE fix', 'pop_3km', 'd_closest', 'd_council_hq']) #demographic/geographic [19:24]

#REGIONS TRACE [1]
#Plotting/table data inputs
hover_data.append({'region_name': False, 'num_schools': True, 'average_300': ':.2f'})
custom_data.append(['region_name_full', #title [0]
                    'num_councils', 'num_schools', 'TOTAL_STUDENTS', 'results_url', #region info [1:5]
                    'num_sitters', 'num_passed', 'pct_passed', 'average_300', 'grade', 'average_5tile', #PSLE results [5:11]
                    'PTR', 'PBR_std7', 'BPR_std7', 'CG_per_student', 'approx_ages_mean', #TAMISEMI [11:16]
                    'map_url', 'pop_3km', 'd_closest', 'd_council_hq']) #Demographics/Geography (Xd) [16:20]
