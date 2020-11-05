import pymysql

def create_favorit_tbl():
    con, cur = None, None

    # con = pymysql.connect(
    #     host='127.0.0.1',user='root',password='1234',
    #     db='jjinmak',charset='utf8')
    con = pymysql.connect(host='localhost', user='root', passwd='1234', db='flaskdb', charset='utf8')

    cur = con.cursor()
    sql = """create table if not exists favorit_tbl(
    favoriteNo int(3) auto_increment primary key,
    favoriteTitle varchar(30) not null,
    favoriteX float(12,7) not null,
    favoriteY float(11,7) not null,
    userID varchar(12) not null
    );"""
    cur.execute(sql)

    con.commit()
    con.close()


def add_favorite(favoriteTitle, favoriteAddr, favoriteX, favoriteY, userID):
    con, cur = None,None

    # con = pymysql.connect(
    #     host='127.0.0.1',user='root',password='1234',
    #     db='jjinmak',charset='utf8')
    con = pymysql.connect(host='localhost', user='root', passwd='1234', db='flaskdb', charset='utf8')


    cur = con.cursor()
    sql = "INSERT INTO favorit_tbl(favoriteTitle, favoriteAddr, favoriteX, favoriteY, userID) VALUE (%s,%s,%s,%s,%s);"
    cur.execute(sql,(favoriteTitle, favoriteAddr, favoriteX, favoriteY, userID))

    con.commit()
    con.close()

def delete_favorite(favoritNo):
    con, cur = None,None

    # con = pymysql.connect(
    #     host='127.0.0.1',user='root',password='1234',
    #     db='jjinmak',charset='utf8')
    con = pymysql.connect(host='localhost', user='root', passwd='1234', db='flaskdb', charset='utf8')


    cur = con.cursor()
    sql = "DELETE FROM favorit_tbl WHERE favoriteNo = %s;"
    cur.execute(sql,(favoritNo))

    con.commit()
    con.close()

def show_favorite(userID):
    con, cur = None, None
    con = pymysql.connect(host='127.0.0.1', user='root', passwd='1234', db='flaskdb', charset='utf8')
    # con = pymysql.connect(host='localhost',
    #                        user='root',
    #                        passwd='1234',
    #                        db='python',
    #                        charset='utf8')

    cur = con.cursor()
    with cur as curs:
        sql = 'select * from favorit_tbl WHERE userID=%s;'
        curs.execute(sql,(userID))
        rs = curs.fetchall()
        temp_list = []
        for row in rs:
            temp_dic = {}
            temp_dic['favoriteNo'] = row[0]
            temp_dic['favoriteTitle'] = row[1]
            temp_dic['favoriteAddress'] = row[2]
            temp_dic['favoriteX'] = row[3]
            temp_dic['favoriteY'] = row[4]
            temp_dic['userID'] = row[5]
            temp_list.append(temp_dic)

    con.commit()
    con.close()
    return temp_list

if __name__ == '__main__':
    create_favorit_tbl()
    favoriteTitle = "태범이네"
    favoriteAddr = "서울특별시 관악구 신림동 572-1"
    favoriteX = 126.725754537688
    favoriteY = 37.3936585257304
    userID = "tuuuuuuuna"
    add_favorite(favoriteTitle, favoriteAddr, favoriteX, favoriteY, userID)
    # delete_favorite(favoriteTitle, userID)
    dict = show_favorite("tuuuuuuuna")
    print(dict)