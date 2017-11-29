import MySQLdb as mdb
import datetime

con=mdb.connect(host='localhost',user='root',passwd="root",db="testdb")
with con:
    cur=con.cursor()
    cur.execute("select DepatureTime,DepatureStation from TrainDetails")
    depature=cur.fetchall()
    cur.execute("select ArrivalTime,ArrivalStation from TrainDetails")
    arrival=cur.fetchall()
    cur.execute("select * from Cities")
    City=cur.fetchall()
    
def boarding_description():
    boardingDescription=[]
    for detail in depature:
        bordingtime =(datetime.datetime.min + detail[0]).time()
        boardDetails=[]
        boardDetails.append(str(bordingtime))
        boardDetails.append(detail[1])
        boardingDescription.append(boardDetails)
    return boardingDescription        

def arrival_description():
    arrivalDescription=[]
    for detail in arrival:
        arrivaltime=(datetime.datetime.min + detail[0]).time()
        arrivalDetails=[]
        arrivalDetails.append(str(arrivaltime))
        arrivalDetails.append(detail[1])
        arrivalDescription.append(arrivalDetails)
    return arrivalDescription
            
def Cities():
    Cities=[]
    for city in City:
        Cities.append(city[0])  
    return Cities

boarding_description()
arrival_description()
Cities()
  
