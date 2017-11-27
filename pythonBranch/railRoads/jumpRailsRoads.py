import railDataBase


class Railroads:
    bordinsDetails,arrivalDetails,Cities=railDataBase.trainDetailsFDatabase()
    cities=Cities
    def PointToPoint(self):
        boardingStations=[]
        arrivalStations=[]
        boardingTime=[]
        for i in range(0,len(self.bordinsDetails)):
            for j in range(0,len(self.bordinsDetails)):
                boardingTime.append(self.bordinsDetails[i][j])
                break
        index=0
        for i in range(0,len(self.bordinsDetails)):
            for ind in range(0,len(boardingTime)):
                if self.bordinsDetails[i][index+1]==self.boarding:
                    if self.arrivalDetails[i][index+1]==self.destination:
                        if self.bordinsDetails[i][index]==boardingTime[ind]:
                            if self.arrivalDetails[i][index] <= self.arrivaltime:
                                boardingStations.append(self.bordinsDetails[i])
                                arrivalStations.append(self.arrivalDetails[i])
                                break
                    else:
                        self.train_details(self.bordinsDetails[i],self.arrivalDetails[i])
                        break
                else:
                    self.train_details(self.bordinsDetails[i],self.arrivalDetails[i])
                    break
        trainDescription=boardingStations+arrivalStations
        self.boardingdescription=boardingStations
        self.arivaldescription=arrivalStations
        return trainDescription

    def train_details(self,bordinsDetails,arrivalStations):
        issuccess = True
        try:
            jumpBoardings.append(bordinsDetails)
            jumpDestinations.append(arrivalStations)
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return issuccess
        
    def jump_train(self):
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
        self.boarddescription=boardstations
        self.destinationdescription=endstations
        jumpdescription=boardstations+endstations
        return  jumpdescription   
        
    def  input_details(self):
        startTime=raw_input("Enter start time of jill:")
        self.starttime=startTime
        arrivalTime=raw_input("Correct time to arrival:")
        self.arrivaltime=arrivalTime
        boardingPoint=raw_input("Enter boarding point:")
        self.boarding=boardingPoint
        arrivalPoint=raw_input("Enter arrival point:")
        self.destination=arrivalPoint

    def pick_Train(self):
       issuccess = True
       try:
           bording=self.boardingdescription+self.boarddescription
           destination=self.arivaldescription+self.destinationdescription
           index=0
           time=[i[0] for i in bording]
           Time=sorted(time, key=str, reverse=True)
           for i in range(0,len(destination)):
               if destination[i][index]==self.arrivaltime:
                   print "the available train to go:",'\n',bording[i],'\n',destination[i]
                   break
               else:
                   if destination[i][index]==Time[0]:
                       print "available train to go:",'\n',bording[i],'\n',destination[i]
                       break
       except Exception as exception:
           issuccess=False
           template = "An exception of type {0} occurred. Arguments:\n{1!r}"
           message = template.format(type(exception).__name__, exception.args)
       return issuccess
              
if __name__ == "__main__":
    jumpBoardings=[]
    jumpDestinations=[]
    details=Railroads()
    details.input_details()
    details.PointToPoint()
    details.jump_train()
    details.pick_Train()
    
