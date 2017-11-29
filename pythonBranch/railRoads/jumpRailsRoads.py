import railDataBase


class Railroads:
    bordinsDetails=railDataBase.boarding_description()
    arrivalDetails=railDataBase.arrival_description()
    cities=railDataBase.Cities()

    def pointToPoint(self):
        boardingStations=[]
        arrivalStations=[]
        jumpBoardings=[]
        jumpDestinations=[]
        boardingTime=[]
        for i in range(0,len(self.bordinsDetails)):
            for j in range(0,len(self.bordinsDetails)):
                boardingTime.append(self.bordinsDetails[i][j])
                break  
        boardingStations=[]
        arrivalStations=[]
        latestTime=sorted(boardingTime, key=str, reverse=True)
        index=0
        for i in range(0,len(self.bordinsDetails)):
            for ind in range(0,len(latestTime)):
                if self.bordinsDetails[i][index+1]==self.boarding:
                    if self.arrivalDetails[i][index+1]==self.destination:
                        if self.bordinsDetails[i][index]==latestTime[ind]:
                            if self.arrivalDetails[i][index] <= self.arrivaltime:
                                boardingStations.append(self.bordinsDetails[i])
                                arrivalStations.append(self.arrivalDetails[i])
                                break
                    else:
                        jumpBoardings.append(self.bordinsDetails[i])
                        jumpDestinations.append(self.arrivalDetails[i])
                        break
                else:
                    jumpBoardings.append(self.bordinsDetails[i])
                    jumpDestinations.append(self.arrivalDetails[i])
                    break
        self.b=boardingStations
        self.a=arrivalStations
        return boardingStations,arrivalStations,jumpBoardings,jumpDestinations
        
    def jump_train(self,jumpBoardings,jumpDestinations):
        boardstations=[]
        endstations=[]
        index=0
        for i in range(0,len(jumpBoardings)):
            if jumpBoardings[i][index+1]==self.boarding:
                if jumpBoardings[i][index]>=self.starttime:
                    if jumpDestinations[i][index+1] in self.cities:
                        if jumpDestinations[i][index]<=self.arrivaltime:
                            for j in range(0,len(jumpBoardings)):
                                if jumpDestinations[i][index+1]==jumpBoardings[j][index+1]:
                                    if jumpBoardings[j][index]>=jumpDestinations[i][index] and jumpBoardings[j][index]<self.arrivaltime:
                                        if jumpDestinations[j][index+1]==self.destination:
                                            if jumpDestinations[j][index]<=self.arrivaltime:
                                                boardstations.append(jumpBoardings[i])
                                                endstations.append(jumpDestinations[j])
            else:
                pass
        return  boardstations, endstations

    def start_time(self):
        startTime=raw_input("Enter start time of jill:")
        self.starttime=startTime
        return startTime
    
    def arrival_time(self):
        arrivalTime=raw_input("Correct time to arrival:")
        self.arrivaltime=arrivalTime
        return arrivalTime
    
    def boarding_point(self):
        boardingPoint=raw_input("Enter boarding point:")
        self.boarding=boardingPoint
        return boardingPoint
    
    def arrival_point(self):
        arrivalPoint=raw_input("Enter arrival point:")
        self.destination=arrivalPoint
        return arrivalPoint


    def pick_Train(self,boardingStations,arrivalStations,boardstations, endstations):
       bording=boardingStations+boardstations
       destination=arrivalStations+endstations
       availabletrain=[]
       index=0
       time=[i[0] for i in bording]
       Time=sorted(time, key=str, reverse=True)
       for i in range(0,len(destination)):
           if destination[i][index]==self.arrivaltime:
               availabletrain.append(bording[i])
               availabletrain.append(destination[i])
               print "the available train to go:",'\n',bording[i],'\n',destination[i]
               break
           else:
               if destination[i][index]==Time[0]:
                   availabletrain.append(bording[i])
                   availabletrain.append(destination[i])
                   print "available train to go:",'\n',bording[i],'\n',destination[i]
                   break
       return availabletrain      
               

      

if __name__ == "__main__":
   
    details=Railroads()
    details.start_time()
    details.arrival_time()
    details.boarding_point()
    details.arrival_point()
    boardingStations,arrivalStations,jumpBoardings,jumpDestinations=details.pointToPoint()
    boardstations, endstations=details.jump_train(jumpBoardings,jumpDestinations)
    details.pick_Train(boardingStations,arrivalStations,boardstations, endstations)

    
