import unittest
from getHtmlCode import htmlTags
from getHtmlCode import  *
class TestHtmlTags(unittest.TestCase):

    def test_check_file(self):
        codes=open("test_htmlFile.html","r").read()
        html=htmlTags()
        actual=html.check_file("test_htmlFile.html")
        self.assertEqual(actual[0],codes)
        self.assertEqual(actual[1],True)

    def test_remove_comment_line(self):
        codes=open("test_htmlFile.html","r").read()
        html=htmlTags()
        actual=html.remove_comment_line("htmlFile.html")
        self.assertTrue(True)

    def test_split_file(self):
        html=htmlTags()
        Tags=['body', 'html', 'img']
        Keys=['src', 'width', 'height']
        Values=["img_girl.jpg", "500", "600"]
        html_codes=open("test_htmlFile.html","r").read()
        
        actual=html.split_file(html_codes)
        self.assertNotIn(actual[0],Tags)
        self.assertEqual(actual[1],Keys)
        self.assertEqual(actual[2],Values)
        self.assertEqual(actual[3],True)
    def test_display(self):
        html=htmlTags()
        tags=["head","title"]
        keys=["age","surname","middlename","lastname"]
        values=["22","Naga","Rani","Raja"]
        self.assertEqual(html.display(tags,keys,values),True)

if __name__ == '__main__':
    unittest.main()
