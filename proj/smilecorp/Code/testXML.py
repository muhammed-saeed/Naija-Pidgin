import xml.sax as sax
from xml.sax import SAXParseException
import os
from sys import argv

class Document():
  def __init__(self):
    self.queries = []
    self.description = ""
    self.body = ""
    
  def addQuery(self,id,rank):
    self.queries.append((id,rank))
    
  def setBody(self,body):
    self.body = body
    
  def setDescription(self,description):
    self.description = description
    
  def getQueries(self):
    return self.queries
    
  def getBody(self):
    return self.body
    
  def getDescription(self):
    return self.description

class DocumentHandler(sax.handler.ContentHandler):

  def __init__(self): 
    self.document = Document()
    self.tempText = ""
    
  def startElement(self, name, attrs): 
    if name == 'query':
      self.document.addQuery(attrs['id'],int(attrs['bing-rank']))
    elif name == 'description':
      self.tempText = ""
    elif name == 'body':
      self.tempText = ""
      
  def endElement(self, name): 
    if name == "description": 
      self.document.setDescription(self.tempText)
    elif name == "body": 
      self.document.setBody(self.tempText)

def createDocumentFromFile(inputFile):
  iobj = open(inputFile,"r")  
  
  handler = DocumentHandler() 
  parser = sax.make_parser() 
  parser.setContentHandler(handler) 
  parser.parse(inputFile)
  document = handler.document
  
  iobj.close()
  return document
  
def main():
  
  folder = "dog_developing_corp_march_docs/" 
  output = "existingXMLErrors.txt"
  oobj = open(output,"w")
  if len(argv) <= 1:
    listing = os.listdir(folder)
    for infile in listing:
      if infile[-4:]  != '.xml':
        continue
      try:
        createDocumentFromFile(folder+infile)
      except SAXParseException, message:
        oobj.write(infile)
        oobj.write(" - ")
        oobj.write(message.__str__())
        oobj.write("\n")
      except Exception as e:
        oobj.write(folder+infile)
        oobj.write(" did not work due to: ")
        oobj.write(str(e))
        oobj.write("\n")

  else:
    listing = []
    for folder in argv[1:]:
      if folder[-1] != '/':
        folder += '/'
      listing = os.listdir(folder)
      for infile in listing:
        if infile[-4:] != '.xml':
          continue
        try:
          createDocumentFromFile(folder+infile)
        except SAXParseException, message:
          oobj.write(infile)
          oobj.write(" - ")
          oobj.write(message.__str__())
          oobj.write("\n")
        except Exception as e:
          oobj.write(folder+infile)
          oobj.write(" did not work due to: ")
          oobj.write(str(e))
          oobj.write("\n")
        


    
  oobj.close()
  return 0

if __name__ == '__main__':
  main()
