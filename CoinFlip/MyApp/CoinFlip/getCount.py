from dbConnector import DBConnect as connect

def getHeadsCount():
    db,cursor = connect()
    getcount = f"select headscount from tosscount"
    cursor.execute(getcount)
    count = cursor.fetchone()
    headscount = int(count[0])
    return headscount

def getTailsCount():
    db,cursor = connect()
    getcount = f"select tailscount from tosscount"
    cursor.execute(getcount)
    count = cursor.fetchone()
    tailscount = int(count[0])
    return tailscount

# print(getHeadsCount())
# print(getTailsCount())