from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import random as r
from scipy import stats
import scipy
import math


# Calculate crime_y12_y12 rate
un_rate=pd.read_csv('Zip_county.csv')
Unemp=pd.read_csv('crate_year.csv')
crime=pd.read_csv('Python_totalsheet.csv')
crime=crime[["City","INSTNM","ZIP","Total","nca_12","ncc_12","ncd_12","oca_12","occ_12","ocd_12","ppa_12","ppc_12","ppd_12","nca_11","ncc_11","ncd_11","oca_11","occ_11","ocd_11","ppa_11","ppc_11","ppd_11"]]


crime['Crime11']=crime["nca_11"]+crime["ncc_11"]+crime["ncd_11"]+crime["oca_11"]+crime["occ_11"]+crime["ocd_11"]+crime["ppa_11"]+crime["ppc_11"]+crime["ppd_11"]
crime['Rate11']=crime['Crime11']/crime["Total"]


#groupby institutions
sub_group1 = crime.iloc[:,0:4]
sub_grouped1 = sub_group1.groupby('INSTNM',as_index = False).mean()

# groupby to get num of crime 
sub_group2 = crime.iloc[:,1:2]
sub_group2['Crime11'] = crime['Crime11']
sub_grouped2 = sub_group2.groupby('INSTNM',as_index = False).sum()
data = pd.merge(sub_grouped1,sub_grouped2, on='INSTNM')
data['CrimeRate'] = data['Crime11']/data['Total']

#match county to zip code
data['ZIP_county'] = data['ZIP'].astype(str).str[:5]
data['ZIP_county'] = data['ZIP_county'].str.replace('.','').astype(int)

#match county unemp data to campus
un_rate['ZIP_county']=un_rate['ZIP']
result1 = pd.merge(data,un_rate, how='inner', on ='ZIP_county')
result2 = pd.merge(result1, Unemp, how = 'inner', on = 'county')

result11=result2[["county","INSTNM","CrimeRate","Unemp_11","ZIP_county"]].dropna()
avg_crimerate = result11['CrimeRate'].mean()
avg_unem = result11['Unemp_11'].mean()


# calculate high or low crime rate and high or low unemployment
result11['CH'] = result11['CrimeRate'] > avg_crimerate
result11['CH'] = result11['CH'].astype(int)
result11['CL'] = result11['CrimeRate'] < avg_crimerate
result11['CL'] = result11['CL'].astype(int)
result11['UH'] = result11['Unemp_11'] > avg_unem
result11['UH'] = result11['UH'].astype(int)
result11['UL'] = result11['Unemp_11'] < avg_unem
result11['UL'] = result11['UL'].astype(int)

c=DataFrame(result11)
c=c.groupby(['UH','UL']).sum()

#calculating z score and p value
z_scores=[-4.76759,4.907776,4.76759,-4.907776]
z_scores=Series(z_scores)
p_values_h0 = scipy.stats.norm.sf(abs(z_scores[0]))*2
z_scores=DataFrame(z_scores)
z_scores.columns=['z score']
z_scores['p value']=z_scores.apply( lambda x:  scipy.stats.norm.sf(abs(z_scores['z score']))*2)

print z_scores