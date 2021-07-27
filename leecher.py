import os
from search_engines import Google
from search_engines import Bing
import requests
import re
from colorama import Fore,Back,Style
import sys
#=============================================
#engine = Google()
#results = engine.search("my query")
#links = results.links()
#=============================================
global Proxylist
global proxyNum
global threadNum
global ComboList
global KwdNum

print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
print('Hi Here is leecher Bing are search sources')
print('We will updata the Goole search Pls wait xD')
print('Our website http://leecher.cnix.plus')
print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

def getLink3(kwdList,page):
    engine = Bing()
    textData = ''
    for i in range(len(kwdList)):   
        KwdNum = i
        results = engine.search(kwdList[i]+' site:api.throwbin.io',pages=page)
        links = results.links()
        for temp in links:
            textData += temp+'\n'
    return textData

def getLink(kwdList,page):
    engine = Bing()
    textData = ''
    for i in range(len(kwdList)):   
        KwdNum = i
        results = engine.search(kwdList[i]+' site:pastebin.com',pages=page)
        links = results.links()
        for temp in links:
            if 'https://pastebin.com/' in temp:
                temp2 = re.findall(r'https://pastebin.com/(\S*)',temp)[0]
                temp3 = 'https://pastebin.com/raw/'+temp2
                textData += temp3+'\n'
    return textData

def readLink(LinkList,patten,mode):
    textData = ''
    textData2 = ''
    temp2 = []
    for link in range(len(LinkList)):
        try:
            req = requests.get(LinkList[link]).text
            combos = re.findall(patten,req) 
            for combo in combos:
                textData += combo+'\n'
            textDataList = textData.split('\n')
            temp2 = list(set(textDataList))
            
        except:
            pass
    print('Leecher Done')
    return textData
if __name__ == '__main__':
    results =  getLink(kwdList=sys.argv[1],page=2)
    ComboList =  readLink(results.split('\n'),r'([a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}:[a-zA-Z0-9_\-\.]+)',1)
    print('saving combo.......')
    file = open('combo.txt','w');
    file.write(str(ComboList));
    file.close();