import random
from dbConnector import DBConnect as connect
from getCount import getHeadsCount,getTailsCount

class Toss:
    while True:
        userChoice = str(input("\nDo we wish to flip the coin? (Y/N):"))
        if(userChoice == 'Y'):
            try:
                db,cursor = connect()
                number = 1
                for amount in range(number):
                    flip = random.randint(0, 1)
                    if (flip == 0):
                        try:
                            print("\tOh It's a Heads")
                            getcount = f"select headscount from tosscount"
                            cursor.execute(getcount)
                            count = cursor.fetchone()
                            headscount = int(count[0])
                            headscount = headscount+1
                            update_query = f"update tosscount set headscount={headscount}"
                            cursor.execute(update_query)
                            db.commit()
                        except Exception:
                            print("Something went wrong!")                
                    else:
                        try:
                            print("\tOh It's a Tails")
                            getcount = f"select tailscount from tosscount"
                            cursor.execute(getcount)
                            count = cursor.fetchone()
                            tailscount = int(count[0])
                            tailscount = tailscount+1
                            update_query = f"update tosscount set tailscount={tailscount}"
                            cursor.execute(update_query)
                            db.commit()
                        except Exception:
                            print("Something went wrong.")
                    
            except Exception as e:
                raise e
            finally:
                db.close()
        else:
            print("Thank you for chosing our coin flip simulation".center(100,'*'))
            print(f"Final Count:\n\n\tHeads count = {getHeadsCount()}\n\tTails count = {getTailsCount()}")
            break