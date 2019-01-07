import copy
import time
from urllib.parse import unquote
import requests
from urllib.parse import quote
import re
from lxml import etree
from bs4 import BeautifulSoup

headersParameters = {  # 发送HTTP请求时的HEAD信息，用于伪装为浏览器
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }


def get_url_via_Baidu(company_name, maxpage=2):

    url = u'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baiduadv&wd=inurl%3A%20linkedin.com%2Fin%2F%20' + company_name + '&oq=inurl%253A%2520linkedin.com%252Fin%252F&sl_lang=en&rsv_srlang=en'
    #print(url)
    failure = 0
    results = []
    while len(url) > 0 and failure < 10:
        try:
            r = requests.get(url, timeout=10, headers=headersParameters)
            r_text = r.text
            soup = BeautifulSoup(r_text, 'html.parser')
            #print(r.status_code, '\n', soup.prettify())
        except Exception as e:
            failure += 1
            continue
        if r.status_code == 200:
            hrefs = list(
                set(re.findall('"(http://www\.baidu\.com/link\?url=.*?)"'.encode('utf8'), r.content)))  # 一页有10个搜索结果
            results += hrefs
            #print(hrefs)
            tree = etree.HTML(r.content)
            nextpage_txt = tree.xpath('//div[@id="page"]/a[@class="n" and contains(text(), "下一页")]/@href')
            url = 'http://www.baidu.com' + nextpage_txt[0].strip() if nextpage_txt else ''
            failure = 0
            maxpage -= 1
            if maxpage <= 0:
                break
        else:
            failure += 2
            print('search failed: %s' % r.status_code)
    if failure >= 10:
        print('search failed: %s' % url)
    return results


def get_linkedin_url(url):
    """ 百度搜索出来的是百度跳转链接，要从中提取出linkedin链接 """
    try:
        r = requests.get(url, allow_redirects=False, headers=headersParameters)
        r_text=r.text
        soup = BeautifulSoup(r_text, 'html.parser')
#        print(soup.prettify())
        if r.status_code == 302 and 'Location' in list(r.headers.keys()) and 'linkedin.com/in/' in r.headers['Location']:
            new_url = r.headers['Location']
            print(new_url)
            print('inside')
            b = re.findall('^(https://www\.linkedin\.com/)', new_url)
            print(b)            
            
            new_url = r.headers['Location']
            b = re.findall('^(https://www\.linkedin\.com/)', new_url)
            if b == []:
                b = re.findall('^(http://www\.linkedin\.com/)', new_url)
            if  b != []:
                return new_url
            else:
                return ''
    except Exception as e:
        print('get linkedin url failed: %s' % url)
    return ''


#print(get_linkedin_url('http://www.baidu.com/link?url=pw5EbHF8pHQTXOOcI_SxCYn3Hr4jr8tfb9Ak96mN70Dc53iwGO6YGOCdm3fQBB5T'))

if __name__ == '__main__':
    company_name = input('Input the company you want to crawl:')
    raw_results = get_url_via_Baidu(company_name,10)
#    print(raw_results)
    results = []
    for url in raw_results:
        true_url = get_linkedin_url(url)
        if true_url != '':
            results.append(true_url)
    print(results)