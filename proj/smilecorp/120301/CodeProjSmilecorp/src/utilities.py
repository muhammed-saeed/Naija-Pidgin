import time
from sys import argv, stdout, path
import re

def timestamp():
  return time.strftime('%Y-%m-%d-%H:%M')

path.insert(0, './modules/')


def ent_repl(mo):
  repl =  ('&' + {'<':'lt','>':'gt','&':'amp','"':'quot',
            "'":'apos'}[mo.group(0)] + ';')
  #print('replaced', mo.group(), 'with', repl)
  return repl

def insertXMLEnt(strng):
  return re.sub('[<>"&'+"']", #|(&(?!(quot|amp|lt|gt|apo);))",
          ent_repl,strng)








