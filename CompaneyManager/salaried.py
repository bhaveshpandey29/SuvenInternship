from abc import ABCMeta, abstractmethod
#from main import Employee
from databaseConnector import DBConnect as connect

class Salaried:    
    def RegisterEmployee(self,Sfname,Slname,Sdob,Scontact,SEmployeeBasicPay):
        try:
            flag = 0
            db,cursor = connect()
            insert_query = f"insert into salaried(salaried_fname,salaried_lname,salaried_dob,salaried_contact,salaried_basicpay) values('{Sfname}','{Slname}','{Sdob}','{Scontact}','{SEmployeeBasicPay}')"
            search_query = f"SELECT * FROM salaried WHERE salaried_contact = '{Scontact}' AND salaried_fname = '{Sfname}'"
            cursor.execute(search_query)
            rs = cursor.fetchall()
            if(len(rs)>0):
                flag = 1
            else:
                cursor.execute(insert_query)
                db.commit()
        except Exception as e:
            db.rollback()
            raise e
        else:
            if(flag == 0):
                print("inserted successfully")
            else:
                print("record already exist")
        finally:
            db.close()

    def RaiseEmployee(self,Efname,Econtact,EnewPay):
        try:
            flag = 0
            salerr = 0
            db,cursor = connect()
            update_query = f"UPDATE salaried SET salaried_basicpay = {EnewPay} WHERE salaried_fname like '{Efname}' and salaried_contact like '{Econtact}';"
            search_query = f"select * from salaried where 'salaried_fname' = '{Efname}' and salaried_contact like {Econtact}"
            searchPay_query = f"SELECT `salaried_basicpay` FROM `salaried` WHERE `salaried_contact` LIKE {Econtact}"
            cursor.execute(search_query)
            rs = cursor.fetchall()
            if(len(rs)>0):
                flag = 1
            else:
                cursor.execute(searchPay_query)
                data = list(cursor.fetchone())
                if(EnewPay > int(data[0])):
                    cursor.execute(update_query)
                    db.commit()
                else:
                    print(f"WARNING!!!!{Efname} have more salary than you have entered.")
                    salerr = 1
                    
        except Exception as e:
            db.rollback()
            raise e
        else:
            if(flag == 0 and salerr == 0):
                print(f"Record Updated now new Basic Pay of {Efname} is {EnewPay}")  
                #print(data[0])
            elif(salerr == 0):
                print(f"Seems like the employee doesn't exists, Please add the employee first.")            
        finally:
            db.close()

# s = Salaried()
# s.RaiseEmployee('Test','36521355','1400')

    def removeEmployee(self,Efname,Elname):
        try:
            flag = 0
            salerr = 0
            db,cursor = connect()
            remove_query = f"DELETE from salaried WHERE salaried_fname = '{Efname}' and salaried_lname = '{Elname}'"
            search_query = f"select * from salaried where salaried_fname = '{Efname}' and salaried_lname =  '{Elname}'"
            cursor.execute(search_query)
            rs = cursor.fetchall()
            if(len(rs)>0):
                cursor.execute(remove_query)
                db.commit()              
            else:
                flag = 1                                                  
        except Exception as e:
            print("Something went wrong!")
            db.rollback()
            raise e
        else:
            if(flag == 0):
                print(f"Great! Now {Efname} {Elname} is removed from your company's record.")  
            else:
                print(f"Seems like the employee {Efname} {Elname} doesn't exists, Please enter the correct details next time.")    
        finally:
            db.close()