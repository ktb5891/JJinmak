from selenium import webdriver
import json

def find_candidate(search):
    url = "https://v4.map.naver.com/"  # 네이버 지도 앱의 구 주소인 v4.map.naver.com를 url로 가지고 온다.
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)

    # 장소의 이름을 저장할 후보 딕셔너리 생성
    candidate_list=[]

    # 구 주소에 접근하게 되면 처음에 뜨는 팝업창 닫기
    close_popup = driver.find_element_by_xpath('//*[@id="dday_popup"]/div[2]/button')
    driver.execute_script("arguments[0].click();", close_popup)

    # 검색창 찾아 검색어 입력
    driver.find_element_by_id("search-input").send_keys(search)
    # 검색 버튼 클릭
    search_bnt = driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button')
    driver.execute_script("arguments[0].click();", search_bnt)

    # 컴퓨터 내에서는 기다릴 필요가 없었으나 인터넷 상태가 좋지 않을 것을 고려하여 작성
    driver.implicitly_wait(2)

    # lsnx_det라는 클래스를 가진 요소들을 search_list 에 저장
    # 해당 클래스에는 이름 및 주소 등의 정보가 들어있음

    # isAdress = driver.find_elements_by_class_name("lsnx_det")
    # isAdress = driver.find_elements_by_css_selector('#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > ul > li > div.lanx')
    # print(isAdress,"ㅏㄴ어류ㅏㄴ어ㅠㅏ머ㅠㅇㄹ마ㅣ뉴ㅓ")

    search_list = driver.find_elements_by_class_name("lsnx_det")
    if search_list:
        for search_result in search_list:
            # 요소들 전부를 살피며 이름은 title, 전체 주소는 address에 저장
            candidate_dict = {}
            title = search_result.find_element_by_css_selector('dt>a').text
            address = search_result.find_element_by_css_selector('.addr').text

            # 이후 몇몇 주소 값의 뒤에 지번 버튼이 같이 크롤링 됬음을 알아채고 지번 버튼을 지워주는 작업을 진행
            if address[-3:] == " 지번":
                address = address[:-3]
            candidate_dict["title"] = title
            candidate_dict["address"] = address
            # 전체 주소를 시도, 군구, 도로명|동|''으로 분리하여 딕셔너에 넣는 작업
            addr_list=address.split()
            sido=addr_list[0]
            gungu=addr_list[1]
            candidate_dict["sido"] = sido
            candidate_dict["gungu"] = gungu

            if len(addr_list) > 3:
                doro = addr_list[2] + addr_list[3]
                candidate_dict["doro"] = doro
            elif len(addr_list) > 2:
                doro = addr_list[2]
                candidate_dict["doro"] = doro
            else:
                doro=' '
                candidate_dict["doro"] = doro
            candidate_list.append(candidate_dict)
        return candidate_list
    else:
        candidate_dict = {}
        Addr_search_list = driver.find_elements_by_xpath('// *[ @ id = "panel"] / div[2] / div[1] / div[2] / div[2] / ul / li / div[1]')
        title_xpath=driver.find_elements_by_xpath('// *[ @ id = "panel"] / div[2] / div[1] / div[2] / div[2] / ul / li / div[1] / div[2] / a[1]')
        title = title_xpath[0].text
        temp_title_list = title.split()
        addr_list=driver.find_elements_by_xpath('//*[@id="panel"]/div[2]/div[1]/div[2]/div[2]/ul/li/div[1]/div[3]/div/a')
        sido = temp_title_list[0]
        gungu = temp_title_list[1]
        doro = addr_list[0].text
        address = sido + ' ' + gungu + ' ' + doro
        candidate_dict['title'] = title
        candidate_dict['address'] = address
        candidate_dict['sido'] = sido
        candidate_dict['gungu'] = gungu
        candidate_dict['doro'] = doro
        candidate_list.append(candidate_dict)
        return candidate_list
    # 후보 딕셔너리 구조 -> { 후보 이름 : 전체주소, 시도, 군구, 도로명|동|''}
    # 검색창에 들어가게 되면 다음 페이지에 더욱 내용이 담겨있으나 그렇게 많은 정보를 검색해서 내놓기에는 효용성이 떨어진다고 판단하여 10개만 추출하기로 한다.

# 활용 예시
if __name__ == '__main__':
    candidate_list =[]
    candidate_json = {}
    search=str(input("출발/도착지를 검색해주세요 : "))
    candidate_list = find_candidate(search)
    while len(candidate_list) == 0:
        search = str(input("검색 결과가 없습니다. 다시 입력하여 주세요 :"))
        candidate_list = find_candidate(search)
    for dict in candidate_list:
        print(dict)
        print("-"*50)
    print("검색 딕셔너리 완성!")
