import requests
from bs4 import BeautifulSoup


def getLastTm_By_station(stdId,search_Bus):
    serviceKey_list=[
        "----------------------------------------------------",
        "----------------------------------------------------",
        "----------------------------------------------------"

    ]
    serviceKey = serviceKey_list[1]
    url="http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?serviceKey="+serviceKey+"&stId="+str(stdId)+"&"
    req = requests.get(url)
    print(req)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    itemlist = soup.select("itemlist")
    print(soup)
    if itemlist:
        for i in itemlist:
            BusNm = i.select("rtnm")[0].text
            if search_Bus == BusNm:
                lastTm=i.select("lastTm")[0].text[-6:-2]
                return lastTm
    return "1200"


if __name__ == '__main__':
    stdId=105000488
    search_Bus="720"
    lastTm = getLastTm_By_station(stdId, search_Bus)
    print(lastTm)
