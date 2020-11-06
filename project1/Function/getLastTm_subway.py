from bs4 import BeautifulSoup
import requests
from read_sub_csv import getStationCode


def getLastTm_subway(lineNm,stationName):
    stationCode = getStationCode(lineNm,stationName)
    serviceKey = "----------------------------------------------------"
    lastTm_dict={}
    for updown_index in range(1,3):
        url ="http://openapi.seoul.go.kr:8088/"+ serviceKey +"/xml/SearchLastTrainTimeByFRCodeService/1/10/"+ stationCode +"/1/"+str(updown_index)+"/"
        response= requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
        rows = soup.findAll("row")
        for row in rows:
            subwayename=row.find('subwayename').text
            if subwayename not in lastTm_dict.keys():
                temp_leftTime= row.find('lefttime').text
                leftTime=temp_leftTime[:2]+temp_leftTime[3:5]
                lastTm_dict[subwayename]=leftTime

    temp=9999
    for key,value in lastTm_dict.items():
        if int(value)<temp:
            temp=int(value)
    return str(temp)

if __name__ == '__main__':
    lastTm = getLastTm_subway('1호선','청량리역')
    print(lastTm)
