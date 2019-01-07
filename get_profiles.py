#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:19:26 2018

@author: sunchuyue
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from linkedin_scraper import Person
import csv


diver = webdriver.Chrome(executable_path='/Users/sunchuyue/bin/chromedriver')

def login():
    diver.get('https://www.linkedin.com/')
    #等待网站加载完成
    time.sleep(1)
    #模拟登陆
    diver.find_element_by_id('login-email').send_keys('anniescy@126.com')
    diver.find_element_by_id('login-password').send_keys('0@Anniescy')
    # 点击跳转
    diver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    time.sleep(1)


#



login()




facebook=[b'https://www.linkedin.com/in/johncantarella', b'https://www.linkedin.com/in/fvarela', b'https://www.linkedin.com/in/pratitirc', b'https://www.linkedin.com/in/sachin-kulkarni-9a36364', b'https://www.linkedin.com/in/celiena-adcock', b'https://www.linkedin.com/in/vivsha', b'https://www.linkedin.com/in/dlrose', b'https://www.linkedin.com/in/nickgrudin', b'https://www.linkedin.com/in/kyle-o-connor-2230b896', b'https://www.linkedin.com/in/madractas', b'https://www.linkedin.com/in/mrabkin', b'https://www.linkedin.com/in/frerkmaltefeller', b'https://www.linkedin.com/in/parthdetroja', b'https://www.linkedin.com/in/angelg7', b'https://www.linkedin.com/in/ryanbiega', b'https://www.linkedin.com/in/thejeslee', b'https://www.linkedin.com/in/kunalmerchant', b'https://www.linkedin.com/in/will-castleberry-3324a4126', b'https://www.linkedin.com/in/karandeep', b'https://www.linkedin.com/in/gaurav-dosi-52099119', b'https://www.linkedin.com/in/alexstamos', b'https://www.linkedin.com/in/hemabudaraju', b'https://www.linkedin.com/in/loganbarrett', b'https://www.linkedin.com/in/akos-lada-737aba31', b'https://www.linkedin.com/in/pcanahuati', b'https://www.linkedin.com/in/andyoconnell', b'https://www.linkedin.com/in/nadastirratt', b'https://www.linkedin.com/in/francesca-de-quesada-covey-271318b', b'https://www.linkedin.com/in/chris-lunny-625949b', b'https://www.linkedin.com/in/aaronbernstein', b'https://www.linkedin.com/in/willemsuyderhoud', b'https://www.linkedin.com/in/adamsberger', b'https://www.linkedin.com/in/dpweiss', b'https://www.linkedin.com/in/christen-dubois-1791491b', b'https://www.linkedin.com/in/joesullivanusa', b'https://www.linkedin.com/in/morganbeller', b'https://www.linkedin.com/in/tamara-hrivnak-7696b6aa', b'https://www.linkedin.com/in/trevorlindsay', b'https://www.linkedin.com/in/jdulski', b'https://www.linkedin.com/in/ashton-smith-5264a057', b'https://www.linkedin.com/in/danlevyusa', b'https://www.linkedin.com/in/pelkinswilliams', b'https://www.linkedin.com/in/kat-johnston-43b2258', b'https://www.linkedin.com/in/richardrosenow', b'https://www.linkedin.com/in/chris-petersen-379b816', b'https://www.linkedin.com/in/kat-johnston-43b2258', b'https://www.linkedin.com/in/bshomair', b'https://www.linkedin.com/in/davej95', b'https://www.linkedin.com/in/bowenpan', b'https://www.linkedin.com/in/jay-hammonds-1a204242', b'https://www.linkedin.com/in/aaron-russell-970a9a54', b'https://www.linkedin.com/in/jomaa', b'https://www.linkedin.com/in/grahammudd', b'https://www.linkedin.com/in/sarahsled', b'https://www.linkedin.com/in/tejaspatil1', b'https://www.linkedin.com/in/brian-lewis-4893', b'https://www.linkedin.com/in/pefa1', b'https://www.linkedin.com/in/willie-henry-74b3475', b'https://www.linkedin.com/in/sachinnanavati', b'https://www.linkedin.com/in/jessica-kornstein-bab4466a', b'https://www.linkedin.com/in/kahinavandyke', b'https://www.linkedin.com/in/nadir-joshua-86161010', b'https://www.linkedin.com/in/reginald-mcknight-b415b1a', b'https://www.linkedin.com/in/ashishkelkar', b'https://www.linkedin.com/in/julian-nagler-a81b2632', b'https://www.linkedin.com/in/gabe-ledeen-46b81318', b'https://www.linkedin.com/in/mark-chevillet-971a001b', b'https://www.linkedin.com/in/bradtmurphy', b'https://www.linkedin.com/in/danzigmond', b'https://www.linkedin.com/in/seandryan', b'https://www.linkedin.com/in/colleenhenry', b'https://www.linkedin.com/in/kingjeff', b'https://www.linkedin.com/in/dgershenson', b'https://www.linkedin.com/in/tyahma', b'https://www.linkedin.com/in/dwaynereeves', b'https://www.linkedin.com/in/ross-sparkman-msc-mba-mhr-12710b14', b'https://www.linkedin.com/in/underwoodjamesm', b'https://www.linkedin.com/in/victoria-grand-ab944234', b'https://www.linkedin.com/in/gisellehale', b'https://www.linkedin.com/in/itamar-rosenn-44b0278', b'https://www.linkedin.com/in/felix9289', b'https://www.linkedin.com/in/kimberlybirch', b'https://www.linkedin.com/in/antigone-davis-b0a8b4103', b'https://www.linkedin.com/in/jwalker79', b'https://www.linkedin.com/in/sandeep-solanki-1b405a19', b'https://www.linkedin.com/in/rodrigoschmidt', b'https://www.linkedin.com/in/meihong', b'https://www.linkedin.com/in/jason-white-11999534', b'https://www.linkedin.com/in/michael-mcnally', b'https://www.linkedin.com/in/connorhayes', b'https://www.linkedin.com/in/steven-chen-72bab218', b'https://www.linkedin.com/in/ann-mack-73061a4', b'https://www.linkedin.com/in/jenlouis', b'https://www.linkedin.com/in/jcolman', b'https://www.linkedin.com/in/xiaoyinqu', b'https://www.linkedin.com/in/yuankai', b'https://www.linkedin.com/in/maryhaile', b'https://www.linkedin.com/in/erikhawkins', b'https://www.linkedin.com/in/janeschachtel', b'https://www.linkedin.com/in/cpgupta561', b'https://www.linkedin.com/in/topdror', b'https://www.linkedin.com/in/brfishman', b'https://www.linkedin.com/in/steve-biddle-2123013', b'https://www.linkedin.com/in/andymitchell1', b'https://www.linkedin.com/in/stephaniesmerigliolatham', b'https://www.linkedin.com/in/jennsy', b'https://www.linkedin.com/in/rgarg2', b'https://www.linkedin.com/in/david-hansell-aa76a8100', b'https://www.linkedin.com/in/devimahadevia', b'https://www.linkedin.com/in/marta-mateu-2b19b041', b'https://www.linkedin.com/in/tom-williams-a2b65513', b'https://www.linkedin.com/in/mohanshivani', b'https://www.linkedin.com/in/lguang', b'https://www.linkedin.com/in/nazareth-vartanian-1b773313', b'https://www.linkedin.com/in/cat-cobb', b'https://www.linkedin.com/in/jblanton', b'https://www.linkedin.com/in/chris-sonderby-255a3756', b'https://www.linkedin.com/in/jamespearce', b'https://www.linkedin.com/in/toryhargro', b'https://www.linkedin.com/in/karin-tracy-89158427', b'https://www.linkedin.com/in/abby-rose-4686b729', b'https://www.linkedin.com/in/kellystonelake', b'https://www.linkedin.com/in/pierre-roux-45a9171', b'https://www.linkedin.com/in/brucehazan', b'https://www.linkedin.com/in/erin-egan-01329878', b'https://www.linkedin.com/in/mattpaster', b'https://www.linkedin.com/in/vivian-van-52a4a88b', b'https://www.linkedin.com/in/ewardthomas', b'https://www.linkedin.com/in/rodneytabares', b'https://www.linkedin.com/in/vaughnhester', b'https://www.linkedin.com/in/lt-clay-74a6799', b'https://www.linkedin.com/in/aaratisoman', b'https://www.linkedin.com/in/rdurga', b'https://www.linkedin.com/in/nora-chan-41659447', b'https://www.linkedin.com/in/sloukakos', b'https://www.linkedin.com/in/stacy-chen-a9bb3134', b'https://www.linkedin.com/in/aanchalgupta', b'https://www.linkedin.com/in/candytien', b'https://www.linkedin.com/in/waltxie', b'https://www.linkedin.com/in/kemalelmoujahid', b'https://www.linkedin.com/in/diannayau', b'https://www.linkedin.com/in/nona-c-jones-mba-b30a948', b'https://www.linkedin.com/in/molly-jackman-1a757644', b'https://www.linkedin.com/in/emekaafigbo', b'https://www.linkedin.com/in/zhen-li-6b73975', b'https://www.linkedin.com/in/felipe-angel-6b930170', b'https://www.linkedin.com/in/jeanetterodriguez0716', b'https://www.linkedin.com/in/ericporterfield', b'https://www.linkedin.com/in/emily-vacher-3ab30845', b'https://www.linkedin.com/in/raquel-lucente-55785a19', b'https://www.linkedin.com/in/leathern', b'https://www.linkedin.com/in/paytoniaiheme', b'https://www.linkedin.com/in/ipsitapaul', b'https://www.linkedin.com/in/chloepark', b'https://www.linkedin.com/in/jamiesmolski', b'https://www.linkedin.com/in/tallythoren', b'https://www.linkedin.com/in/shona-button-467ba4a', b'https://www.linkedin.com/in/yini-guo-8a65a729', b'https://www.linkedin.com/in/elle-white-b14b4746', b'https://www.linkedin.com/in/devon-williams-bb07564', b'https://www.linkedin.com/in/iizrailov', b'https://www.linkedin.com/in/laiturn', b'https://www.linkedin.com/in/joelp', b'https://www.linkedin.com/in/collmill', b'https://www.linkedin.com/in/connie-chung-19905856', b'https://www.linkedin.com/in/lisadconn', b'https://www.linkedin.com/in/george-alafoginis-930254110', b'https://www.linkedin.com/in/chengevan', b'https://www.linkedin.com/in/david-ginsberg-6064145', b'https://www.linkedin.com/in/vcallisonburch', b'https://www.linkedin.com/in/carlosgomezuribe', b'https://www.linkedin.com/in/laurajuanes', b'https://www.linkedin.com/in/hbarra', b'https://www.linkedin.com/in/kaiyawaddell', b'https://www.linkedin.com/in/john-morgan-99406b1', b'https://www.linkedin.com/in/tobyroessingh', b'https://www.linkedin.com/in/kel-lau-710b97a2', b'https://www.linkedin.com/in/charlie-wyman-33276749', b'https://www.linkedin.com/in/ryanmackfb', b'https://www.linkedin.com/in/ewamai', b'https://www.linkedin.com/in/jeffhuang', b'https://www.linkedin.com/in/mayapatterson', b'https://www.linkedin.com/in/atish-banerjea-540764129', b'https://www.linkedin.com/in/erinmurraymanning', b'https://www.linkedin.com/in/john-tenanes-4b7848', b'https://www.linkedin.com/in/lars-backstrom-862a764', b'https://www.linkedin.com/in/gavin-corn-a59b6484', b'https://www.linkedin.com/in/lewis-knight-6201777', b'https://www.linkedin.com/in/patrickharris', b'https://www.linkedin.com/in/carolyn-everson-8633479', b'https://www.linkedin.com/in/bweihl', b'https://www.linkedin.com/in/matiasc', b'https://www.linkedin.com/in/bobby-hollis-a334474', b'https://www.linkedin.com/in/sunita-parasuraman-77b63812', b'https://www.linkedin.com/in/donseymour', b'https://www.linkedin.com/in/monika-bickert-10961250', b'https://www.linkedin.com/in/sarah-personette-4b71125', b'https://www.linkedin.com/in/matt-perault-54455b10b', b'https://www.linkedin.com/in/philliprather', b'https://www.linkedin.com/in/allison-ball-swope-62b48a43', b'https://www.linkedin.com/in/mosseri', b'https://www.linkedin.com/in/paul-grewal-288978b4', b'https://www.linkedin.com/in/roberta-thomson-4619225', b'https://www.linkedin.com/in/crossleyhelen', b'https://www.linkedin.com/in/elizabeth-laraki-9825909', b'https://www.linkedin.com/in/julie-zhuo-35b11322', b'https://www.linkedin.com/in/hansjuergenschmidtke', b'https://www.linkedin.com/in/amy-hayes-07b56126', b'https://www.linkedin.com/in/kunbiadeyemo', b'https://www.linkedin.com/in/alexdeve', b'https://www.linkedin.com/in/reenaphilip', b'https://www.linkedin.com/in/leoolebe', b'https://www.linkedin.com/in/doug-fraser-2bb98a4', b'https://www.linkedin.com/in/amin-zoufonoun-a6a3995', b'https://www.linkedin.com/in/alejandracos', b'https://www.linkedin.com/in/anandc', b'https://www.linkedin.com/in/yann-lecun-0b999', b'https://www.linkedin.com/in/tskhurana', b'https://www.linkedin.com/in/schuyler-milender-0b753622', b'https://www.linkedin.com/in/juan-m-salazar-8341aa13', b'https://www.linkedin.com/in/nirali-bhagdev-9709126', b'https://www.linkedin.com/in/sharonbyang', b'https://www.linkedin.com/in/kristen-clifford-1a658523', b'https://www.linkedin.com/in/brohrer', b'https://www.linkedin.com/in/naomi-gleit-7849aba9', b'https://www.linkedin.com/in/tomalison', b'https://www.linkedin.com/in/heidi-swartz-0842a59', b'https://www.linkedin.com/in/stephen-satterfield-7192b52a', b'https://www.linkedin.com/in/fidjisimo', b'https://www.linkedin.com/in/ragavansrinivasan', b'https://www.linkedin.com/in/noah-gorsky-b1488211', b'https://www.linkedin.com/in/brian-rice-a130a290', b'https://www.linkedin.com/in/ashutoshjhaveri', b'https://www.linkedin.com/in/michael-bailey-a2653521', b'https://www.linkedin.com/in/elisabeth-diana-10524b2', b'https://www.linkedin.com/in/peter-stern-960a5515', b'https://www.linkedin.com/in/katie-crona-1a806a7', b'https://www.linkedin.com/in/laurentalley', b'https://www.linkedin.com/in/cameron-lutz-67ab3a88', b'https://www.linkedin.com/in/alvinbowles', b'https://www.linkedin.com/in/pavel-tekel-63205668', b'https://www.linkedin.com/in/katherinaj', b'https://www.linkedin.com/in/deborahliu', b'https://www.linkedin.com/in/ryan-d-mcgarry-53ab804', b'https://www.linkedin.com/in/robshawsports', b'https://www.linkedin.com/in/davisf', b'https://www.linkedin.com/in/mark-d-arcy-0b526a55', b'https://www.linkedin.com/in/meghanpeters', b'https://www.linkedin.com/in/salowski', b'https://www.linkedin.com/in/johnwhitfield', b'https://www.linkedin.com/in/jie-zheng-643b6163', b'https://www.linkedin.com/in/guyrosen', b'https://www.linkedin.com/in/javierolivan', b'https://www.linkedin.com/in/nicholasraby', b'https://www.linkedin.com/in/huangyi7', b'https://www.linkedin.com/in/urviparekh', b'https://www.linkedin.com/in/maming', b'https://www.linkedin.com/in/osofsky', b'https://www.linkedin.com/in/jeffpark101', b'https://www.linkedin.com/in/michaellevinson', b'https://www.linkedin.com/in/alexandrelebrun', b'https://www.linkedin.com/in/john-hegeman-02137b7', b'https://www.linkedin.com/in/ayushagarwal', b'https://www.linkedin.com/in/codingtmd', b'https://www.linkedin.com/in/robert-hennegan-90a60879', b'https://www.linkedin.com/in/julieahogan', b'https://www.linkedin.com/in/susan-li-08b73033', b'https://www.linkedin.com/in/soumith', b'https://www.linkedin.com/in/danieldanker', b'https://www.linkedin.com/in/breenguyen', b'https://www.linkedin.com/in/dwehner', b'https://www.linkedin.com/in/biganderson', b'https://www.linkedin.com/in/johnanthonyevans', b'https://www.linkedin.com/in/dmarcus', b'https://www.linkedin.com/in/erica-zoromski-3040362', b'https://www.linkedin.com/in/bryanosullivan', b'https://www.linkedin.com/in/ashley-james-a6b20728', b'https://www.linkedin.com/in/rsherman', b'https://www.linkedin.com/in/yoavshapira', b'https://www.linkedin.com/in/natalie-tran-41b0641a', b'https://www.linkedin.com/in/whitneyk', b'https://www.linkedin.com/in/hylawallis', b'https://www.linkedin.com/in/sjanardhan', b'https://www.linkedin.com/in/jennifer-adams-draffen-4913a5', b'https://www.linkedin.com/in/alexorig', b'https://www.linkedin.com/in/louismoynihan', b'https://www.linkedin.com/in/andrea-saul-4b343460', b'https://www.linkedin.com/in/crystal-patterson-38242a4', b'https://www.linkedin.com/in/wenying-hu-a2763520', b'https://www.linkedin.com/in/eva-press-4b8a7547', b'https://www.linkedin.com/in/robert-pepper-8466b830', b'https://www.linkedin.com/in/brianboland', b'https://www.linkedin.com/in/mike-johnson-45638b15', b'https://www.linkedin.com/in/danielconner10', b'https://www.linkedin.com/in/dorislfong', b'https://www.linkedin.com/in/sameerchowdhri', b'https://www.linkedin.com/in/mbenedict', b'https://www.linkedin.com/in/raovj', b'https://www.linkedin.com/in/christopherpbarbour', b'https://www.linkedin.com/in/namnnguyen', b'https://www.linkedin.com/in/mjblanchard', b'https://www.linkedin.com/in/miranda-kalinowski-bb1a0223', b'https://www.linkedin.com/in/alex-himel-6119413', b'https://www.linkedin.com/in/aastha-gupta-3b854115', b'https://www.linkedin.com/in/lyndi-horn-8957aa6', b'https://www.linkedin.com/in/taylorjason', b'https://www.linkedin.com/in/maxine-williams-7697485', b'https://www.linkedin.com/in/bweihl', b'https://www.linkedin.com/in/jtrimiew', b'https://www.linkedin.com/in/nina-d-souza-9501547', b'https://www.linkedin.com/in/gaurav-dosi-52099119', b'https://www.linkedin.com/in/tomalison', b'https://www.linkedin.com/in/jeffreynar', b'https://www.linkedin.com/in/ryanbiega']
#csvFile = open("Facebook url.csv", "w")
#writer = csv.writer(csvFile)
## 写入的内容都是以列表的形式传入函数
#writer.writerow(fileHeader)
#writer.writerow(d1)
#writer.writerow(d1)
company_url=[]
for e in facebook:
    company_url.append(e.decode('utf-8'))
    
#print(facebook_url)
data=open('facebook50resume.csv','w')
fieldnames=['name','educations','experiences']
writer=csv.DictWriter(data,fieldnames=fieldnames)
writer.writeheader()
writer.writeheader()



def get_profiles():
    company_employee={}
    count=0

    for e in company_url:
        
        print('******************************')
        print(e)
        time.sleep(3)
        company_employee[e]=Person(e,driver = diver, scrape=False)
        company_employee[e].scrape(close_on_complete=False)
    #    print(facebook_employee[e])
        if str(company_employee[e].educations) != '[]' and str(company_employee[e].experiences) != '[]':
            writer.writerow({'name':str(company_employee[e].name),'educations':str(company_employee[e].educations),
                           'experiences':str(company_employee[e].experiences)})
            time.sleep(1)
            print(company_employee[e].educations)
            
            print(company_employee[e].experiences)
            
            count+=1
        if count==50:
            break




get_profiles()




#person=Person('https://www.linkedin.com/in/fvarela',driver = diver, scrape=True) 
#print(person.name)




