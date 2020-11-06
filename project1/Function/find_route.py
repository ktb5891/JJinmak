import requests
from bs4 import BeautifulSoup
from getLowArrInfoByStdIdList import getLastTm_By_station
from timeCalculator import cal
from getLastTm_subway import getLastTm_subway

def find_all_of_route(start_x,start_y,end_x,end_y):
      serviceKey_list = [
            "----------------------------------------------------",
            "----------------------------------------------------",
            "----------------------------------------------------",
            "----------------------------------------------------"]
      serviceKey = serviceKey_list[0]
      url = "http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoByBusNSub?serviceKey="+ serviceKey + \
            "&startX=" + str(start_x) + "&startY=" + str(start_y) + "&endX=" + str(end_x) + "&endY=" + str(end_y) + "&"
      req = requests.get(url)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser')
      itemlist=soup.select("itemlist")
      stations_from_start = set()
      stations_from_end = set()
      total_route_list=[]
      for item in itemlist:
            total_route_dict = {}
            time = int(item.find("time").text)
            station = item.select('pathlist')
            start_list = []
            end_list = []
            trans_list = []
            trans_type = []
            for i in station:
                  # print("1")
                  station_start = i.select("fname")[0].text
                  station_end = i.select("tname")[0].text
                  public_trans = i.select('routenm')[0].text
                  IsSubway = i.select("raillinklist")
                  if IsSubway:
                        trans_type.append("subway")
                        howmanysubway=len(IsSubway)
                  else:
                        trans_type.append("bus")
                  start_list.append(station_start)
                  end_list.append(station_end)
                  trans_list.append(public_trans)
                  last_start_station_ID = i.select('fid')[0].text
                  last_station_ID = i.select('tid')[0].text
            total_route_dict['stations_from_start'] = start_list
            total_route_dict['stations_from_end'] = end_list
            total_route_dict['Trans_list'] = trans_list
            total_route_dict['Trans_type'] = trans_type
            total_route_dict["Travel_time"] = time
            total_route_list.append(total_route_dict)
            stations_from_start.add(start_list[0])
            stations_from_end.add(end_list[-1])

            if total_route_dict['Trans_type'][-1]=="bus":
                  lastTm=getLastTm_By_station(last_station_ID,total_route_dict['Trans_list'][-1])
                  print(lastTm)
                  startTime=cal(lastTm,total_route_dict['Travel_time'])
            else:
                  try:
                        lastTm = getLastTm_subway(total_route_dict["Trans_list"][-1],total_route_dict["stations_from_end"][-1])
                        lastTm = str(lastTm)
                        startTime = cal(lastTm, total_route_dict['Travel_time'])

                  except:
                        pass
            if lastTm[:2]=="00":
                  lastTm = "24" + lastTm[2:]
            total_route_dict["lastTm"] = lastTm
            total_route_dict["startTime"] = startTime

      stations_from_start = list(stations_from_start)
      stations_from_end= list(stations_from_end)
      if total_route_list:
            return  total_route_list, stations_from_start, stations_from_end
      # total_route_list는 {출발 정류장:[], 도착 정류장:[], 교통수단:[], 교통수단 종류:[], 막차시간}들 모음 - 구조 리스트
      # stations_from_start는 출발지에서 가까운 정류장들 모음 - 구조 세트
      # stations_from_end는 도착지에서 가까운 정류장들 모음 - 구조 세트

if __name__ == '__main__':
      start_x = 127.03960274144
      start_y = 37.5012863640697
      end_x = 126.953047253148
      end_y = 37.5948548185391
      total_route_list, stations_from_start, stations_from_end = find_all_of_route(start_x, start_y, end_x, end_y)
      for _ in total_route_list:
            print(_)
      print(stations_from_start)
      print(stations_from_end)
