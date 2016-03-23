import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import matplotlib
from pandas.tools.plotting import scatter_matrix
from pandas.tools.plotting import parallel_coordinates
import os
import datetime
import pandas.io.data as web
import datetime
from pandas.io import wb
import scipy
import scipy.stats as stats
import gc
from alchemyapi import AlchemyAPI
import json
import csv

alchemyapi = AlchemyAPI()

#returns sentiment score,sentiment and topic/category
def getSentiment1(demo_text):
    if 1:
        #return 'Test'
        response = alchemyapi.sentiment('text', demo_text)
        response_t = alchemyapi.taxonomy('text', demo_text)

        if response['status'] == 'OK':

            x = response['docSentiment']['type']
        
   
            if 'score' in response['docSentiment']:
                y =  response['docSentiment']['score']
            else:
                y = 0

            return x
        else:
            if response['statusInfo'] == 'daily-transaction-limit-exceeded' :
                print('********************************************')
                print (response['statusInfo'])
                print('********************************************')                
            return response['statusInfo']



print   'Start .....'


t1 = datetime.datetime.now()
print os.getcwd()
#os.chdir("C:/Users/KaukabEnayet/Google Drive/Pyhton - project/Kaukab_working_directory/DATA/")
os.chdir("C:/Users/KaukabEnayet/OneDrive/004_MSBA/002_Fall/002_Exploratory/Group Project/Final")

email_csv = pd.read_csv('Emails.csv',sep = ',',header =  0, skiprows = 0)

email_csv2 = email_csv[0:7945]
#7944

email_csv2['ExtractedBodyText'].fillna('', inplace=True)
email_csv2['ExtractedSubject'].fillna('', inplace=True)
email_csv2['MetadataSubject'].fillna('', inplace=True)

#email_csv2['sentiment_body'] = ''
#email_csv2['sentiment_subj'] = ''
#email_csv2['sentiment_comb'] = ''

#email_csv2['body_length'] = -1
#email_csv2['subj_length'] = -1
#email_csv2['subj_word_count'] = -1
#email_csv2['body_word_count'] = -1

word_dict = dict()


for i in range(0,7945):
    if len(email_csv2['ExtractedSubject'][i]) == 0:
        email_csv2['ExtractedSubject'][i] = email_csv2['MetadataSubject'][i]
        
    if len(email_csv2['ExtractedBodyText'][i]) == 0:
        email_csv2['ExtractedBodyText'][i] = email_csv2['RawText'][i]        
    
    #email_csv2['sentiment_body'][i] = getSentiment1(email_csv2['ExtractedBodyText'][i])
    email_csv2.loc[i,('sentiment_body')] = getSentiment1(email_csv2['ExtractedBodyText'][i])
    
    #email_csv2['sentiment_subj'][i] = getSentiment1(email_csv2['ExtractedSubject'][i])
    email_csv2.loc[i,('sentiment_subj')] = getSentiment1(email_csv2['ExtractedSubject'][i])    
    
    #email_csv2['sentiment_comb'][i] = getSentiment1(email_csv2['ExtractedSubject'][i] +' '+ email_csv2['ExtractedBodyText'][i])
    email_csv2.loc[i,('sentiment_comb')] = getSentiment1(email_csv2['ExtractedSubject'][i] +' '+ email_csv2['ExtractedBodyText'][i])       
    
    #email_csv2['body_length'][i] = len(email_csv2['ExtractedBodyText'][i])
    email_csv2.loc[i,('body_length')]= len(email_csv2['ExtractedBodyText'][i])
    
    #email_csv2['subj_length'][i] = len(email_csv2['ExtractedSubject'][i])
    email_csv2.loc[i,('subj_length')]= len(email_csv2['ExtractedSubject'][i])
    
    #email_csv2['body_word_count'] = len(email_csv2['ExtractedBodyText'][i].split())
    email_csv2.loc[i,('body_word_count')]= len(email_csv2['ExtractedBodyText'][i].split())  
    
    #email_csv2['subj_word_count'] = len(email_csv2['ExtractedSubject'][i].split())
    email_csv2.loc[i,('subj_word_count')] = len(email_csv2['ExtractedSubject'][i].split())
    
    for word in email_csv2['ExtractedSubject'][i].split():
        temp = (filter(str.isalpha, word)).upper()
        if len(temp) > 3:
            word_dict[temp] = word_dict.get(temp, 0) + 1
    
    if i%100 == 0:
        print 'processed ...............  ' + str(i)
        print datetime.datetime.now()-t1
        t1 = datetime.datetime.now()







a = getSentiment1( 'good car') 
print a


email_csv2.to_csv('Hillary_emails.csv', sep=',')
#.apply(get_year_bucket, 1)

with open('word_count.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in word_dict.items()]
f.close()
