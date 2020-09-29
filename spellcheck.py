#!/usr/bin/env python3

import logging, requests, re
from time import sleep
import sys, getopt
from autocorrect import Speller
try:
	from BeautifulSoup import BeautifulSoup
except ImportError:
	from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
url = 'URL'
headers = {'User-Agent': ua.random}
spell = Speller(lang='en')
reservedwords = ['Us', 'Insights', 'Blackbox', 'AS400', 'App', 'Cloud', 'Fintech', 'CRM', 'ERP', 'Webinars', 'AI-driven', 'AI', 'Awards', 'RPA', 'COBOL', 'GDPR', 'ROI', 'RPG', 'Java', 'Python', 'https://www.pivotcloudsolutions.com/wp-content/uploads/2020/09/pivotcloud-intro-home.mp4', 'IBMi,', 'Insurtech', 'PCS', 'blackbox', 'backend', 'KPI', 'SaaS', 'JDE.', 'BlackBox', 'KPIs', 'RPA.', '‘BlackBox’', 'cyber', 'DevOps', 'CIO', 'Facebook', 'AS400/IBMi', 'FinTech', 'RPG,', 'MQ.', 'JD', 'Netapps.', 'reuters.com', 'BMS)', 'MQ).', '(BQL).', 'BQL,', 'IBMi', 'JDEdwards', 'MQ/middleware).', 'RPGL,', 'MQ,', 'backend,', 'URLs', 'RFID.', 'XAI', 'dependecy', 'NetSuite', 'NSW', 'Astra', '2NX', 'info@astra-global.com', 'SSO', 'CRM/ERP/Build', 'PCs', 'SpaceX', 'SpaceX’s', 'newsfeed', 'Microsoft', 'McKinsey', 'GDPR.', 'Wipro', 'Lidl', 'CFOs', 'Sribar,', 'Gartner', '#CIO', 'Webinar', 'webinar', 'Prasad', 'Cyber', 'Jacinta', 'Mandyam', 'CMO', 'Ravi', 'Chelle', 'Flexpod.', 'FMCG,', 'Prakash', 'Pithani', 'ERP,', 'FlexPOD', 'Warwick', 'IIT', 'Geert', 'deBelt', '(GDPR).', 'IP', '(“DPA”)', 'DPA,', 'fintech', 'Walmart', '(BQL)', 'CIOs)', 'Golang)', 'MVC', '(RPA).', 'signup', 'MQ', 'SQL', 'BQL', 'Jiddu', 'Micor-Service', 'booot,', 'URIs', 'URL', 'MySQL', 'Oralce', 'MSSQL', 'PgSQL', 'NoSQL', '(Mongodb,', 'CouchDB', 'Customerdb', 'VMS', 'SSID(Optional)', 'Golang,', 'enviroments', 'OpenID,', 'SAML', 'OAuth', 'Automation(RPA)', '(RPA)', 'RPA,', '(BQL),', 'RPA’', 'RPAs', 'RPAs,', 'rpa', 'CSV', 'csv', 'GitHub)', 'JSON', '(JDBC,', 'ODBC,', 'URL,', 'Keycloak', 'OpenID', 'FreeOTP', '(SOA)', '(MFC),', 'CTOs', 'https://pivotcloudsolutions.com/', 'SME', 'https://pivotcloudsolutions.com', 'Prasad,', 'Justin', 'Novello', 'Unsplash.com', 'Elon', 'SpaceX,', 'CxOs', 'https://www.pivotcloudsolutions.com/demo-co', 'ntact-form/', 'https://www.pivotcloudsolutions.com', 'IoT', 'work-arounds', '(https://simplicable.com/new/legacy-systems)', 'Döderlein,', 'Auka).', '(https://www.altexsoft.com/whitepapers/legacy-system-modernization-how-to-transform-the-enterprise-for-digital-future/)', 'Forrester', 'Cryan', 'Analythics', 'BigData', '(https://pivotcloudsolutions.com)', 'chatbots', 'Api-driven', 'Jacinta,']

url_list = []

def clean_me(soup):
    for s in soup(['script', 'style']):
        s.decompose()
    return ' '.join(soup.stripped_strings)

def searchpage(page):
    print ("Checking page : " + page);
    sleep(0.5)
    website = requests.get(page, headers=headers)
    html = website.text
    soup = BeautifulSoup(html, "html.parser")
	
    spellcheck(clean_me(soup))
    for a in soup.find_all('a'):
        nurl = a['href']
        try:
            if nurl not in url_list and not nurl.endswith("mp4"):
                url_list.append(nurl)
                if nurl.startswith('/') or nurl.startswith('#'):
                    searchpage(url + nurl)
                elif nurl.startswith(url):
                    searchpage(nurl)
        except:
            pass

def spellcheck(text):
    words = text.split()
    for word in words:
        if word.lower() != spell(word.lower()) and word not in reservedwords:
            print(word)

def main(argv):
   url = ''
   try:
      opts, args = getopt.getopt(argv,"hu:",["url="])
   except getopt.GetoptError:
      print 'spellcheck.py -u <https://webiste.com>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'spellcheck.py -u <https://webiste.com>'
         sys.exit()
      elif opt in ("-u", "--url"):
         url = arg
   searchpage(url)
   
if __name__ == "__main__":
   main(sys.argv[1:])
   
