import requests as req
from bs4 import BeautifulSoup as bfs

import sys

class BexcoEvent:
    def __init__(self, __vpage=1):
        self.web = req.get(f'https://www.bexco.co.kr/kor/CMS/EventScheduleMgr/list.do?robot=Y&mCode=MN214&page={__vpage}')
        self.soup = bfs(self.web.content, 'html.parser')

    def turnpage(self, __vpage=1):
        self.web = req.get(f'https://www.bexco.co.kr/kor/CMS/EventScheduleMgr/list.do?robot=Y&mCode=MN214&page={__vpage}')
        self.soup = bfs(self.web.content, 'html.parser')
        self.EventListPrint()

    def EventListPrint(self):
        ebox = self.soup.select(".txtBox")
        etitles = self.soup.select(".txtBox .subject")
        edates = self.soup.select(".txtBox .date")
        eplaces = self.soup.select(".txtBox .place")
        
        print("BEXCO 전시 일정")
        print("="*18)
        print("\n")
        
        for et, ed, ep in zip( etitles, edates, eplaces ):
            print("="*18)
            print(et.text)
            print(list(ed.text.strip().replace('\t', '').replace('\r', '').replace('\n', '').split('\~')))
            print(ep.text)
            print("="*18)
            print("\n"*3)

if "__main__" == __name__:
    _page = int(sys.argv[1])
    l = BexcoEvent(_page)
    l.EventListPrint()

