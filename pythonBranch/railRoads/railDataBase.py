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
    boarding_description=[]
    for details in depature:
        board_time =(datetime.datetime.min + details[0]).time()
        boarding_details=[]
        boarding_details.append(str(board_time))
        boarding_details.append(details[1])
        boarding_description.append(boarding_details)   
    return boarding_description        

def arrival_description():
    arrival_description=[]
    for details in arrival:
        arrival_time=(datetime.datetime.min + details[0]).time()
        arrival_details=[]
        arrival_details.append(str(arrival_time))
        arrival_details.append(details[1])
        arrival_description.append(arrival_details)   
    return arrival_description
            
def Cities():
    Cities=[]
    for city in City:
        Cities.append(city[0])    
    return Cities

boarding_description()
arrival_description()
Cities()
  
