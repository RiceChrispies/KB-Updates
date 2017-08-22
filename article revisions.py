import bs4 as bs
import urllib.request
import fileinput
from simple_salesforce import salesforce
#Issues calling this, but need to table this for now.

sf-Salesforce(username='***', password='***', security_token='***')

source = urllib.request.urlopen('https://eu1.salesforce.com/kA5D00000004MIb').read()
soup = bs.BeautifulSoup(source,'lxml')

#article_block = soup.find(name="table", attrs={"class": "overlayListTable versionOverlayList"})

print (soup) #print the soup

#filename = "articleRevision.csv"
#f = open(filename, "w")

#all_revisions = article_block.find(name="tr")

#f.write(article_block + '\n')



#Added a line here for testing
