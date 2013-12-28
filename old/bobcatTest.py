import urllib
import urllib2
from bs4 import BeautifulSoup

#req = urllib2.Request(urllib.quote_plus('http://bobcat.library.nyu.edu/primo_library/libweb/action/search.do?dscnt=0&vl(378633853UI1)=all_items&scp.scps=scope:(NS),scope:(CU),scope:("BHS"),scope:(NYU),scope:("NYSID"),scope:("NYHS"),scope:(GEN),scope:("NYUAD")&frbg=&tab=all&dstmp=1386438633283&srt=rank&ct=search&mode=Basic&dum=true&vl(212921975UI0)=any&indx=1&vl(1UIStartWith0)=contains&vl(freeText0)=genomics&vid=NYU&fn=search'))

#params = { 'dscnt': '0', 'vl(378633853UI1)' : 'all_items', 'scp.scps' : 'scope:(NS),scope:(CU),scope:("BHS"),scope:(NYU),scope:("NYSID"),scope:("NYHS"),scope:(GEN),scope:("NYUAD")', 'frbg' : '', 'tab' : 'all', 'dstmp' = '1386438633283', 'srt' : 'rank', 'ct' = 'search', 'mode' : 'Basic', 'dum' : 'true', 'vl(212921975UI0)' : 'any', 'indx' : '1', 'vl(1UIStartWith0)' : 'contains', 'vl(freeText0)' : 'genomics', 'vid' : 'NYU', 'fn' : 'search' }
#paramStr = urllib.urlencode(params)

#Start at just aleph.library.nyu.edu

req1 = urllib2.Request("http://aleph.library.nyu.edu")
#then pull out <!-- filename: short-a-body--> to </tr>
#actually first <td> with details in there
resp1 = urllib2.urlopen(req1)
content1 = resp1.read()
soup1 = BeautifulSoup(content1)

print soup1

'''
nextUrl1 = soup1.find(id="short-a").find("form")["action"]


print nextUrl1


req2 = urllib2.Request(nextUrl1)
resp2 = urllib2.urlopen(req2)
content2 = resp2.read()
soup2 = BeautifulSoup(content2)


nextUrl2 = soup2.find(id="nav1search").find("a")["href"]

print nextUrl2

print soup2



#print nextUrl2


#print soup2
'''