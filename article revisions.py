import bs4 as bs
import urllib.request
import fileinput
from simple_salesforce import Salesforce
import requests
# https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module
session = requests.Session()
sf = Salesforce(instance='***', username='***', password='***', security_token='***')

#session_id, instance = SalesforceLogin(
#    username='***',
#    password='***',
#    security_token='***',
#    sandbox=False)

source = urllib.request.urlopen('https://eu1.salesforce.com/kA5D00000004MIb').read()
soup = bs.BeautifulSoup(source,'lxml')

#article_block = soup.find(name="table", attrs={"class": "overlayListTable versionOverlayList"})

print (soup) #print the soup

#filename = "articleRevision.csv"
#f = open(filename, "w")

#all_revisions = article_block.find(name="tr")

#f.write(article_block + '\n')



#Added a line here for testing
