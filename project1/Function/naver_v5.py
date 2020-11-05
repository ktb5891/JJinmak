from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


def find_candidate(search):
    url = "https://m.map.naver.com/#/search"
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)

    driver.implicitly_wait(2)

    search_input = driver.find_element_by_xpath("//*[@id='ct']/div[1]/div[1]/form/div/div[2]/div/span[1]/input")
    search_input.send_keys(search)
    search_input.send_keys(Keys.ENTER)

    try:
        search_input.send_keys(Keys.ENTER)
        Alert(driver).dismiss()
    except:
        pass

    candidate_dict = {}
    title_list=[]

    search_list = driver.find_elements_by_class_name("item_info")

    for i in search_list:
        title= i.find_element_by_css_selector("div > strong").text
        looking_addr = i.find_element_by_css_selector("div.item_info_inn > div > a").text
        temp_list=list(looking_addr)[5:]
        address =""
        for _ in temp_list:
            address+=_
        title_list.append(title)

        addr_list = address.split()
        sido = addr_list[0]
        gungu = addr_list[1]

        if len(addr_list) > 3:
            doro = addr_list[2] + addr_list[3]
            candidate_dict[title] = [address, sido, gungu, doro]
        elif len(addr_list) > 2:
            dong = addr_list[2]
            candidate_dict[title] = [address, sido, gungu, dong]
        else:
            candidate_dict[title] = [address, sido, gungu, '']

    return candidate_dict,title_list

# 활용 예시
if __name__ == '__main__':
    candidate_dict ={}
    search=str(input("출발/도착지를 검색해주세요 : "))
    candidate_dict,title_list = find_candidate(search)
    while len(candidate_dict) == 0:
        search = str(input("검색 결과가 없습니다. 다시 입력하여 주세요 :"))
        candidate_dict = find_candidate(search)
    for key,value in candidate_dict.items():
        print(key,'\n',value)
        print("-"*50)
    print("검색 딕셔너리 완성!")