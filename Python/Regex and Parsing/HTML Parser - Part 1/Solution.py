# Author: Kai Tanaka

from html.parser import HTMLParser

n = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for attr in attrs:
            if None in attr:
                print ("-> " + attr[0] + " > " + "None")
            else:
                print ("-> " + " > ".join(attr))
                
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        
        print ("Empty :", tag)
        for attr in attrs:
            if None in attr:
                print ("-> " + attr[0] + " > " + "None")
            else:
                print ("-> " + " > ".join(attr))
                
parser = MyHTMLParser()
for i in range(n):
    parser.feed(input())