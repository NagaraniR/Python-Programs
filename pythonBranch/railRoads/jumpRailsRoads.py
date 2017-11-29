import railDataBase


class Railroads:

    def database_values(self):
        bordinsDetails=railDataBase.boarding_description()
        arrivalDetails=railDataBase.arrival_description()
        cities=railDataBase.Cities()
        return bordinsDetails,arrivalDetails,cities

    def getPointToPoint(self,bordinsDetails,arrivalDetails,arrivaltime,boardingpoint,arrivalpoint):
        boardingStations=[]
        arrivalStations=[]
        jumpBoardings=[]
        jumpDestinations=[]
        index=0
        for i in range(0,len(bordinsDetails)):
            if bordinsDetails[i][index+1]==boardingpoint:
                if arrivalDetails[i][index+1]==arrivalpoint:
                    if arrivalDetails[i][index]<=arrivaltime:
                        boardingStations.append(bordinsDetails[i])
                        arrivalStations.append(arrivalDetails[i])
                        
                else:
                    jumpBoardings.append(bordinsDetails[i])
                    jumpDestinations.append(arrivalDetails[i])
            else:
                jumpBoardings.append(bordinsDetails[i])
                jumpDestinations.append(arrivalDetails[i])       
        return boardingStations,arrivalStations,jumpBoardings,jumpDestinations
        
    def jump_train(self,jumpBoardings,jumpDestinations,arrivaltime,boardingpoint,arrivalpoint,cities):
        boardstations=[]
        endstations=[]
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
                                            boardstations.append(jumpBoardings[i])
                                            endstations.append(jumpDestinations[j])
            else:
                pass
        return  boardstations, endstations
    
    def arrival_time(self):
        arrivaltime=raw_input("Correct time to arrival:")
        return arrivaltime
    
    def boarding_point(self):
        boardingpoint=raw_input("Enter boarding point:")
        return boardingpoint
    
    def arrival_point(self):
        arrivalpoint=raw_input("Enter arrival point:")
        return arrivalpoint

    def split_availabletrain(self,boardingStations,arrivalStations,boardstations, endstations):
        correcttimedepature=[]
        correcttimearrival=[]
        previoustimedepature=[]
        previoustimearrival=[]
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
            if len(bording)>1:
                for i in range(0,len(destination)):
                    if destination[i][count]==arrivaltime:
                        correcttimedepature.append(bording[i])
                        correcttimearrival.append(destination[i])
                    else:
                        if destination[i][count]==secondmax:
                            previoustimedepature.append(bording[i])
                            previoustimearrival.append(destination[i])
        else:
            print "the avalable train to go:",'\n',bording,'\n',destination
        return correcttimedepature,correcttimearrival,previoustimedepature,previoustimearrival
                    
    def pick_train(self,correcttimedepature,correcttimearrival,previoustimedepature,previoustimearrival):
        if len(correcttimedepature)>=1:
            Time=[time[0] for time in correcttimedepature]
            Time=sorted(Time,key=str,reverse=True)
            index=0
            for i in range(0,len(correcttimedepature)):
                if correcttimedepature[i][index]==Time[0]:
                    print "The available train to go:",'\n',correcttimedepature[i],'\n',correcttimearrival[i]
        elif len(previoustimedepature)>=1:
            Time=[time[0] for time in previoustimedepature]
            Time=sorted(Time,key=str,reverse=True)
            count=0
            for i in range(0,len(previoustimedepature)):
                if previoustimedepature[i][count]==Time[0]:
                    print "the available train to go:",'\n',previoustimedepature[i],'\n',previoustimearrival[i]

if __name__ == "__main__":
    details=Railroads()
    arrivaltime=details.arrival_time()
    boardingpoint=details.boarding_point()
    arrivalpoint=details.arrival_point()
    bordinsDetails,arrivalDetails,cities=details.database_values()
    boardingStations,arrivalStations,jumpBoardings,jumpDestinations=details.getPointToPoint(bordinsDetails,arrivalDetails,arrivaltime,boardingpoint,arrivalpoint)
    boardstations, endstations=details.jump_train(jumpBoardings,jumpDestinations,arrivaltime,boardingpoint,arrivalpoint,cities)
    correcttimedepature,correcttimearrival,previoustimedepature,previoustimearrival=details.split_availabletrain(boardingStations,arrivalStations,boardstations, endstations)
    details.pick_train(correcttimedepature,correcttimearrival,previoustimedepature,previoustimearrival)
