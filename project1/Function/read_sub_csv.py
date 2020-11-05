import csv

dict={}
f = open('SubwayStationInfo.csv', 'r', encoding='cp949')
rdr = csv.reader(f)
for line in rdr:
    if line[2] in dict.keys():
        dict[line[2]].append({line[1]:line[3]})
    else:
        dict[line[2]]=[{line[1]:line[3]}]
f.close()

def getStationCode(lineNm,stationName):
    for i in dict[lineNm]:
        for _ in range(len(stationName)):
            # print(stationName[:_])
            if stationName[:_] in i.keys():
                code = i[stationName[:_]]
                return code
# lineNm = 호선 입력
# stationName = 역이름


# if __name__ == '__main__':
#     getStationCode("1호선", "청량리(지상)역")

# for i in dict["공항철도"]:
#     stationName="홍대입구역"
#     for _ in range(len(stationName)):
#         # print(stationName[:_])
#         if stationName[:_] in i.keys():
#             code = i[stationName[:_]]
#             print(code)
