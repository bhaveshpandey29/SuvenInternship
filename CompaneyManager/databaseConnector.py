import pymysql as sql
def DBConnect(ip="localhost",uname="root",password="04200420",dbname="companymanager"):
    try:
        db = sql.connect(ip,uname,password,dbname)
        cursor = db.cursor()
    except Exception as e:
        raise e
    else:
        return(db,cursor)

