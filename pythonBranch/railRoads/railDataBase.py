import MySQLdb as mdb
import datetime


class DbConnection:

    def __init__(self):
        self.depature_trains_description = []
        self.arrival_trains_description = []
        self.passby_stations = []
        con=mdb.connect(host ='localhost',user = 'root',passwd = "root",db = "nagarani")
        with con:
            cur = con.cursor()
            cur.execute("select DepatureTime,DepatureStation from TrainDetails")
            self.depature_trains_details = cur.fetchall() 
            cur.execute("select ArrivalTime,ArrivalStation from TrainDetails")
            self.arrival_trains_details = cur.fetchall()
            cur.execute("select * from Cities")
            self.stations = cur.fetchall()
    
    def get_depature_description(self):
        for depature_train_details in self.depature_trains_details:
            train_details = []
            depature_time =(datetime.datetime.min + depature_train_details[0]).time()
            train_details.append(str(depature_time))
            train_details.append(depature_train_details[1])
            self.depature_trains_description.append(train_details)

    def get_arrival_description(self):
        for arrival_train_details in self.arrival_trains_details:
            train_details=[]
            arrival_time=(datetime.datetime.min + arrival_train_details[0]).time()
            train_details.append(str(arrival_time))
            train_details.append(arrival_train_details[1])
            self.arrival_trains_description.append(train_details)    
            
    def get_stations_passby(self):
        for station in self.stations:
            self.passby_stations.append(station[0])
