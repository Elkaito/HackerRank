# Author: Kai Tanaka

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        [print("-> {} > {}".format(*att)) for att in attr]
    
n = int(input())
html = "\n".join([input() for _ in range(n)])
parser = MyHTMLParser()
parser.feed(html)
parser.close()