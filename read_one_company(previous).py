#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 13:59:49 2019

@author: sunchuyue
"""

import csv
from read_college_ranking import *

n_univ_dict = read_national_ranking('national_university_rankings.csv')
#
#

w_univ_dict = read_ranking('world_university_rankings.csv')



def read_one_company(filename):
    resumes = {}
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            resumes[row['name']] = {'educations': row['educations'][1:-1].splitlines(), 'experiences':row['experiences'][1:-1].splitlines()}
        
    return resumes




resumes = read_one_company('berkshire hathawayLinkedIn.csv')


def rank_education(resumes):
    count = 0
    all_univ = []
    for person in resumes:
        education = resumes[person]['educations']
        univ_count = 0
        univ_score = 0
        universities = []
        while univ_count<len(education):  
            
            while univ_count<len(education) and education[univ_count] in ['Degree Name', 'Field Of Study']:
                univ_count+=2

            if univ_count>=len(education):
                break
            
            univ = education[univ_count].split(',')
            univ_count+=1
            for u in univ:
                u = u.lstrip().rstrip()
                if u[0].isdigit():
                    continue
                u = u.split(' - ')
                universities.append(u[0])
        all_univ+=universities
        
#        print('results!!!!!!',universities)
    
    in_w = 0
    l1 = []
    in_n = 0
    l2 = []
#    print(all_univ)
    for u in all_univ:
        if u in n_univ_dict:
            in_n+=1
            l1.append(u)
        if u in w_univ_dict:
            in_w+=1
            l2.append(u)
    print('world',in_w/len(resumes))
    print(l2)
    print('national',in_n/len(resumes))
    print(l1)
             
    

#rank_education(resumes)

def rank_experience(resumes):
    for person in resumes:
        experience  = resumes[person]['experiences']
        print(experience)
        
        
        
        
        
        
        
        
        
rank_experience(resumes)       
        
