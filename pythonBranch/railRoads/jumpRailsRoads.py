from railDataBase import DbConnection


class Railroads:

    def database_values(self):
        connection=DbConnection()
        bording_details=connection.boarding_description()
        arrival_details=connection.arrival_description()
        cities=connection.Cities()
        return bording_details,arrival_details,cities

    def input_passenger_details(self):
        passenger_details={"arrival_time":"08:30:00","boarding_point":"kodambakkam","arrival_point":"mount"}
        return passenger_details

    def getPointToPoint(self,bording_details,arrival_details,passenger_details):
        boarding_stations=[]
        arrival_stations=[]
        jump_boardings=[]
        jump_destinations=[]
        index=0
        for i in range(0,len(bording_details)):
            if bording_details[i][index+1]==passenger_details["boarding_point"]:
                if arrival_details[i][index+1]==passenger_details["arrival_point"]:
                    if arrival_details[i][index]<=passenger_details["arrival_time"]:
                        boarding_stations.append(bording_details[i])
                        arrival_stations.append(arrival_details[i])
                        
                else:
                    jump_boardings.append(bording_details[i])
                    jump_destinations.append(arrival_details[i])
            else:
                jump_boardings.append(bording_details[i])
                jump_destinations.append(arrival_details[i])
        return boarding_stations,arrival_stations,jump_boardings,jump_destinations
        
    def jump_train(self,jump_boardings,jump_destinations,passenger_details,cities):
        jump_boardStations=[]
        jump_endStations=[]
        count=0
        for i in range(0,len(jump_boardings)):
            if jump_boardings[i][count+1]==passenger_details["boarding_point"]:
                if jump_destinations[i][count+1] in cities:
                    if jump_destinations[i][count]<passenger_details["arrival_time"]:
                        jump_boardStations.append(jump_boardings[i])
                        jump_endStations.append(jump_destinations[i])
                    else:
                        pass
        return jump_boardStations,jump_endStations
    def get_jump_train(self,jump_boardings,jump_destinations,jump_boardStations,jump_endStations,passenger_details):
        jump_board_stations=[]
        jump_end_stations=[]
        count=0
        success="Error"
        for i in range(0,len(jump_endStations)):
            for j in range(0,len(jump_boardings)):
                if jump_boardings[j][count+1]==jump_endStations[i][count+1]:
                    if jump_boardings[j][count]>=jump_endStations[i][count] and jump_boardings[j][count]<passenger_details["arrival_time"]:
                        if jump_destinations[j][count+1]==passenger_details["arrival_point"]:
                            if jump_destinations[j][count]<=passenger_details["arrival_time"]:
                                jump_board_stations.append(jump_boardStations[i])
                                jump_end_stations.append(jump_destinations[j])

                            else:
                                if len(jump_board_stations)==0: 
                                    print  success
        return  jump_board_stations, jump_end_stations

    def split_availabletrain(self,boarding_stations,arrival_stations,jump_board_stations, jump_end_stations,passenger_details):
        correct_time_depature=[]
        correct_time_arrival=[]
        previous_time_depature=[]
        previous_time_arrival=[]
        bording=boarding_stations+jump_board_stations
        destination=arrival_stations+jump_end_stations
        count=0
        if len(destination)>1:
            Time=[time[0]for time in destination]
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
            for i in range(0,len(destination)):
                if destination[i][count]==passenger_details["arrival_time"]:
                    correct_time_depature.append(bording[i])
                    correct_time_arrival.append(destination[i])
                else:
                    if destination[i][count]==secondmax:
                        previous_time_depature.append(bording[i])
                        previous_time_arrival.append(destination[i])
        elif len(bording) == 1:
            if destination[0][0]==passenger_details["arrival_time"]:
                correct_time_depature.append(bording)
                correct_time_arrival.append(destination)
            else:
                previous_time_depature.append(bording)
                previous_time_arrival.append(destination)
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
    details=Railroads()
    passenger_details=details.input_passenger_details()
    bordingDetails,arrivalDetails,cities=details.database_values()
    boardingStations,arrivalStations,jump_boardings,jump_destinations=details.getPointToPoint(bordingDetails,arrivalDetails,passenger_details)
    board_stations, end_stations=details.jump_train(jump_boardings,jump_destinations,passenger_details,cities)
    jump_board_stations,jump_end_stations=details.get_jump_train(jump_boardings,jump_destinations,board_stations,end_stations,passenger_details)
    correct_time_depature,correct_time_arrival,previous_time_depature,previous_time_arrival=details.split_availabletrain(boardingStations,arrivalStations,jump_board_stations, jump_end_stations,passenger_details)
    details.pick_train(correct_time_depature,correct_time_arrival,previous_time_depature,previous_time_arrival)

