import requests
from bs4 import BeautifulSoup
from getLowArrInfoByStdIdList import getLastTm_By_station
from timeCalculator import cal
from find_route import find_all_of_route

def sol(total_route_list):
    temp=0
    for i in total_route_list:
        if "startTime" in i.keys():
            if int(i["startTime"])>=temp:
                # print(i)
                # print(i["startTime"])
                temp=int(i["startTime"])
                ans=i
    print(ans)
    return ans

if __name__ == '__main__':
    start_x = 127.03960274144
    start_y = 37.5012863640697
    end_x = 126.953047253148
    end_y = 37.5948548185391
    total_route_list, stations_from_start, stations_from_end = find_all_of_route(start_x, start_y, end_x, end_y)
    ans = sol(total_route_list)