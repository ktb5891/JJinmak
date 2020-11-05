import sys
read= sys.stdin.readline
from make_candidate_list import find_candidate
from make_info_list import make_info_list,find_xy

def find_spot(candidate_dict):
    # make_info_list함수를 이용하여 info_list와 위치의 위도 경도를 가지고 온다
    info_list=make_info_list(candidate_dict["title"],candidate_dict["address"])
    x,y = find_xy(info_list)
    return x,y


# 사용 예시
if __name__ == '__main__':
    candidate_list=find_candidate("에코메트로 7단지")
    try:
        for candidate_dict in candidate_list:
            start_x,start_y=find_spot(candidate_dict)
            start_point=candidate_dict["title"]
            print(start_point,"의 위도 값 : ",start_y," 경도 값 : ",start_x)
    except:
        pass