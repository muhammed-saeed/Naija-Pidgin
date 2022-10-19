import sys

import urllib.request as urlreq
from html.parser import HTMLParser
import re
from html.entities import entitydefs#, name2codepoint
#from io import StringIO
#import html2text

import createQueries as cQ
import readMsFiles as M
from DefaultDict import DD
import bingFunctions as bF

#TODO solve \n, \t etc in output text


class  HTMLReader(HTMLParser):
  def __init__(self):
    self.doc = ''
    self.title = ''
    self.in_body = False
    self.in_title = False
    self.in_script = False
    self.in_style = False
    super().__init__()


  
  def handle_starttag(self, tag, attrs):
    
    if self.in_body:
      self.doc += ' '
      if tag == "script":
        self.in_script = True
      if tag == "style":
        self.in_style = True

    elif tag == 'title':
      self.in_title = True

    elif tag == "body":
      self.in_body = True
      #print('inBody')
    #print('start',tag)

  def handle_endtag(self, tag):
    if self.in_body and not self.in_script:
      self.doc += ' '

    if tag == "script":
      self.in_script = False
      if tag == "style":
        self.in_style = False
    elif tag == 'title':
      self.in_title = False
      #print(self.title)
    elif tag == "body":
      self.in_body = False
    #print('end',tag)

  def handle_data(self, data):
    if self.in_body and not self.in_script and not self.in_style:
      self.doc += data.strip()   
      #print(data.strip())
    elif self.in_title:
      self.title += data.strip()

  def handle_startendtag(self, tag, attrs):
    if self.in_body and not self.in_script and not self.in_style:
      self.doc += ' '
    #print('stend',tag)

  def handle_charref(self, name):
    try:
      if name.startswith('x'):
        c = chr(int(name[1:],16))
      else:
        c = chr(int(name))
      self.doc += c

    except Exception as e:
      print('char could not be recognized:')
      print(e)
      print('\t',self.url)

    #print('char:',name,c)

  def handle_entityref(self, name):
    #print('entity:',name, chr(name2codepoint[name]), entitydefs[name])
    try:
      self.doc += entitydefs[name] # '&' + name + ';'
    except KeyError as e:
      print('entitydefs KeyError', e)
      print('\t', self.url)


def get_doc(url):
  hr = HTMLReader()
  hr.url = url
  req = urlreq.Request(url)
  browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'
  req.add_header('User-Agent', browser)
  try:
    with urlreq.urlopen(req) as h:
      try:
        html = h.read().decode(errors='ignore')#.replace("'",'"')
      except Exception as e:
        print('error while decoding:')
        print(e)
        print('\t',url)
      #print('1\n',html)
      try:
        hr.feed(html)
      except Exception as e:
        print('error while parsing html:')
        print(e)
        print('\t',url)
        #print('\n\n2\n',hr.title,'\n',hr.doc)
  except Exception as e:
      print('error while opening website:')
      print(e)
      print('\t',url)
      return('Website could not be opened','')
  return (hr.title,re.sub('[<>"'+"']|(&(?!(quot|amp|lt|gt|apo);))",
          lambda mo:'&' + {'<':'lt','>':'gt','&':'amp','"':'quot',
            "'":'apos'}[mo.group(0)]+ ';',hr.doc))

def get_doc_section(url, queries):
  doc = get_doc(url)
  #look for smallest complete para(s)/sections including queries?
  # immer am stueck?
  

if __name__ == '__main__':
  urls = {'http://dogdishdiet.com/2011/07/how-much-dry-food-should-i-feed-my-dog/',
          'http://en.wikipedia.org/wiki/XML'}
  for url in urls:
    with open('htmltextoutput.txt','w') as f:
      title, doc = get_doc(url)
      f.write('\n\n  <title> ' + title + '</title>\n')
      f.write('  <body>\n' + doc + '\n  </body>\n')








'''
  #mit html2text
  #http://www.tek-tips.com/viewthread.cfm?qid=1604666
  encoding = 'utf-8'
  f = urllib.urlopen(url)
  try: s = f.read()
  except: print('reading failed')
  finally: f.close()
  ustr = s.decode(encoding)
  #b = StringIO()
  #old = sys.stdout
  try:
    #sys.stdout = b
    html2text.wrapwrite(html2text.html2text(ustr, url))
  
  finally: pass #sys.stdout = old
  #text = b.getvalue()
  #b.close()
  #print(text)
  return  
  #text
'''
