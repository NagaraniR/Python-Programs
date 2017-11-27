import MySQLdb as mdb
import datetime
def trainDetailsFDatabase():
    con=mdb.connect(host='localhost',user='root',passwd="root",db="testdb")
    with con:
        cur=con.cursor()
        cur.execute("select DepatureTime,DepatureStation from TrainDetails")
        details=cur.fetchall()
        boardingDescription=[]
        arrivalDescription=[]
        Cities=[]
    
        for detail in details:
            bordingtime =(datetime.datetime.min + detail[0]).time()
            boardDetails=[]
            boardDetails.append(str(bordingtime))
            boardDetails.append(detail[1])
            boardingDescription.append(boardDetails)

        cur.execute("select ArrivalTime,ArrivalStation from TrainDetails")
        details=cur.fetchall()
        for detail in details:
            arrivaltime=(datetime.datetime.min + detail[0]).time()
            arrivalDetails=[]
            arrivalDetails.append(str(arrivaltime))
            arrivalDetails.append(detail[1])
            arrivalDescription.append(arrivalDetails)
        cur.execute("select * from Cities")
        city=[item[0] for item in cur.fetchall()]
        return boardingDescription,arrivalDescription,city

trainDetailsFDatabase()    
