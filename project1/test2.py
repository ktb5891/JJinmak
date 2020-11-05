from selenium import webdriver



url = "https://v4.map.naver.com/"  # 네이버 지도 앱의 구 주소인 v4.map.naver.com를 url로 가지고 온다.
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)

# 장소의 이름을 저장할 후보 딕셔너리 생성
candidate_list = []

# 구 주소에 접근하게 되면 처음에 뜨는 팝업창 닫기
close_popup = driver.find_element_by_xpath('//*[@id="dday_popup"]/div[2]/button')
driver.execute_script("arguments[0].click();", close_popup)

# 검색창 찾아 검색어 입력
driver.find_element_by_id("search-input").send_keys("신림동 572-1")
# 검색 버튼 클릭
search_bnt = driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button')
driver.execute_script("arguments[0].click();", search_bnt)

# 컴퓨터 내에서는 기다릴 필요가 없었으나 인터넷 상태가 좋지 않을 것을 고려하여 작성
driver.implicitly_wait(2)
