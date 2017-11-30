import unittest
from getHtmlCode import htmlTags
from getHtmlCode import  *
class TestHtmlTags(unittest.TestCase):

    def test_check_file(self):
        codes=open("htmlFile.html","r").read()
        html=htmlTags()
        Expected=html.check_file("htmlFile.html")
        self.assertEqual(Expected[0],codes)
        self.assertEqual(Expected[1],True)

    def test_split_file(self):
        html=htmlTags()
        Tags=["html","head","title","object","param"]
        Keys=['type', 'data', 'width', 'height', 'name', 'value']
        Values=['"application/x-flash"', '"your-file.swf"', '"0"', '"0"', '"quality"', '"high"']
        textFile=open("htmlFile.html","r").read()
        
        expected=html.split_file(textFile)
        self.assertNotIn(expected[0],Tags)
        self.assertEqual(expected[1],Keys)
        self.assertNotEqual(expected[2],Values)
        self.assertEqual(expected[3],True)
    def testDisplay(self):
        html=htmlTags()
        check=True
        tags=["head","title"]
        keys=["age","surname","middlename","lastname"]
        values=["22","Naga","Rani","Raja"]
        self.assertEqual(html.display(tags,keys,values),check)

if __name__ == '__main__':
    unittest.main()
