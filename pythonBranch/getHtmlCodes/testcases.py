import unittest
from sample3 import htmlTags
from sample3 import  *
class TestHtmlTags(unittest.TestCase):

    def testcheckFile(self):
        codes=open("htmlFile.txt","r").read()
        h=htmlTags()
        Expected=h.checkFile("htmlFile.txt")
        self.assertEqual(Expected[0],codes)
        self.assertEqual(Expected[1],True)

    def testsplitFile(self):
        h=htmlTags()
        expectedTags=["html","head","title","object","param"]
        expectedKeys=['type', 'data', 'width', 'height', 'name', 'value']
        expectedValues=['"application/x-flash"', '"your-file.swf"', '"0"', '"0"', '"quality"', '"high"']
        textFile=open("htmlFile.txt","r").read()
        
        actualTwo=h.splitFile(textFile)
        self.assertNotIn(expectedTags,actualTwo[0])
        self.assertEqual(actualTwo[1],expectedKeys)
        self.assertNotEqual(actualTwo[2],expectedValues)
        self.assertEqual(actualTwo[3],True)
    def testDisplay(self):
        h=htmlTags()
        check=False
        self.assertEqual(h.display(),check)

if __name__ == '__main__':
    unittest.main()
