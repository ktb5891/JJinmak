from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def station_info(center):
    url = "https://map.naver.com/v5/search/"+center
    driver = webdriver.Chrome("chromedriver.exe")
    # 1600,1150
    driver.set_window_size(1000,550)
    driver.get(url)

    busStations=[]
    subwayStations=[]
    # 검색창을 켜기 위하여 검색 버튼을 클릭
    time.sleep(3)
    driver.implicitly_wait(10)
    click_search = driver.find_element_by_xpath('//*[@id="sidebar"]/navbar/perfect-scrollbar/div/div[1]/div/ul/li[2]/a')
    driver.execute_script("arguments[0].click();", click_search)

    time.sleep(2)

    public_btn = driver.find_element_by_xpath("//*[@id='container']/div[1]/shrinkable-layout/search-layout/search-box/div/div[2]/around-here-card/ul/li[4]/a/span[1]")
    driver.execute_script("arguments[0].click();", public_btn)
    driver.implicitly_wait(10)

    time.sleep(2)

    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')

    link_search = soup.findAll("div", {"class": "link_search"})
    for i in link_search:
        # title=i.findAll("strong")
        # print(i.find("strong").text)
        # info=i.findAll("span")
        # for aa in info:
        #     print(aa.text)
        temp_bus = list(i.strings)
        title = temp_bus[1]
        code = temp_bus[2][:6]
        goto = temp_bus[2][8:-1]
        busStation=[title, code, goto]
        busStations.append(busStation)


    metro_btn = driver.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/around-here-layout/around-here-home/div/div[1]/ul/li[2]/button')
    driver.execute_script("arguments[0].click();", metro_btn)
    driver.implicitly_wait(10)

    time.sleep(2)


    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')

    link_search = soup.findAll("div", {"class": "link_search"})
    for i in link_search:
        # title=i.findAll("strong")
        # print(i.find("strong").text)
        # info=i.findAll("span")
        # for aa in info:
        #     print(aa.text)
        temp_aubway = list(i.strings)

        title=temp_aubway[1]
        address=temp_aubway[4]
        temp = address.split()
        sido=temp[0]
        gungu= temp[1]
        doro = temp[2] + temp[3]
        subwayStation=[title, address, sido, gungu, doro]
        subwayStations.append(subwayStation)
    busStations.sort()
    subwayStations.sort()
    return busStations,subwayStations

if __name__ == '__main__':
    center=str(input())
    busStations,subwayStations = station_info(center)
    print("----------버스정류소----------")
    for _ in busStations:
        print(_)
    print("----------지하철역----------")
    for _ in subwayStations:
        print(_)
