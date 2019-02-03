#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:34:43 2019

@author: sunchuyue
"""

import csv
#fieldnames = ['institution', 'score']
def read_ranking(filename):
    companies = {}
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            companies[row['Title']] = row['Rank']
    return companies


