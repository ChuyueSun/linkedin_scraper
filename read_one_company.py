#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:07:31 2019

@author: sunchuyue
"""

import csv
import re
from read_college_ranking import *

n_univ_dict = read_national_ranking('national_university_rankings.csv')
w_univ_dict = read_ranking('world_university_rankings.csv')
#print(w_univ_dict)


def read_one_company(filename):
    resumes = {}
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            raw = [item.strip() for item in re.split(re.compile('[\n,]'), row['educations'][1:-1])]
            i = 0
            flag = True
            current = {'educations':[]}
            while i < len(raw):
                if raw[i] == 'Field Of Study':
                    i += 2
                    continue
                if ('niversity' in raw[i] or 'ollege' in raw[i] or 'nstitute' in raw[i] or 'chool' in raw[i] or 'TKIET'in raw[i]) \
                        and ('from' not in raw[i]) and ('HIGH SCHOOL' not in raw[i].upper() and "St Xavier's School" not in raw[i]):
                    current['educations'].append([raw[i]])
                    i += 1
                    continue
                if raw[i] == 'Degree Name' and 'HIGH SCHOOL' not in raw[i+1].upper() and 'AISSCE' not in raw[i+1]:
                    if len(raw[i+1]) > 3:
                        if 'MBA' in raw[i+1] or 'M.B.A' in raw[i+1].upper():
                            current['educations'][-1].append('MBA')
                        elif 'MA' in raw[i+1] or 'M.A' in raw[i+1].upper():
                            current['educations'][-1].append('MA')
                        elif 'BA' in raw[i+1] or 'B.A' in raw[i+1].upper():
                            current['educations'][-1].append('BA')
                        elif 'MS' in raw[i+1] or 'M.S' in raw[i+1].upper():
                            current['educations'][-1].append('MS')
                        elif 'INCOMPLETE' in raw[i+1].upper():
                            current['educations'][-1].append('INCOMPLETE')
                        elif 'Master' in raw[i+1] or 'MLIS' in raw[i+1]:
                            current['educations'][-1].append('Master')
                        elif 'Bachelor' in raw[i+1] or 'B.Tech' in raw[i+1]:
                            current['educations'][-1].append('Bachelor')
                        elif 'Doctor' in raw[i+1]:
                            current['educations'][-1].append('Doctor')
                        elif 'JD' in raw[i+1] or 'J.D' in raw[i+1].upper():
                            current['educations'][-1].append('Doctor')
                        else:
                            print('Error:', raw)
                            flag = False
                    else:
                        current['educations'][-1].append(raw[i+1])
                    i += 2
                    continue
                i += 1
            if flag:
                aflag = True
                for item in current['educations']:
                    if len(item) != 2:
                        aflag = False
                        print('Input Error:',raw)
                if aflag:
                    resumes[row['name']] = current
    # print(resumes)
    return resumes


def evaluate_education(resumes):
    result = {}
    for name in resumes:
        current = {'education':[]}
        # print(resumes[name]['educations'][-1])
        current['education'].append(getEduScore(resumes[name]['educations'][0][0]))
        current['education'].append(getDegScore(resumes[name]['educations'][0][1]))
        result[name] = current



def getEduScore(uniName):
    # print(uniName)
    u = uniName.lstrip().rstrip()
    u = u.split(' - ')
    # print('u', u)
    for name in w_univ_dict:
        for un in u:
            if un in name:
                return w_univ_dict[name]
    print('Error in edu:', uniName)
    return 0

def getDegScore(deg):
    if deg.upper() in {'INCOMPLETE','N/A'}:
        return 0.5
    if deg in {'BBA','BA','BS','Bachelor','AB','BSE'}:
        return 1
    if deg in {'MS','MA','Master'}:
        return 2
    if deg in {'MBA', 'PhD', 'Doctor'}:
        return 3
    print('Error in Degree:',deg)

if __name__ == '__main__':
    resumes = read_one_company('Wells FargoLinkedIn.csv')
    evaluate_education(resumes)


