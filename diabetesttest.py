# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy as sy
import pandas as pd

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)

list(diabetes_small)


from scipy.stats import ttest_ind

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

Caucasian = diabetes[diabetes['race']=='Caucasian']
African_American = diabetes[diabetes['race']=='AfricanAmerican']

from scipy.stats import ttest_ind

ttest_ind(Caucasian['time_in_hospital'], African_American['time_in_hospital'])

Asian = diabetes[diabetes['race']=='Asian']
African_American = diabetes[diabetes['race']=='AfricanAmerican']

from scipy.stats import ttest_ind

ttest_ind(Asian['num_lab_procedures'], African_American['num_lab_procedures'])




