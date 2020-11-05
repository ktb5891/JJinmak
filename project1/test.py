from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import time



search="서초래미안"
# url = "https://map.naver.com/v5/search/"+search  # 네이버 지도 앱의 구 주소인 v4.map.naver.com를 url로 가지고 온다.
url = "https://m.map.naver.com/search2/search.nhn?query="+search
response= requests.get(url)
html = response.content
soup = BeautifulSoup(html,"html.parser")
# print(soup)
script = soup.findAll("script",{"type":"text/javascript"})
print(len(script))
print(script[len(script)-1])


#######################################################
# driver = webdriver.Chrome("chromedriver.exe")
# driver.get(url)
#
# time.sleep(10)
#
#
# IsAddress = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[1]/combined-search-list/fusion-search-list/fusion-address-list/div/fusion-address-item/div/div/div/div[1]')
# print(IsAddress.text)
#
#
# IsDong = driver.find_element_by_xpath('//*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-address/div/div[2]/div/div[1]/div[1]/div/strong')
# print(IsDong.text)

##################################################
# # 신림동 572-1 검색
# //*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[1]/combined-search-list/fusion-search-list/fusion-address-list/div/fusion-address-item/div/div/div/div[1]
# 모바일
# //*[@id="ct"]/div[2]/ul/li/div[1]

#
# # 관악구 신림동 검색
# //*[@id="container"]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-address/div/div[2]/div/div[1]/div[1]/div/strong
# 모바일
# //*[@id="ct"]/div[2]/div[1]/strong

# # 서초래미안 검색
# //*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/div[1]/a/span[1]
# //*[@id="_pcmap_list_scroll_container"]/ul/li[2]/div[1]/div[1]/a/span[1]
# 모바일
# //*[@id="ct"]/div[2]/ul/li[1]/div[1]

# # 장소의 이름을 저장할 후보 딕셔너리 생성
# candidate_list=[]
#
# # 구 주소에 접근하게 되면 처음에 뜨는 팝업창 닫기
# close_popup = driver.find_element_by_xpath('//*[@id="dday_popup"]/div[2]/button')
# driver.execute_script("arguments[0].click();", close_popup)
#
# # 검색창 찾아 검색어 입력
# driver.find_element_by_id("search-input").send_keys(search)
# # 검색 버튼 클릭
# search_bnt = driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button')
# driver.execute_script("arguments[0].click();", search_bnt)
#
# # 컴퓨터 내에서는 기다릴 필요가 없었으나 인터넷 상태가 좋지 않을 것을 고려하여 작성
# driver.implicitly_wait(2)

# # lsnx_det라는 클래스를 가진 요소들을 search_list 에 저장
# # 해당 클래스에는 이름 및 주소 등의 정보가 들어있음
# search_list = driver.find_elements_by_class_name("lsnx_det")
# for search_result in search_list:
#     # 요소들 전부를 살피며 이름은 title, 전체 주소는 address에 저장
#     candidate_dict = {}
#     title = search_result.find_element_by_css_selector('dt>a').text
#     address = search_result.find_element_by_css_selector('.addr').text
#
#     # 이후 몇몇 주소 값의 뒤에 지번 버튼이 같이 크롤링 됬음을 알아채고 지번 버튼을 지워주는 작업을 진행
#     if address[-3:] == " 지번":
#         address = address[:-3]
#     candidate_dict["title"] = title
#     candidate_dict["address"] = address
#     # 전체 주소를 시도, 군구, 도로명|동|''으로 분리하여 딕셔너에 넣는 작업
#     addr_list=address.split()
#     sido=addr_list[0]
#     gungu=addr_list[1]
#     candidate_dict["sido"] = sido
#     candidate_dict["gungu"] = gungu
#
#     if len(addr_list) > 3:
#         doro = addr_list[2] + addr_list[3]
#         candidate_dict["doro"] = doro
#     elif len(addr_list) > 2:
#         doro = addr_list[2]
#         candidate_dict["doro"] = doro
#     else:
#         doro=' '
#         candidate_dict["doro"] = doro
#     candidate_list.append(candidate_dict)
