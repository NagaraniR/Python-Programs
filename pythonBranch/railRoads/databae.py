import MySQLdb as mdb
import datetime


class DbConnection:
    def get_train(self,arrival_time,board_station,arrival_station):
        con=mdb.connect(host='localhost',user='root',passwd="root",db="nagarani")
        cursor=con.cursor()
        result="select * from TrainDetails where DepatureStation='{board_station}' and ArrivalStation='{arrival_station}' and ArrivalTime='{arrival_time}'".format(board_station=board_station,arrival_station=arrival_station,arrival_time=arrival_time)
        cursor.execute(result)
        data=cursor.fetchall()
        con.close()
        return data

    def display(self,data):
        available_train=[]
        for details in data:
           depature_time=(datetime.datetime.min + details[0]).time()
           available_train.append(str(depature_time))
           available_train.append(details[1])
           arrival_time=(datetime.datetime.min + details[2]).time()
           available_train.append(str(arrival_time))
           available_train.append(details[3])
        print available_train   

connection=DbConnection()
data=connection.get_train("08:30:00","kodambakkam","mount")
connection.display(data)
   
