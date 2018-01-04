from railDataBase import DbConnection


class Railroads:

    def __init__(self):
        self.passenger_details = {}
        details = DbConnection()
        details.get_depature_description()
        details.get_arrival_description()
        details.get_stations_passby()
        self.depature_trains_description = details.depature_trains_description
        self.arrival_trains_description = details.arrival_trains_description
        self.passby_stations = details.passby_stations

    def add_passenger_details(self, arrival_time, boarding_point, arrival_point):
        self.passenger_details["arrival_time"] = arrival_time
        self.passenger_details["boarding_point"] = boarding_point
        self.passenger_details["arrival_point"] = arrival_point

    def getPointToPoint(self):
        direct_boarding_trains = []
        direct_arrival_trains = []
        missmatch_boarding_trains = []
        missmatch_destination_trains = []
        index=0
        for i in range(0,len(self.depature_trains_description)):
            if self.depature_trains_description[i][index+1]==self.passenger_details["boarding_point"]:
                if self.arrival_trains_description[i][index+1]==self.passenger_details["arrival_point"]:
                    if self.arrival_trains_description[i][index]<=self.passenger_details["arrival_time"]:
                        direct_boarding_trains.append(self.depature_trains_description[i])
                        direct_arrival_trains.append(self.arrival_trains_description[i])
                        
                else:
                    missmatch_boarding_trains.append(self.depature_trains_description[i])
                    missmatch_destination_trains.append(self.arrival_trains_description[i])
            else:
                missmatch_boarding_trains.append(self.depature_trains_description[i])
                missmatch_destination_trains.append(self.arrival_trains_description[i])
        return direct_boarding_trains, direct_arrival_trains, missmatch_boarding_trains, missmatch_destination_trains
        
    def check_missmatch_train(self,missmatch_boarding_trains, missmatch_destination_trains):
        boarding_trains = []
        arrival_trains = []
        count=0
        for i in range(0,len(missmatch_boarding_trains)):
            if missmatch_boarding_trains[i][count+1] == self.passenger_details["boarding_point"]:
                if missmatch_destination_trains[i][count+1] in self.passby_stations:
                    if missmatch_destination_trains[i][count]<self.passenger_details["arrival_time"]:
                        boarding_trains.append(missmatch_boarding_trains[i])
                        arrival_trains.append(missmatch_destination_trains[i])
                    else:
                        pass
        return boarding_trains, arrival_trains
    
    def get_jump_train(self, boarding_trains, arrival_trains, missmatch_boarding_trains, missmatch_destination_trains):
        jump_board_trains = []
        jump_arrival_trains = []
        count=0
        success="Error"
        for i in range(0,len(arrival_trains)):
            for j in range(0,len(missmatch_boarding_trains)):
                if missmatch_boarding_trains[j][count+1]==arrival_trains[i][count+1]:
                    if missmatch_boarding_trains[j][count]>=arrival_trains[i][count] and missmatch_boarding_trains[j][count]<self.passenger_details["arrival_time"]:
                        if missmatch_destination_trains[j][count+1]==self.passenger_details["arrival_point"]:
                            if missmatch_destination_trains[j][count]<=self.passenger_details["arrival_time"]:
                                jump_board_trains.append(missmatch_boarding_trains[i])
                                jump_arrival_trains.append(missmatch_destination_trains[j])

                            else:
                                if len(jump_board_trains)==0: 
                                    print  success
        return  jump_board_trains, jump_arrival_trains

    def split_availabletrain(self,direct_boarding_trains,direct_arrival_trains,jump_board_trains, jump_arrival_trains):
        correct_time_depature=[]
        correct_time_arrival=[]
        previous_time_depature=[]
        previous_time_arrival=[]
        bordings=direct_boarding_trains+jump_board_trains
        destinations=direct_arrival_trains+jump_arrival_trains
        count=0
        if len(destinations)>1:
            Time=[time[0]for time in destinations]
            Time=sorted(Time,key=str,reverse=True)
            firstmax=Time[0]
            secondmax=Time[1]
            if Time[0]>Time[1]:
                firstmax=Time[0]
                secondmax=Time[1]
            else:
                for i in range(2,len(Time)):
                    if Time[i]<firstmax:
                        secondmax=Time[i]
                        break
            for i in range(0,len(destinations)):
                if destinations[i][count]==self.passenger_details["arrival_time"]:
                    correct_time_depature.append(bordings[i])
                    correct_time_arrival.append(destinations[i])
                else:
                    if destinations[i][count]==secondmax:
                        previous_time_depature.append(bordings[i])
                        previous_time_arrival.append(destinations[i])
        elif len(bordings) == 1:
            if destinations[0][0]==self.passenger_details["arrival_time"]:
                correct_time_depature.append(bordings)
                correct_time_arrival.append(destinations)
            else:
                previous_time_depature.append(bordings)
                previous_time_arrival.append(destinations)
        else:
            print "Train schedule does not have available train which you want to go"
        return correct_time_depature,correct_time_arrival,previous_time_depature,previous_time_arrival
                    
    def pick_train(self,correctTimeDepature,correctTimeArrival,previousTimeDepature,previousTimeArrival):
        issuccess=True
        try:    
            if len(correctTimeDepature)>=1:
                Time=[time[0] for time in correctTimeDepature]
                Time=sorted(Time,key=str,reverse=True)
                index=0
                for i in range(0,len(correctTimeDepature)):
                    if correctTimeDepature[i][index]==Time[0]:
                        print "Fastest Available train to go:",'\n',correctTimeDepature[i],'\n',correctTimeArrival[i]
            elif len(previousTimeDepature)>=1:
                Time=[time[0] for time in previousTimeDepature]
                Time=sorted(Time,key=str,reverse=True)
                count=0
                for i in range(0,len(previousTimeDepature)):
                    if previousTimeDepature[i][count]==Time[0]:
                        print "Fastest Available train to go:",'\n',previousTimeDepature[i],'\n',previousTimeArrival[i]
            else:
                pass
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return  issuccess   

if __name__ == "__main__":
    train = Railroads()
    passenger_details=train.add_passenger_details("08:30:00", "kodambakkam", "mount")
    trains_details = train.getPointToPoint()
    boarding_trains, arrival_trains = train.check_missmatch_train(trains_details[2], trains_details[3])
    jump_board_trains, jump_arrival_trains = train.get_jump_train(boarding_trains, arrival_trains, trains_details[2], trains_details[3])
    available_trains = train.split_availabletrain(trains_details[0], trains_details[1], jump_board_trains, jump_arrival_trains)
    train.pick_train(available_trains[0],available_trains[1],available_trains[2],available_trains[3])
