<p align="center">
<b><a href="#Summary">Summary</a></b>
|
<b><a href="#Project-Documentation">Project Documentation</a></b>
|
<b><a href="#Engagement">Engagement</a></b>
|    
<b><a href="#Data-Sources-and-Methodology">Data Sources and Methodology</a></b>
|
<b><a href="#Next-Steps">Next Steps</a></b>
</p>

# NECTA PSLE Dashboard
This repository contains the notebooks and data used by the Data Safari team to create the dashboard publicly accessible at https://bit.ly/psle2022mvp.

## Summary
----------

### Inspiration
Every year in Tanzania, the publication of Primary School Leaving Examination (PSLE) results is a national data moment for students, parents, teachers, schools, and the government, traditionally determining placement of standard seven leavers into secondary school. Student results are found on per-school web pages but access to wider analysis such as urban vs. rural or regional comparisons, beyond the now de-prioritized rankings, is still needed. Further linking results data to school resources, and geographical features (proxies of urbanity/rurality) provides an untapped opportunity to use data to inform local and national policy decisions, and improve educational outcomes.

### Dashboard
Our solution is a publicly accessible data dashboard that is intuitive and attractive to the general public, and flexible and powerful enough to enable deep technical analysis. By providing a platform for anyone to discover data-driven insights, we hope to contribute to systematic data-driven improvements in the education sector in Tanzania, and collaborate with and inspire others to do the same globally. Dashboard features include:
- **Interactive maps** to visualize and access data at various levels
- **Analysis tab** for both univariate and bivariatee data exploration
- **Prediction tab** for machine learning predictions

### Users
Specific user groups include:
- **Government education authorities:** policy evaluation and setting
- **School administrators:** resource review and advocacy
- **Education sector funders and NGOs:** target funding gaps
- **Researchers:** expedite their own analysis needs

### Caveats
We recognize that:
- Examination performance do not represent actual **learning outcomes** and abilities.
- There are a constellation of **socio-economic factors** beyond school resources or geography that affect a student's performance. Any lack of pattern-finding or predictability can and should inform the need to collect that "missing" data such as the existence of local initiatives (test camps), teacher motivation and teaching approaches, effective resource use, and student study habits.

## Project Documentation
----------
### Data Documents
Two documents are useful to understand the data used:
- <data_dictionary.xlsx>
- <data_provenance.xlsx>

### Notebooks
Jupyter notebooks are used to run project code. Some documentation conventions:

**Learnings:**
- 🧑🏻‍💻 Python and libraries
- 📚 Machine Learning
- 😎 Cool concepts
- ⚠️ Gotchas!


## Engagement
----------
We at Data Safari are always interested to engage with interested people to improve our products, collaborate on projects, or collectively build capacities to create data-driven solutions. Please reach out us at hello@datasafari.io or fill in the contact form on our dashboard (to-be-added).

## Data Sources and Methodology
----------
- **National Examinations Council of Tanzania (NECTA):** This council adminsters and publshes PSLE (and other exams) data on their [PSLE Results](https://necta.go.tz/psle_results) portal. Going down the administrative divisions, the individual school pagse are found, for example here for [Jitegemee Primary School](https://onlinesys.necta.go.tz/results/2022/psle/results/shl_ps1104063.htm) in Morogoro Municipality, Morogoro Region. We webscraped all of these pages, resulting in a DataFrame of **17,900 schools** (public and private) with non-missing results data. The "WASTANI WA SHULE" number is the average of all students for that school out of a total of 300, 50 each for the six tested subjects of Kiswahili, English, Social Studies, Mathematics, Science, and Civics. **The notebook can be found at <01-webscrape-necta.ipynb>** Results data have various permutations:
    - `average_300` (float)
    - `y_2tile`, `y_5tile` quantiles (cat)
    - `pct_passed` with A-C grades (float)<br><br>
- **President's Office - Regional Administration and Local Government (TAMISEMI):** This central authority for coordinating regional and local development initiatives collects and publishes per-school resources, ages, and gender data annually, such as here for [Basic Education Data 2022](https://www.tamisemi.go.tz/singleministers/basic-education-data-2022). **The notebook can be found at <02-merge-tamisemi.ipynb>** Collected data include:
    - Location: geo-coordinates, region, council, ward
    - School ownership: government or non-government
    - Pupil-to-Teacher Ratio (PTR)
    - Pupil-to-Book Ratio (PBR)
    - Capitation Grant amounts (CG)
    - Ages and gender data<br><br>
- **Extracted geographical data:** Three parameters were then extracted based on geo-coordinates (government-only). **The notebook can be found at <04-feature-extraction.ipynb>**:
    - Distance to closest other school 
    - Distance to council headquarters
    - Population density: [Meta Data for Good source](https://dataforgood.facebook.com/dfg/tools/high-resolution-population-density-maps), [mWater data query](https://portal.mwater.co/#/resource_center/population_queries)

## Next Steps
----------
1. Additional dashboard features and tabs
2. Integrate time-series data from 2013-21


```python

```
