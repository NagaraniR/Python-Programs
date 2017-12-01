import railDataBase


class Railroads:

    def database_values(self):
        bording_details=railDataBase.boarding_description()
        arrival_details=railDataBase.arrival_description()
        cities=railDataBase.Cities()
        return bording_details,arrival_details,cities

    def getPointToPoint(self,bording_details,arrival_details,arrival_time,boarding_point,arrival_point):
        boardingStations=[]
        arrivalStations=[]
        jumpBoardings=[]
        jumpDestinations=[]
        index=0
        for i in range(0,len(bording_details)):
            if bording_details[i][index+1]==boarding_point:
                if arrival_details[i][index+1]==arrival_point:
                    if arrival_details[i][index]<=arrival_time:
                        boardingStations.append(bording_details[i])
                        arrivalStations.append(arrival_details[i])
                        
                else:
                    jumpBoardings.append(bording_details[i])
                    jumpDestinations.append(arrival_details[i])
            else:
                jumpBoardings.append(bording_details[i])
                jumpDestinations.append(arrival_details[i])
        return boardingStations,arrivalStations,jumpBoardings,jumpDestinations
        
    def get_jump_train(self,jumpBoardings,jumpDestinations,arrivaltime,boardingpoint,arrivalpoint,cities):
        jump_boardStations=[]
        jump_endStations=[]
        index=0
        for i in range(0,len(jumpBoardings)):
            if jumpBoardings[i][index+1]==boardingpoint:
                if jumpDestinations[i][index+1] in cities:
                    if jumpDestinations[i][index]<arrivaltime:
                        for j in range(0,len(jumpBoardings)):
                            if jumpDestinations[i][index+1]==jumpBoardings[j][index+1]:
                                if jumpBoardings[j][index]>=jumpDestinations[i][index] and jumpBoardings[j][index]<arrivaltime:
                                    if jumpDestinations[j][index+1]==arrivalpoint:
                                        if jumpDestinations[j][index]<=arrivaltime:
                                            jump_boardStations.append(jumpBoardings[i])
                                            jump_endStations.append(jumpDestinations[j])
            else:
                pass
        return  jump_boardStations, jump_endStations
    
    def input_arrival_time(self):
        arrival_time=raw_input("Correct time to arrival:")
        return arrival_time
    
    def input_boarding_point(self):
        boarding_point=raw_input("Enter boarding point:")
        return boarding_point
    
    def input_arrival_point(self):
        arrival_point=raw_input("Enter arrival point:")
        return arrival_point

    def split_availabletrain(self,boardingStations,arrivalStations,boardstations, endstations,arrivaltime):
        correct_time_depature=[]
        correct_time_arrival=[]
        previous_time_depature=[]
        previous_time_arrival=[]
        bording=boardingStations+boardstations
        destination=arrivalStations+endstations
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
                if destination[i][count]==arrivaltime:
                    correct_time_depature.append(bording[i])
                    correct_time_arrival.append(destination[i])
                else:
                    if destination[i][count]==secondmax:
                        previous_time_depature.append(bording[i])
                        previous_time_arrival.append(destination[i])
        elif len(bording) == 1:
            if destination[0][0]==arrivaltime:
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
    arrival_time=details.input_arrival_time()
    boarding_point=details.input_boarding_point()
    arrival_point=details.input_arrival_point()
    bordingDetails,arrivalDetails,cities=details.database_values()
    boardingStations,arrivalStations,jumpBoardings,jumpDestinations=details.getPointToPoint(bordingDetails,arrivalDetails,arrival_time,boarding_point,arrival_point)
    board_stations, end_stations=details.get_jump_train(jumpBoardings,jumpDestinations,arrival_time,boarding_point,arrival_point,cities)
    correct_time_depature,correct_time_arrival,previous_time_depature,previous_time_arrival=details.split_availabletrain(boardingStations,arrivalStations,board_stations, end_stations,arrival_time)
    details.pick_train(correct_time_depature,correct_time_arrival,previous_time_depature,previous_time_arrival)
