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
        expectedTags=["html","head","title","object","param"]
        expectedKeys=['type', 'data', 'width', 'height', 'name', 'value']
        expectedValues=['"application/x-flash"', '"your-file.swf"', '"0"', '"0"', '"quality"', '"high"']
        textFile=open("htmlFile.html","r").read()
        
        actualTwo=html.split_file(textFile)
        self.assertNotIn(expectedTags,actualTwo[0])
        self.assertEqual(actualTwo[1],expectedKeys)
        self.assertNotEqual(actualTwo[2],expectedValues)
        self.assertEqual(actualTwo[3],True)
    def testDisplay(self):
        html=htmlTags()
        check=True
        tags=["head","title"]
        keys=["age","surname","middlename","lastname"]
        values=["22","Naga","Rani","Raja"]
        self.assertEqual(html.display(tags,keys,values),check)

if __name__ == '__main__':
    unittest.main()
