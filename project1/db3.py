import pymysql

def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='flaskdb'
            , charset='utf8')
    if conn:
        print('디비 접속 완료')
    return conn
#연결 테스트 함수 호출
# get_connection()

def get_member_list():

    #커서 생성
    conn = get_connection()
    cursor = conn.cursor()

    #sql문 쿼리문
    sql = '''select * from membertbl order by userno asc'''
    cursor.execute(sql)

    #결과를 가져온다.
    result = cursor.fetchall()

    #튜플구조 => 리스트 딕셔너리
    #sql문 쿼리문
    temp_list = []
    for row in result:
        temp_dic = {}
        temp_dic['userNo'] = row[0]
        temp_dic['userid'] = row[1]
        temp_dic['userName'] = row[2]
        temp_dic['pwd'] = row[3]
        temp_list.append(temp_dic)

    # for row in temp_list:
    #     for key in row:
    #         print(key, ' => ', row[key])
    #     print('='*25)

    #접속 종료
    conn.close()
    return temp_list

# get_member_list()


def add_member(m_id, m_name, m_pwd):
    #커서 생성
    conn = get_connection()
    cursor = conn.cursor()

    #sql문 쿼리문
    sql = '''insert into membertbl (userid, username,pwd) values (%s,%s,%s)'''
    
    cursor.execute(sql,(m_id,m_name,m_pwd))
    conn.commit()
    conn.close()

# member_add('tester2','박보영','5509')

# userId가 있으면 0을 반환
# 특정 레코드 반환
def member(userid):
    #커서 생성
    conn = get_connection()
    cursor = conn.cursor()

    #sql문 쿼리문
    sql = '''select * from membertbl where userid = %s'''
    cursor.execute(sql,userid)

    #결과를 가져온다.
    result = cursor.fetchone()
    if result:
        temp_dic = {}
        temp_dic['userNo'] = result[0]
        temp_dic['userid'] = result[1]
        temp_dic['userName'] = result[2]
        temp_dic['pwd'] = result[3]
        conn.close()
        return temp_dic
    else:
        conn.close()
        return 0

# print(member('admin'))
# print(member('aaaaaaa'))