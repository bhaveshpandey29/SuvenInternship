from abc import ABCMeta, abstractmethod
from databaseConnector import DBConnect as connect

class Manager:    
    def RegisterEmployee(self,Mfname,Mlname,Mdob,Mcontact,MemployeeBasicPay):
        try:
            flag = 0
            db,cursor = connect()
            insert_query = f"insert into manager(manager_fname,manager_lname,manager_dob,manager_contact,manager_basicpay) values('{Mfname}','{Mlname}','{Mdob}','{Mcontact}','{MemployeeBasicPay}')"
            search_query = f"select * from manager where 'manager_fname' = '{Mfname}' and manager_contact like {Mcontact}"
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
                print("New Manager added successfully")
            else:
                print("Whoops! The record already exists. Please check your records")
        finally:
            db.close()

    def RaiseEmployee(self,Efname,Econtact,EnewPay):
        try:
            flag = 0
            salerr = 0
            db,cursor = connect()
            update_query = f"UPDATE manager SET manager_basicpay = {EnewPay} WHERE manager_fname like '{Efname}' and manager_contact like '{Econtact}';"
            search_query = f"select * from manager where 'manager_fname' = '{Efname}' and manager_contact like {Econtact}"
            searchPay_query = f"SELECT `manager_basicpay` FROM `manager` WHERE `manager_contact` LIKE {Econtact}"
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
                    print(f"WARNING!!!!{Efname} have more or same salary than you have entered.")
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

    def removeEmployee(self,Efname,Elname):
        try:
            flag = 0
            salerr = 0
            db,cursor = connect()
            remove_query = f"DELETE from manager WHERE manager_fname = '{Efname}' and manager_lname = '{Elname}'"
            search_query = f"select * from manager where manager_fname = '{Efname}' and manager_lname =  '{Elname}'"
            cursor.execute(search_query)
            rs = cursor.fetchall()
            if(len(rs)>0):
                cursor.execute(remove_query)
                db.commit() 
                #flag = 1
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