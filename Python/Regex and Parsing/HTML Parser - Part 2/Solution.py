# Author: Kai Tanaka

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        # Single line comment
        if len(data.split('\n')) == 1:
            print(">>> Single-line Comment", data, sep="\n")
        # Multiline comment
        else:
            print(">>> Multi-line Comment",data, sep="\n")
            
    def handle_data(self, data):
        if data.strip():
            print(">>> Data",data, sep="\n")

  
    
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()