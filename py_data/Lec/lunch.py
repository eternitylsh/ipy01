import requests as req
from bs4 import BeautifulSoup as bfs

import sys

class Lunch:
    def __init__(self):
        self.web = req.get('https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do')
        self.soup = bfs(self.web.content, 'html5lib')

    def GetLunch(self, __date):
        day = self.soup.select(".menu-tbl .day")
        date = self.soup.select(".menu-tbl .date")
        wons = self.soup.select("h3.menu-tit01")
        menus = self.soup.select("h3.menu-tit01+p")

        tddidx = [ i for i, d in enumerate(day) if __date == d.text ][0]

        print('-' * 18)
        print( day[tddidx].text, date[tddidx].text, wons[tddidx].text )
        print('-' * 18)
        print(menus[tddidx].text)
        print('-' * 18)
        print('\n'*3)



if "__main__" == __name__:
    _date = sys.argv[1]
    l = Lunch()
    l.GetLunch(_date)

