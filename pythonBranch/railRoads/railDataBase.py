import MySQLdb as mdb
import datetime


class DbConnection:
    con=mdb.connect(host='localhost',user='root',passwd="root",db="testdb")
    with con:
        cur=con.cursor()
        cur.execute("select DepatureTime,DepatureStation from TrainDetails")
        depature=cur.fetchall()
        cur.execute("select ArrivalTime,ArrivalStation from TrainDetails")
        arrival=cur.fetchall()
        cur.execute("select * from Cities")
        City=cur.fetchall()
    
    def boarding_description(self):
        boardingDescription=[]
        for detail in self.depature:
            bordingtime =(datetime.datetime.min + detail[0]).time()
            boardDetails=[]
            boardDetails.append(str(bordingtime))
            boardDetails.append(detail[1])
            boardingDescription.append(boardDetails)  
        return boardingDescription        

    def arrival_description(self):
        arrivalDescription=[]
        for detail in self.arrival:
            arrivaltime=(datetime.datetime.min + detail[0]).time()
            arrivalDetails=[]
            arrivalDetails.append(str(arrivaltime))
            arrivalDetails.append(detail[1])
            arrivalDescription.append(arrivalDetails)  
        return arrivalDescription
            
    def Cities(self):
        Cities=[]
        for city in self.City:
            Cities.append(city[0])    
        return Cities
connection=DbConnection()
connection.boarding_description()
connection.arrival_description()
connection.Cities()
