#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 07:26:53 2018

@author: sunchuyue
"""
import csv
from bs4 import BeautifulSoup
import requests
import re
import random
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

def read_company_names():
    f = open('fortune500txt.txt', 'r')
    lines = f.readlines()
    company_names=[]
    for line in lines:
        elements = line.split()
        company=''
        for i in range(len(elements)):
            if i > 0 and i < len(elements)-1:
                company+=elements[i]+' '
                
        company_names.append(company[:-1])

    
    f.close()
    return company_names



company_names = read_company_names()




def get_url_via_Google(company_name,max_resume=45):
    
    
    if '&' in company_name:
        return None
    
    
    
    results = []
    failure = 0
    ip_pool = [
        '124.230.67.67:30519',
        '1.69.110.21:11063',
        '175.1.241.85:27172',
        '121.232.194.167:27408',
        '60.160.170.137:25510'
        '106.42.96.172:30186'
    ]
    temp_company=open(str(company_names.index(company_name)) + ' ' + company_name+'.csv','w')
    writer=csv.writer(temp_company)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    header = {
        "user-agent": user_agent,
    }
    url = 'https://www.google.com/search?q=' + company_name + '+site:linkedin.com/in'
    while len(url) > 0 and failure < 10:
        #count = -1
        width = len(ip_pool)
        try:
            #print(failure)
            #count += 1
            proxie_txt = ip_pool[random.randrange(0,4)]
            proxies = {
                'http': 'http://' + proxie_txt
            }
            r = requests.get(url, headers=header, proxies=proxies, timeout=10)
            r_text = r.text
            soup = BeautifulSoup(r_text, 'html.parser')
            #print(soup.prettify())
        except Exception as e:
            failure += 1
            #print(failure)
            continue
        if r.status_code == 200:
            hrefs = list(set(re.findall('https://www\.linkedin\.com/in/[a-zA-Z0-9-]+'.encode('utf-8'), r.content)))
            print(hrefs)
            writer.writerow(hrefs)
            results += hrefs
            max_resume -= len(hrefs)
            nextpage_txt = soup.find_all(name='a', class_="pn", id="pnnext")
#            print(nextpage_txt)
            nextpage = nextpage_txt[-1].get('href') if nextpage_txt else ''
            #print(nextpage)
            #print('http://www.google.com.tw' + nextpage.strip())
            url = 'https://www.google.com' + nextpage.strip()
            failure = 0
            #print(failure)

            if max_resume<=0:
                break
        else:
            failure += 2
            print(failure, proxie_txt)
            print('search failed: %s' % r.status_code)
            print(url)
    if failure >= 10:
        print('search failed: %s' % url)
    return results


if __name__ == '__main__':


#    company_name = input('Input the company you want to crawl:')
#    #lst = get_url_via_Baidu(company_name)
#    lst = get_url_via_Google(company_name)
#    print(lst)
    
    companies=company_names[365:380]
    print(companies)
    for each in companies:
        lst=[]
        lst = get_url_via_Google(each)
        print(lst)
    
  
    
#  'Intel',  'Prudential Financial','Albertsons Cos.','United Technologies','Marathon Petroleum'
#        'Disney','Humana','Pfizer','AIG','Lockheed Martin'
#    ['Sysco','FedEx','Hewlett Packard Enterprise','Cisco Systems','HP']
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    