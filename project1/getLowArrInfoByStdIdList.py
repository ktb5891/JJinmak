import requests
from bs4 import BeautifulSoup


def getLastTm_By_station(stdId,search_Bus):
    serviceKey_list=[
        "891h1XE5tlr8DWq1zPhPbyJQVZTbdU4b90ZLnIk9KLXSpk%2Bz9PKQB5PeoVGKlxd%2BARmP%2FRJM%2B4Ry6CV71XYvng%3D%3D",
        "jqFn5RYKJTSM3Q%2FP7bw44SIu5eQ8%2FOp8bzzmVuVs0FjVkGWUYblKkIeMpbxXsOropCS%2B4ETKE0F0%2F6zR8BvPEw%3D%3D",
        "PLLx23%2Beq0f7G2OdoALWYv1GrgOu%2B25clMxxWSInwiNssM7ennJ%2BY1KN6J%2F6osvdnDt6IADhSfBRcqMR0YmLog%3D%3D"

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