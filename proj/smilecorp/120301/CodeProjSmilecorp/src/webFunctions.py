from utilities import *

import urllib.request as urlreq
from html.parser import HTMLParser
import re
from html.entities import entitydefs#, name2codepoint
entitydefs['apo'] = entitydefs['apos'] = "'" 
#from io import StringIO
#import html2text
#from tidylib import tidy_document as tidy


import createQueries as cQ
import readMsFiles as M
from DefaultDict import DD
import bingFunctions as bF

def removeLinebreaks(strng):
  return strng.replace('\n',' ') 

def remove_multiple_spaces(full_html):
  """
  Removes javascript from the html
  http://www.daniweb.com/software-development/python/threads/185151
  vidaj
  """
  #return full_html.replace('\n',' ') 
  return re.sub('[ \t]{1,}',' ', full_html) 
  # no more multiline comments
  '''
  tagRegex = re.compile("(?i)<(\/?\w+)((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>")
  tagPos = {}
  indices = []
  links = {}
  for match in tagRegex.finditer(full_html):
    name = match.group(1).lower()
    value = (name, match.group(0), match.start(), match.end())
    indices.append(match.start())
    tagPos[match.start()] = value
    if name not in links.keys(): links[name] = [value]
    else: links[name].append(value)
  indices.sort()

  html = ""
  removed = ""
  tag = 'comment'
  tagCount = len(links[tag])#self.countStartTag('script')
  startTags = links[tag]
  stopTags = links[tag]

  lastStop = 0
  for start, stop in zip(startTags, stopTags):
    html += full_html[lastStop:start[2]]
    removed += full_html[start[2]:stop[3]]
    lastStop = stop[3]
  html += full_html[lastStop]

  removeTags('script')

  #print('removed javascript:')
  #print(removed)
  return html
  '''

def remove_scriptstyle(html):
  #html = removeLinebreaks(html)
  clean = ''
  p = re.compile('<script.*?</script>',re.DOTALL)
  #p = re.compile('<s(cript|tyle).*?</s(cript|tyle)>',re.DOTALL)
  spans = []
  for i,mo in enumerate(p.finditer(html)):
    #print(i)
    #print(mo.group(0) + '\n\n')
    #span = a,b = mo.start(), mo.end()
    spans.append(mo.span())
  end = 0
  for a,b in spans:
    clean += html[end:a]
    #print('\n\nin:\n',html[end:a])
    #print('\n\nout:\n',html[a:b])
    end = b
  clean += html[end:]

  html = clean
  clean = ''
  p = re.compile('<style.*?</style>',re.DOTALL)
  spans = []
  for i,mo in enumerate(p.finditer(html)):
    #print(i)
    #print(mo.group(0) + '\n\n')
    #span = a,b = mo.start(), mo.end()
    spans.append(mo.span())
  end = 0
  for a,b in spans:
    clean += html[end:a]
    #print('\n\nin:\n',html[end:a])
    #print('\n\nout:\n',html[a:b])
    end = b
  clean += html[end:]
  return clean




def removeJavaScript(full_html):
  #TODO remove comments as HTMLParser does not recognize multiline comments
  full_html = removeLinebreaks(full_html)
  # but maybe these are mostly in javascript
  """
  Removes javascript from the html
  http://www.daniweb.com/software-development/python/threads/185151
  vidaj
  """
  tagRegex = re.compile("(?i)<(\/?\w+)((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>")
  tagPos = {}
  indices = []
  links = {}
  for match in tagRegex.finditer(full_html):
    name = match.group(1).lower()
    value = (name, match.group(0), match.start(), match.end())
    indices.append(match.start())
    tagPos[match.start()] = value
    if name not in links.keys(): links[name] = [value]
    else: links[name].append(value)
  indices.sort()

  html = ""
  removed = ""
  tag = 'script'

  #def removeTags(tag, html):
  if tag not in links:
    return full_html
  tagCount = len(links[tag])#self.countStartTag('script')
  startTags = links[tag]
  stopTags = links[tag]

  lastStop = 0
  for start, stop in zip(startTags, stopTags):
    html += full_html[lastStop:start[2]]
    removed += full_html[start[2]:stop[3]]
    lastStop = stop[3]
  html += full_html[lastStop]

  #removeTags('script', html)

  #print('removed javascript:')
  #print(removed)
  return html


class  HTMLReader(HTMLParser):
  def __init__(self, url = '', debug = False, log = stdout, max_secs = 600):
    self.time = time.time() + max_secs
    self.doc = ''
    self.title = ''
    self.url = url
    self.in_body = False
    self.in_title = False
    self.in_script = 0
    self.in_style = False
    self.debug = debug
    if debug: 
      log.write("----\nURL  " + self.url)
      print(url)
    super().__init__()


  
  def handle_starttag(self, tag, attrs):
    
    if self.in_body:
      #if tag == 'br':
      if tag in {'br', 'p', 'ol', 'ul', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table'}:
        #print('start', tag)
        self.doc += '\n'
      else:
        self.doc += ' '
      if tag == "script":
        self.in_script += 1 
      if tag == "style":
        self.in_style = True

    elif tag == 'title':
      self.in_title = True

    elif tag == "body":
      self.in_body = True
      #print('inBody')
    #print('start',tag)

  def handle_endtag(self, tag):
    if self.in_body and self.in_script == 0 and not self.in_style:
      #if tag in {<br/> <br> </p> </ol> </ul> </hX> (X = 1-6) </table>}:
      if tag in {'br', 'p', 'ol', 'ul', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table'}:
        #print('end',tag)
        self.doc += '\n'
      else:
        self.doc += ' '

    if tag == "script":
      self.in_script -= 1 
      if tag == "style":
        self.in_style = False
    elif tag == 'title':
      self.in_title = False
      #print(self.title)
    elif tag == "body":
      self.in_body = False
    #print('end',tag)



  def handle_startendtag(self, tag, attrs):
    if self.in_body and self.in_script == 0 and not self.in_style:
      if tag == 'br':
        #print('/br')
        self.doc += '\n'
      else:
        self.doc += ' '

    #print('stend',tag)



  def handle_data(self, data):
    if self.in_body and self.in_script == 0 and not self.in_style:
      self.doc += data.strip()   
      if time.time() > self.time:
        log.write(' '.join(('\n', self.url, 'cut after' , str(time.time()-self.time), 'seconds\n\n')))

      if self.debug:
        with open('selfdoc.txt', 'a') as f:
          f.write(data.strip())
      #if self.debug:print(data.strip(),)   
      #print(data.strip())
    elif self.in_title:
      self.title += data.strip()

  def handle_charref(self, name):
    if self.in_body and self.in_script == 0 and not self.in_style:
      try:
        if name.startswith('x'):
          c = chr(int(name[1:],16))
        else:
          c = chr(int(name))
        self.doc += c
        #if self.debug: print(c)

      except Exception as e:
        print('char could not be recognized:')
        print(e)
        print('\t',self.url)

      #print('char:',name,c)

  def handle_entityref(self, name):
    #print('entity:',name, chr(name2codepoint[name]), entitydefs[name])
    if self.in_body and self.in_script == 0 and not self.in_style:
      try:
        ent = entitydefs[name] # '&' + name + ';'
        self.doc += ent # '&' + name + ';'
      except KeyError as e:
        #print('entitydefs KeyError', e)
        #print('\t', self.url)
        ent =  '&' + name + ';'
        self.doc += ent
      #if self.debug: print(ent)

def get_doc(url, log_f, debug = False):
  errors = ''
  with open(log_f, 'a') as log:
    #hr = HTMLReader()
    #hrTY = HTMLReader()
    hrMJ = HTMLReader(url, debug, log)
    #hr.url = hrTY.url = 
    #hrMJ.url = url
    req = urlreq.Request(url)
    browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'
    req.add_header('User-Agent', browser)
    html = ''
    try:
      with urlreq.urlopen(req,timeout = 10) as h:
        try:
          html = h.read().decode(errors='ignore')#.replace('\n','')#.replace("'",'"')
          if debug:
            with open('../res/Corpora/dog_developing_corp_22_docs/html.html','w') as f:
              f.write(html)
        except Exception as e:
          log.write('error while decoding:\n')
          log.write(str(e) + '\n')
          log.write('\t' + url + '\n')
          errors += 'decoding;'
        #print('1\n',html)
        #doesnt work: html = removeJavaScript(html) 
        '''
        try:
          hr.feed(html)
        except Exception as e:
          with open(log_f, 'a') as log:
            log.write('error while parsing html:\n')
            log.write(str(e) + '\n')
            log.write('\t' + url + '\n\n')
          #print('\n\n2\n',hr.title,'\n',hr.doc)

        xhtml = tidy(html)[0]
        #print('xhtml',xhtml)
        try:
          hrTY.feed(xhtml)
        except Exception as e:
          with open(log_f, 'a') as log:
            log.write('error while parsing xhtml:\n')
            log.write(str(e) + '\n')
            log.write('\t' + url + '\n\n')
          #print('\n\n2\n',hr.title,'\n',hr.doc)
        '''
        jhtml = remove_scriptstyle(html)
        if debug:
          with open('../res/Corpora/dog_developing_corp_22_docs/jhtml.html','w') as f:
            f.write(jhtml)

        try:
          hrMJ.feed(jhtml)
          if hrMJ.debug:
            print('done feeding')
        except Exception as e:
          log.write('error while parsing jhtml:\n')
          log.write(str(e) + '\n')
          log.write('\t' + url + '\n\n')
          #print('\n\n2\n',hr.title,'\n',hr.doc)
          errors += 'parsing;'
    except Exception as e:
      
        log.write('error while opening website:\n')
        log.write(str(e) + '\n')
        log.write('\t' + url + '\n')
        errors += 'opening;'
        print('raising')
        raise e
        #return('Website could not be opened','')
    return (hrMJ.title, remove_multiple_spaces(hrMJ.doc), errors)

def get_doc_section(url, queries):
  doc = get_doc(url)
  #look for smallest complete para(s)/sections including queries?
  # immer am stueck?
  



if __name__ == '__main__':
  url  = "http://www.ohmydogsupplies.com/dog-supplies/dog-bowls/"#"http://en.wikipedia.org/wiki/Dog_food"
  req = urlreq.Request(url)
  browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'
  req.add_header('User-Agent', browser)
  with urlreq.urlopen(req,timeout = 10) as h:
    html = h.read().decode(errors='ignore')#.replace('\n','')#.replace("'",'"')
    remove_scriptstyle(html)
      

  '''
  urls = {'http://dogdishdiet.com/2011/07/how-much-dry-food-should-i-feed-my-dog/',
          'http://en.wikipedia.org/wiki/XML'}
  for url in urls:
    with open('htmltextoutput.txt','w') as f:
      title, doc = get_doc(url,'webFuncLog.txt')
      f.write('\n\n  <title> ' + title + '</title>\n')
      f.write('  <body>\n' + doc + '\n  </body>\n')
  '''

  '''
  with open('DogFoodWikipedia.html') as w:
    hr = HTMLReader()
    html = w.read()
    hr.feed(html)
    hrJS = HTMLReader()
    htmlJS = removeJavaScript(html) 
    hrJS.feed(htmlJS)
  with open('DogFoodText.txt','w') as f:
    f.write(hr.doc)
  with open('DogFoodTextJavaRemove.txt','w') as f:
    f.write(hrJS.doc)
  '''





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
