from bs4 import BeautifulSoup
import requests
import re
import random
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


def get_url_via_Google(company_name, maxpage=4,max_resume=20):
    results = []
    failure = 0
    ip_pool = [
        '119.98.44.192:8118',
        '10.10.1.10:3128',
        '111.198.219.151:8118',
        '101.86.86.101:8118'
    ]
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
            results += hrefs
            max_resume -= len(hrefs)
            nextpage_txt = soup.find_all(name='a', class_="pn", id="pnnext")
            print(nextpage_txt)
            nextpage = nextpage_txt[-1].get('href') if nextpage_txt else ''
            #print(nextpage)
            #print('http://www.google.com.tw' + nextpage.strip())
            url = 'https://www.google.com' + nextpage.strip()
            failure = 0
            #print(failure)
            maxpage -= 1
            if maxpage <= 0 or max_resume<=0:
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
    company_name = input('Input the company you want to crawl:')
    #lst = get_url_via_Baidu(company_name)
    lst = get_url_via_Google(company_name)
    print(lst)
