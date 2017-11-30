import unittest
from jumpRailsRoads import *
from jumpRailsRoads import Railroads
import MySQLdb as mdb
import datetime


class test(unittest.TestCase):
    con=mdb.connect(host='localhost',user='root',passwd="root",db="testdb")
    with con:
        cur=con.cursor()
        cur.execute("select DepatureTime,DepatureStation from TrainDetails")
        details=cur.fetchall()
        boardings=[]
        for detail in details:
            bordingtime =(datetime.datetime.min + detail[0]).time()
            boardDetails=[]
            boardDetails.append(str(bordingtime))
            boardDetails.append(detail[1])
            boardings.append(boardDetails)

    def setUp(self):
        pass

    def test_poinToPoint(self):
        details=Railroads()
        arrivals=[['08:10:00', 'mambalam'],
                  ['08:20:00', 'guindy'], ['08:25:00', 'mount'],
                  ['08:20:00', 'mount'], ['08:30:00', 'mount'], ['08:30:00', 'mount'],
                  ['08:35:00', 'mount'], ['08:40:00', 'mount'], ['10:06:00', 'Frankfurt'],
                  ['15:50:00', 'Darmstadt'], ['14:11:00', 'Darmstadt'],
                  ['08:30:00', 'mount'], ['08:15:00', 'guindy'], ['08:30:00', 'mount'], ['08:30:00', 'mount']]
        
        expected=details.getPointToPoint(self.boardings,arrivals,"08:30:00","kodambakkam","mount")
        actualOne=[['08:15:00', 'kodambakkam'],
                ['08:15:00', 'kodambakkam'], ['08:10:00', 'kodambakkam'], ['08:20:00', 'kodambakkam']]
        actualTwo=[['08:05:00', 'kodambakkam'], ['08:05:00', 'kodambakkam']]
        self.assertEqual(expected[0],actualOne)
        self.assertNotEqual(expected[0],actualTwo)

    def test_jump_train(self):
        details=Railroads()
        board=[["10:10:00","nungambakkam"],["10:25:00","chrompet"]]
        arrival=[["10:20:00","chrompet"],["10:30:00","park"]]
        expected=details.jump_train(board,arrival,"10:30:00","nungambakkam","park",["nungambakkam","chrompet","park"])
        actual=[["10:10:00","nungambakkam"]]
        self.assertEqual(expected[0],actual)
            
        
    def test_split_availabletrain(self):
        details=Railroads()
        board= [['21:00:00', 'Dindigul'], ['21:00:00', 'Dindigul'], ['20:00:00', 'Dindigul'], ['20:00:00', 'Dindigul']]
        arrival=[['24:00:00', 'Chennai'], ['23:00:00', 'Chennai'], ['24:00:00', 'Chennai'], ['023:00:00', 'Chennai']]
        jump_board= [['08:05:00', 'Dindigul'], ['08:05:00', 'Dindigul'], ['08:10:00', 'Dindigul']]
        jump_arrival= [['24:00:00', 'Chennai'], ['23:00:00', 'Chennai'], ['23:00:00', 'Chennai']]
        expected=details.split_availabletrain(board,arrival,jump_board,jump_arrival,"24:00:00")
        actual=[['21:00:00', 'Dindigul'], ['20:00:00', 'Dindigul'],['08:05:00', 'Dindigul']]
        self.assertEqual(expected[0],actual)

    def test_pick_train(self):
        details=Railroads()
        expected=details.pick_train([['21:00:00', 'Dindigul'],['20:00:00', 'Dindigul']],[['24:00:00', 'Chennai'],['24:00:00', 'Chennai']],[['21:00:00', 'Dindigul'], ['20:00:00', 'Dindigul']], [['23:00:00', 'Chennai'],['023:00:00', 'Chennai']])
        actual=True
        self.assertEqual(expected,actual)

        
        
        

if __name__ == "__main__":
    unittest.main()
