
# This is a project to predict the tendancy of WuHan 19 CoVirus 

import pandas as pd
import os
from os.path import join as opj


def data_read():
    
    dp = './19_nCoV_data/data-sources/dxy/data/'
    namelist = os.listdir(dp)
    namelist = [name for name in namelist if name[-3:] == 'csv']
    for n in namelist:
        data_org = opj(dp, n)

        a = pd.read_csv(data_org, header=None)
        a = a.iloc[3:-1].reset_index(drop=True)

        pp = [[], [], []]
        for each in a[0]:
            pp[0].append(each.split('|')[0])
            pp[1].append(int(each.split('|')[1]))
            pp[2].append(int(each.split('|')[2]))
        pp[0].append('China Total')
        pp[1].append(sum(pp[1]))
        pp[2].append(sum(pp[2]))
        places = pd.Series(pp[0])
        confs = pd.Series(pp[1])
        deaths = pd.Series(pp[2])
        new_df = pd.DataFrame(columns=['place', 'confirmed','deaths'])
        new_df['place'] = places
        new_df['confirmed'] = confs
        new_df['deaths'] = deaths

        print(n)
        print(new_df)





class SEIR(object):
    """
    build up an SEIR model for 
    """
    def __init__(self):
        pass

if __name__ == '__main__':
    data_read()
