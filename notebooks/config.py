#config.py

#############################
#FOR 01-necta-webscrape.ipynb
#############################

#Config paths - URLs
exam_year = '2022'
exam_type = 'psle'
base_URL = f"https://onlinesys.necta.go.tz/results/{exam_year}/{exam_type}/"
top_URL = f"{exam_type}.htm"

#Config paths - CSVs
necta_raw_csv_path = '../data/raw/necta/01-necta-webscrape_raw.csv'
necta_missing_csv_path = '../data/raw/necta/01-necta-webscrape_missing.csv'
necta_features_csv_path = '../data/intermediate/01/01-necta-webscrape_features.csv'

############################
#FOR 02-tamisemi-merge.ipynb
############################

#TAMISEMI 1
#Paths
ts1_url = 'https://www.tamisemi.go.tz/storage/app/epr42022/Consolidated_Primary_EnrolmentbyGrade_PTR_2022_PSLE2021.xlsx'
ts1_xlsx = '../data/raw/tamisemi/Consolidated_Primary_EnrolmentbyGrade_PTR_2022_PSLE2021.xlsx'
necta_ts1_csv_path = '../data/intermediate/02/02-tamisemi-merge_ts1_merged.csv'
necta_ts1_unjoined_csv_path = '../data/intermediate/02/02-tamisemi-merge_ts1_unjoined.csv'
#Variables
ts1_cols = ['REGION', 'COUNCIL', 'WARD', 'SCHOOL NAME', 'SCHOOL REG. NUMBER', 'NECTA EXAM CENTRE NO',\
            'SCHOOL OWNERSHIP', 'LATITUTE', 'LONGITUDE', 'TOTAL BOYS', 'TOTAL GIRLS', 'PTR']
ts1_nid = 'NECTA EXAM CENTRE NO'
ts1_nid_fix = f'{ts1_nid} fix'
ts1_nid_is_fixed = f'{ts1_nid} is_fixed'
ts1_sch = 'SCHOOL NAME'
ts1_sch_fix = f'{ts1_sch} fix'
ts1_sch_is_fixed = f'{ts1_sch} is_fixed'
ts1_council_replaces = ['Kahama MC', 'Kigoma/Ujiji MC', 'Mtwara Mikindani MC']
ts1_council_values = ['Kahama TC', 'Kigoma MC', 'Mtwara MC']

#TAMISEMI 2
#Paths
ts2_url = 'https://www.tamisemi.go.tz/storage/app/epr42022/Primary%20Textbooks%20and%20PBR,%202022%20(1).xlsx'
ts2_xlsx = '../data/raw/tamisemi/Primary Textbooks and PBR, 2022 (1).xlsx'
necta_ts2_csv_path = '../data/intermediate/02/02-tamisemi-merge_ts2_merged.csv'
#Variables
ts2_cols_pupils = ['Std 7-Pupils']
ts2_cols_books = ['Std 7-English', 'Std 7-Maarifa ya Jamii', 'Std 7-Mathematics',\
                  'Std 7-Sayansi na Teknolojia', 'Std 7-Kiswahili', 'Std 7-Uraia na maadili']
ts2_cols_pbr = ['PBR-Std 7-English', 'PBR-Std 7-Maarifa ya Jamii', 'PBR-Std 7-Mathematics',\
                'PBR-Std 7-Sayansi na Teknolojia', 'PBR-Std 7-Kiswahili', 'PBR-Std 7-Uraia na maadili']
ts2_cols = ['School Name', 'Reg Number'] + ts2_cols_pupils + ts2_cols_books + ts2_cols_pbr

#TAMISEMI 3
#Paths
ts3_url = 'https://www.tamisemi.go.tz/storage/app/epr42022/School_CG_Primary_2021-2022%20(2).xlsx'
ts3_xlsx = '../data/raw/tamisemi/School_CG_Primary_2021-2022 (2).xlsx'
necta_ts3_csv_path = '../data/intermediate/02/02-tamisemi-merge_ts3_merged.csv'
#Variables
ts3_cols = ['SCHOOL NAME', 'Reg#', 'TOTAL']
cg_rate_tuple = ('CG_TOTAL', 'TOTAL STUDENTS', 'CG_per_student')

#TAMISEMI 4
#Paths
ts4_url = 'https://www.tamisemi.go.tz/storage/app/epr42022/Enrollment%20in%20Government%20and%20Non_Government%20Primary%20Schools%20by%20Age%20and%20Sex_2022.xlsx'
ts4_xlsx = '../data/raw/tamisemi/Enrollment in Government and Non_Government Primary Schools by Age and Sex_2022.xlsx'
necta_ts_merged_path = '../data/intermediate/02/02-tamisemi-merge.csv'

#################################
#FOR 03-feature-extraction.ipynb
#################################

#Feature Extraction 1 (fe1)
fe1_mwater_path = '../data/manual/03-mwater_latlon_fixes_population.csv' 
fe1_mwater_cols_concat = ['Name', 'LATITUDE fix', 'LONGITUDE fix', 'pop_3km']
lat_col = 'LATITUDE'
lat_col_fix = f'{lat_col} fix'
lat_col_is_fixed = f'{lat_col} is_fixed'
lon_col = 'LONGITUDE'
lon_col_fix = f'{lon_col} fix'
lon_col_is_fixed = f'{lon_col} is_fixed'
fe1_csv_path = '../data/intermediate/03/03-feature-extraction_fe1.csv'

#Feature Extraction 2 (fe2)
fe2_csv_path = '../data/intermediate/03/03-feature-extraction_fe2.csv'

#Feature Extraction 3 (fe3)
fe3_mwater_path = '../data/manual/03-mwater_council_hq_coords.csv'
fe3_csv_path = '../data/intermediate/03/03-feature-extraction_fe3.csv'

#Feature Extraction 4 (fe4)
fe_csv_path = '../data/deployable/03-feature-extraction.csv'
