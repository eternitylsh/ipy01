import requests as req
from bs4 import BeautifulSoup as bfs
import pyshorteners as ps

class WCrolling:
    def __init__(self, scons):
        self.sconstr = self.getConstr(scons)
        self.url = f"https://work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?moreCon=more&enterPriseGbn=all&srcKeyword={self.sconstr}&careerTypes=N&pageIndex={1}"
        web = req.get(self.url)
        soup = bfs(web.content, 'html.parser')
        self.max_page = int(soup.select(".paging_direct")[0].text.strip()[2])

    def ViewSearchPage(self, __page):

        if 0 > __page or self.max_page < __page: 
            print(f"Out of range index page... ; {__page}")
            return -1
    
        web = req.get(self.url)
        soup = bfs(web.content, 'html.parser')
        
        sh = ps.Shortener()

        componys = soup.select("tr td.a-l .cp_name")
        worktitles = soup.select("tr .cp-info-in>a")

        for i, ( compony, worktitle ) in enumerate( zip(componys, worktitles) ):
            print( f"{i + 1} : {worktitle.text.strip()} \n {sh.tinyurl.short('https://work.go.kr/' + worktitle.attrs['href'])}" )

    def ChangePage(self, __page):
        self.url = f"https://work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?moreCon=more&enterPriseGbn=all&srcKeyword={self.sconstr}&careerTypes=N&pageIndex={__page}"
        self.ViewSearchPage(__page)

    def ChangeSearchCondition(self, scons):
        tpage = int(self.url[-1])
        self.sconstr = self.getConstr(scons)
        self.url = f"https://work.go.kr/empInfo/empInfoSrch/list/dtlEmpSrchList.do?moreCon=more&enterPriseGbn=all&srcKeyword={self.sconstr}&careerTypes=N&pageIndex={tpage}"
        self.ViewSearchPage(tpage)

    def getConstr(self, scons):
        cstr = ""

        for i, scon in enumerate(scons):
            cstr += f"{scon}"

            if not len(scons) - 1 == i:
                cstr += "+%7C+"
        
        return cstr

