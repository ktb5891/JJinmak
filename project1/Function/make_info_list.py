# 라이브러리 추가
import requests
from urllib.parse import urlparse

# 검색값과 검색주소를 가져와서 카카오 map url에 접속하여 위도 경도를 불러올 함수
def make_info_list(title,address):
    # 카카오 map의 url에 접속하여 주소 검색
    url = "https://dapi.kakao.com/v2/local/search/address.json?&query=" + address
    # 검색 결과를 result에 저장을 하고 json 포멧으로 변환
    result = requests.get(urlparse(url).geturl(), headers={"Authorization":"----------------------------------------------------"})
    print(result)
    json_obj = result.json()
    print(json_obj)
    # 검색 결과 정렬
    # 검색 결과를 저장 할 빈 리스트를 만들어 놓는다.
    list = []

    # 제이슨 포멧에 정리되어있는 주소와 위도, 경도를 list에 저장
    for document in json_obj['documents']:
        val = [title, document['address_name'], float(document['y']), float(document['x'])]
        list.append(val)
    return list

# 위에서 만들어진 리스트를 이용하여 위도, 경도 값만 리턴하는 함수
def find_xy(list):
    x = list[0][3]
    y = list[0][2]
    return x,y

# 활용 예시
if __name__ == '__main__':
    address="서울특별시 강남구 테헤란로 212"
    temp_list = make_info_list("멀티캠퍼스 역삼",address)
    print(temp_list,"테에에에엥엠프리스트")

    x,y = find_xy(temp_list)
    print("멀티캠퍼스역삼의 위도는 ",y," 경도는 ",x," 이다.")
    # 위도는  37.5012767241426  경도는  127.039600248343  이다.
