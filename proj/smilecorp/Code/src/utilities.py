import time
from sys import argv, stdout, path
import re
import shelve
from contextlib import closing
import urllib.request

path.insert(0, './modules/')

def timestamp():
  return time.strftime('%Y-%m-%d-%H:%M')

def countdown(n = 10):
  for i in range(n,0,-1):
    print('\r',i,end='')
    time.sleep(1)
  print('\r')

def wait_a_bit():
  print('Waiting for a minute...')
  time.sleep(60)

def ent_repl(mo):
  repl =  ('&' + {'<':'lt','>':'gt','&':'amp','"':'quot',
            "'":'apos'}[mo.group(0)] + ';')
  #print('replaced', mo.group(), 'with', repl)
  return repl

def insertXMLEnt(strng):
  return re.sub('[<>"&'+"']", #|(&(?!(quot|amp|lt|gt|apo);))",
          ent_repl,strng)

def ask_yes_no(strng):
  go_on = input(strng)
  while True:
    if go_on in {'y','yes','Y'}:
      return True
    if go_on in {'n','no','N'}:
      return False
    else:
      go_on = input('Try y or n. ')

def check_connectivity(reference):
    #http://stackoverflow.com/questions/3764291/checking-network-connection
    try:
        f = urllib.request.urlopen(reference)#, timeout=3)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False

   




