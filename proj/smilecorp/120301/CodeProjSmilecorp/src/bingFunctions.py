from utilities import *

import shelve
#from sys import stdout
from bingapi import Bing
app_id = '7977945912BDC64D968333DD9B3053001E4395AB'
import createQueries as cQ
import readMsFiles as M
from DefaultDict import DD

bing = Bing(app_id, timeout = 3)


def bingCount(inpf, outf):
  currentGC = None
  with open(inpf) as inp:
    with open(outf,'w') as out:
      for line in inp:
        #line = line.strip()
        if not line:  continue
  
        if '\t' in line:
          #in case i want to compare to googleCount which is already there
          #and expected to be in the beginning of the line followed by a tab
          lineSplit = line.split('\t')
          if len(lineSplit) > 2:
            print('strange line: ' + line)
          l = lineSplit[1]

          #fixes bug in googleCounts
          if lineSplit[0] == currentGC or lineSplit[0] == '':
            lineSplit[0] = '0'
          else:
            currentGC = lineSplit[0]

        else:
          l = line
          lineSplit = [l]
  
        result = bing.do_web_search(l, extra_args={'web.count':1})
        try:
          n = result['SearchResponse']['Web']['Total'] 
          n = str(n)
        except Exception as e:
          print(e)
        out.write(n + '\t' + '\t'.join(lineSplit))



def get_URL_gen(query, n = 50, log_f = stdout):
  bing_rank = 0
  if n > 250:
    n = 250
  #funktion statt generator:resultURLs = []
  offset = 0
  if n <= 50:
    if n < 1: 
      print('get URL gen called with invalid amount of results', str(n),'\n set to 1')
      n = 1
    nS = 0 #number of searches -1
    lastN = n
  else:
    nS = int(n / 50)
    lastN = n % 50
  #print('n=',n,'nS =',nS, 'last n =', lastN)

  for i in range(nS):
    try:
      response = (bing.do_web_search(query, extra_args={'web.count':50, 
        'web.offset':offset}) if offset > 1 else  
        bing.do_web_search(query, extra_args={'web.count':50}))
    except Exception as e:
      with open(log_f,'a') as log:
        log.write(' '.join(('in get URL gen:\n', query, type(e).__name__, 
                    str(e), '\n\n')))
      break
    #if offset < 50: 
    #  print('Total amount of results:',response['SearchResponse']['Web']['Total']) 
    #print('off',offset)
    offset += 50
    try:
      if response['SearchResponse']['Web']['Total'] > 0:
        for result in response['SearchResponse']['Web']['Results']:
          #resultURLs.append(result['Url'])
          bing_rank += 1
          yield (result['Url'], bing_rank)
        #print('off',offset)
      else:
        break
    except Exception as e:
      log.write(str(e) + '\n ')
      log.write(str(response) + '\n\n')

  if lastN == 0: return

  try:
    response = bing.do_web_search(query, extra_args={'web.count':lastN, 
    'web.offset':offset})

  except Exception as e:
    with open(log_f,'a') as log:
      log.write(' '.join(('in get URL gen:\n', query, type(e).__name__, 
                    str(e), '\n\n')))
    return

  #print('o:',offset, 'lastN', lastN)
  #print('Total amount of results:',response['SearchResponse']['Web']['Total']) 
  #print(query)
  #print(response)
  if response['SearchResponse']['Web']['Total'] > 0:
    for result in response['SearchResponse']['Web']['Results']:
      #resultURLs.append(result['Url'])
      bing_rank += 1
      yield (result['Url'],bing_rank)
      
  return #resultURLs


def get_URL_dict(query_f, n = 50, log_f = stdout):
  urls = DD(set)
  #if isinstance(queries, str):
  #  pass 
  #read query file for this name
  #open file, call fNRUs, integrate in dict while counting occurences per url
  #for query in queries:#??
  with open(query_f) as qf:
    print('queries processed:')
    i = 0
    qf.readline() #first line with column names
    for line in qf:
      i += 1
      print('\r', i,end= '')
      q_tup = line.strip().split('\t')
      query = ''.join(('"', q_tup[2], '" "near:5" "', '" "'.join(q_tup[3:6]), '"'))
        # must be "s around near:x, else 0 results
      #print('q',query)
      res_Us = get_URL_gen(query, n, log_f)
      for res in res_Us:
        #print('res',res)
        res_U, b_rank = res
        urls[res_U].add((q_tup[0], b_rank)) #q_id
  print('\n')
  return urls


def make_URL_shelve(query_f, us_f, n = 50, log_f = stdout):
  urls = shelve.open(us_f)  
  #if isinstance(queries, str):
  #  pass 
  #read query file for this name
  #open file, call fNRUs, integrate in dict while counting occurences per url
  #for query in queries:#??
  with open(query_f) as qf:
    print('queries processed:')
    i = 0
    qf.readline() #first line with column names
    for line in qf:
      i += 1
      print('\r', i,end= '')
      q_tup = line.strip().split('\t')
      query = ''.join(('"', q_tup[2], '" "near:5" "', '" "'.join(q_tup[3:6]), '"'))
        # must be "s around near:x, else 0 results
      #print('q',query)
      res_Us = get_URL_gen(query, n, log_f)
      for res in res_Us:
        #print('res',res)
        res_U, b_rank = res
        if res_U in urls:
          val = urls[res_U]
          val.add((q_tup[0], b_rank)) #q_id
          urls[res_U] = val
        else:
          val = set()
          val.add((q_tup[0], b_rank)) #q_id
          urls[res_U] = val
  urls.close()
  print('\n')
  return(us_f)



