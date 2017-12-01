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

    def test_getPointToPoint(self):
        details=Railroads()
        arrivals=[['08:10:00', 'mambalam'],
                  ['08:20:00', 'guindy'], ['08:25:00', 'mount'],
                  ['08:20:00', 'mount'], ['08:30:00', 'mount'], ['08:30:00', 'mount'],
                  ['08:35:00', 'mount'], ['08:40:00', 'mount'], ['10:06:00', 'Frankfurt'],
                  ['15:50:00', 'Darmstadt'], ['14:11:00', 'Darmstadt'],
                  ['08:30:00', 'mount'], ['08:15:00', 'guindy'], ['08:30:00', 'mount'], ['08:30:00', 'mount']]
        
        actual=details.getPointToPoint(self.boardings,arrivals,"08:30:00","kodambakkam","mount")
        expected=[['08:15:00', 'kodambakkam'],
                ['08:15:00', 'kodambakkam'], ['08:10:00', 'kodambakkam'], ['08:20:00', 'kodambakkam']]
        Expected=[['08:05:00', 'kodambakkam'], ['08:05:00', 'kodambakkam']]
        self.assertEqual(actual[0],expected)
        self.assertNotEqual(actual[0],Expected)
        self.assertIn(['08:20:00', 'guindy'],actual[3])

    def test_get_jump_train(self):
        details=Railroads()
        board=[["10:10:00","nungambakkam"],["10:25:00","chrompet"]]
        arrival=[["10:20:00","chrompet"],["10:30:00","park"]]
        actual=details.get_jump_train(board,arrival,"10:30:00","nungambakkam","park",["nungambakkam","chrompet","park"])
        expected=[["10:10:00","nungambakkam"]]
        self.assertEqual(actual[0],expected)
        self.assertNotEqual(actual[1],["10:20:00","chrompet"])
            
        
    def test_split_availabletrain(self):
        details=Railroads()
        board= [['21:00:00', 'Dindigul'], ['21:00:00', 'Dindigul'], ['20:00:00', 'Dindigul'], ['20:00:00', 'Dindigul']]
        arrival=[['24:00:00', 'Chennai'], ['23:00:00', 'Chennai'], ['24:00:00', 'Chennai'], ['023:00:00', 'Chennai']]
        jump_board= [['08:05:00', 'Dindigul'], ['08:05:00', 'Dindigul'], ['08:10:00', 'Dindigul']]
        jump_arrival= [['24:00:00', 'Chennai'], ['23:00:00', 'Chennai'], ['23:00:00', 'Chennai']]
        actual=details.split_availabletrain(board,arrival,jump_board,jump_arrival,"24:00:00")
        expected=[['21:00:00', 'Dindigul'], ['20:00:00', 'Dindigul'],['08:05:00', 'Dindigul']]
        self.assertEqual(actual[0],expected)
        self.assertNotEqual(actual[3],["23:30:00","Chennai"])

    def test_pick_train(self):
        details=Railroads()
        expected=details.pick_train([],[],[['21:00:00', 'Dindigul'], ['20:00:00', 'Dindigul']], [['23:00:00', 'Chennai'],['023:00:00', 'Chennai']])
        actual=True
        self.assertEqual(expected,actual)
        #corect time depature ['21:00:00', 'Dindigul'],['20:00:00', 'Dindigul']
        #correct time arrival ['24:00:00', 'Chennai'],['24:00:00', 'Chennai']
if __name__ == "__main__":
    unittest.main()
