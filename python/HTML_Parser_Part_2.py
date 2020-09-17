from html.parser import HTMLParser
import re

# Link: https://www.hackerrank.com/challenges/html-parser-part-2/problem

class MyHTMLParser(HTMLParser):
    
    def pre_process_data(self, data):
        data = re.sub('\n+', '\n', data)
        data = data.strip('\n')
        lines = data.split('\n')
        return lines

    def handle_comment(self, data):
        data_lines = self.pre_process_data(data)
        if data_lines[0] == '' and len(data_lines) == 1:
            return
        if len(data_lines) == 1:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')
        for line in data_lines:
            print(line)

    def handle_data(self, data):
        data_lines = self.pre_process_data(data)
        if data_lines[0] == '' and len(data_lines) == 1:
            return
        print('>>> Data')
        for line in data_lines:
            print(line)
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
