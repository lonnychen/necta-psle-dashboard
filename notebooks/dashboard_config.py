#dashboard_config.py

#######################
#FOR 04-dashboard.ipynb
#######################

###########################
#Plotting/table DATA inputs
###########################

initial_zoom = 4
school_map_zoom = 17
region_map_zoom = 8
color_values = ['average_300', 'grade', 'pct_passed', 'average_5tile', 'average_5tile_filtered', 'PTR', 'PBR_std7', 'BPR_std7', 'CG_per_student', 'approx_ages_mean', 'pop_3km', 'd_closest', 'd_council_hq']
color_labels = {'average_300': 'PSLE average (total 300)',
                'grade': 'Grade (A-E)', #category_orders
                'pct_passed': 'PSLE % passed (A-C)',
                'average_5tile': 'PSLE quintile (national)', #category_orders
                'average_5tile_filtered': 'PSLE quintile (filtered)', #category_orders
                'PTR': 'Pupil-to-Teacher Ratio (PTR)',
                'PBR_std7': 'Pupil-to-Book Ratio (PBR) (Std 7)',
                'BPR_std7': 'Book-to-Pupil Ratio (BPR) (Std 7)',
                'CG_per_student': 'Capitation Grant (CG) per student (TZS)',
                'approx_ages_mean': 'Ages mean (approx.)',
                'pop_3km': 'Population within 3km radius',
                'd_closest': 'Distance to closest other gov. school (km)',
                'd_council_hq': 'Distance to council headquarters (km)'}
category_orders = {'average_5tile': ['highest', 'fourth', 'middle', 'second', 'lowest'],
                   'average_5tile_filtered': ['highest', 'fourth', 'middle', 'second', 'lowest'],
                   'grade': ['A', 'B', 'C', 'D', 'E']}
tamisemi_url = 'https://www.tamisemi.go.tz/singleministers/basic-education-data-2022'

#REVIEW
labels = {'average_300': 'PSLE average', 'average_5tile': 'PSLE quintile', 'n_schools': 'Number of schools'}

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
                    'SCHOOL OWNERSHIP', 'TOTAL STUDENTS', #info [5:7]
                    'results_url', 'num_sitters', 'num_passed', 'average_300', 'grade', 'pct_passed', #PSLE results [7:13]
                    'PTR', 'PBR_std7', 'BPR_std7', 'CG_per_student', 'approx_ages_mean', #TAMISEMI [13:18]
                    'LATITUDE fix', 'LONGITUDE fix', 'pop_3km', 'd_closest', 'd_council_hq']) #demographic/geographic [18:23]

#REGIONS TRACE [1]
#Plotting/table data inputs
hover_data.append({'region_name': False, 'num_schools': True, 'average_300': ':.2f'})
custom_data.append(['region_name_full', #title [0]
                    'num_councils', 'num_schools', 'TOTAL_STUDENTS', #region info [1:4]
                    'results_url', 'num_sitters', 'num_passed', 'average_300', 'grade', 'pct_passed', #PSLE results [4:10]
                    'PTR', 'PBR_std7', 'BPR_std7', 'CG_per_student', 'approx_ages_mean', #TAMISEMI [10:15]
                    'map_url', 'pop_3km', 'd_closest', 'd_council_hq']) #Demographics/Geography (Xd) [15:19]
