import os.path
import os
from shutil import rmtree
import shelve

from utilities import *

import createQueries as cQ
import bingFunctions as bF
import webFunctions as wF



'''
 start with dog feed example
get vo pairs
 put search strings in file
 get urls for all these
write in file? shelf?
get docs for all urls
  id counting, structure http://lcaro.wikidot.com/corpus-xml
  write in xml file
    header and footer
'''

def  _file_operations(args):
  pass

def  _get_url_shelves(args):
  pass

def _make_docs_full(urls,results,snippets,corpus_name, corpus_f,log_f):
  pass

def _make_docs_mini(amount,urls,results,snippets,corpus_name, corpus_f,log_f):
  pass

def _make_mini_make_doc(amount):
  print('mini',amount)
  def ret_func(*args):
    return _make_docs_mini(amount, *args)
  return ret_func

def _make_docs_best_scored(urls,results,snippets,corpus_name, corpus_f,log_f):
  pass


#def build_corpus(scen, corpus_name, new_urls = True, new_qs = False):
def build_corpus(corpus_name, scen_id, scen, scen_long, scen_short, scen_par = None, 
                                    new_urls = True, new_qs = False, flag = 'full'):
  
  print('Writing corpus named', corpus_name, 'for', scen, 'scenario; flag:', flag)

  if flag.startswith('mini'):
    make_docs = _make_mini_make_doc(int(flag[4:]))
  else:
    make_docs = _make_docs_full
  #scen = scen.replace(' ', '_')
  #scen_short = scen_short.replace(' ', '_')
  #scen_par = scen_par.replace(' ', '_')

  corpus_f = '../res/Corpora/' + corpus_name + '_corpus.xml'
  log_f = '../res/Corpora/' + corpus_name + '_log.txt'
  doc_dir = '../res/Corpora/' + corpus_name + '_docs'
  query_f = '../res/Queries/' + scen_long +'_queries.txt' 
  url_dir = '../res/Corpora/' + corpus_name + '_urls'

  new_qs = new_qs or not os.path.isfile(query_f)
  new_urls = new_urls or new_qs or not os.path.isfile(url_dir + '/urls.db')
  print('new queries:', new_qs, (' ' if new_qs and os.path.isfile(query_f) else ' not ') + 'overwriting',query_f)
  print('new urlshelves:', new_urls, (' ' if new_urls and os.path.exists(url_dir) else ' not ') + 'overwriting', url_dir)

  #TODO make function _file_operations(..)
  if os.path.isfile(corpus_f) or os.path.exists(doc_dir):
    if not input('A corpus named ' + corpus_name + 
        ' already exists.\nDo you want to overwrite it?\n') == 'yes':
      raise Exception('Cannot continue without overwriting an existing corpus file.')

    #corpus file will just be overwritten later
    #os.rmdir(doc_dir)
    if os.path.exists(doc_dir):
      rmtree(doc_dir)

  with open(log_f, 'w') as log:
    log.write(timestamp() + ' \n\n')


  if new_urls:
    if os.path.exists(url_dir):
      rmtree(url_dir)
    if not os.path.exists(url_dir):
      os.mkdir(url_dir)
    else:
      raise Exception('Cannot continue without overwriting an existing url directory.')
    
  '''
  if os.path.isfile(urlshelve_name + '.db') and new_urls:
    os.remove(urlshelve_name + '.db')
  if os.path.isfile(urlshelve_name + '_queries.db') and new_urls:
    os.remove(urlshelve_name + '_queries.db')
  if os.path.isfile(urlshelve_name + '_snippets0.db') and new_urls:
    i_sn = 0
    while True:
      try:
        os.remove(urlshelve_name + '_snippets' + str(i_sn) + '.db')
        i_sn += 1
      except OSError as e:
        break
  '''

  if not os.path.exists(doc_dir):
    os.mkdir(doc_dir)
  else:
    raise Exception('Cannot continue without overwriting an existing corpus directory.')
  #til here

  #TODO make function _get_url_shelves(args*)
  if new_qs:
    cQ.createQueries(scen_long, scen_short, query_f, scen_par)
  
  #TODO score queries


  #urls = bF.get_URL_dict(query_f, 10, log_f) 
  if new_urls:
    bF.make_URL_shelves(query_f, url_dir, 250, log_f)#TODO 250 
  urls = shelve.open(url_dir + '/urls', 'r') 
  results = shelve.open(url_dir + '/results', 'r')  
  snippets = [shelve.open(url_dir + '/snippets0', 'r')]
  sn_no = 0

  while True:
    #print(sn_no)
    sn_no += 1
    if os.path.isfile(url_dir + '/snippets'+str(sn_no)+'.db'):
      snippets.append(shelve.open(url_dir + '/snippets' + str(sn_no), 'r'))
    else:
      break
  #til here 
  #urls, results, snippets =  _get_url_shelves(args*)

  print(len(urls), 'URLs gefunden.\n\n')
  #with open(scen + '_urls.txt','w') as uf:
  #  for u in urls:
  #    uf.write('\t'.join([str(len(urls[u])), u] + [q for q in urls[u]]) + '\n')



  with open(corpus_f,'w') as c:
    c.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n\t',
        '<corpus eventid="', scen_id,#'1234', #TODO how get eventid, as function param
        #'" scenario="feed a pet dog" short="dog" time="', timestamp(), 
        '" scenario="' + scen + '" short="' + scen_short.replace('_',' ') +
        '" time="', timestamp(), '" potential_queries="', query_f, '">\n')))


  #TODO make function _make_docs(urls,results,snippets,corpus_name, corpus_f,log_f)
  doc_no = 0
  url_no = 0
  n_succ = n_tot = n_ish = n_perf = 0
  for url in urls:
    n_supp = str(len(urls[url]))
    url_no += 1
    try:
      title, body, errors = wF.get_doc(url,log_f)
    except Exception as e:
      #raise e
      with open(log_f,'a') as log:
        log.write(''.join(('Document at URL: ',url,
            ' could not be retrieved due to ',type(e).__name__,' : ', str(e),
            '\nIt was found by these queries: \n  ', str(urls[url]),'\n\n')))
      continue
    body =  insertXMLEnt(body.strip())
    title =  insertXMLEnt(title)
    if body:
      n_ish += 1
      if len(body) > 20:
        #print(timestamp(),'len',len(body))
        n_succ += 1
      if errors == '':
        n_perf += 1
    n_tot += 1
    if not body:
      continue
  
    doc_no += 1
      
    doc_id = str(doc_no).zfill(6)
    '''
    with open(comp_f,'a') as c:
      c.write(doc_id + ' ' + url)
      for txt in body:
        c.write('\t')
        c.write(txt)
      c.write('\n')
    '''
    doc_file = corpus_name + '_docs/' + doc_id + '.xml'
    with open(corpus_f,'a') as c:
      c.write(''.join(('\n\t\t<document id="', doc_id,'" url="', insertXMLEnt(url),'" time="',
                  timestamp(),'" support="',n_supp,'" title="', title, '" file="',
                    insertXMLEnt(doc_file),'">\n')))

      c.write('\t\t</document>\n')
    
    with open('../res/Corpora/' +  insertXMLEnt(doc_file),'w') as d:
      d.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                  '\n<document id="doc', doc_id,'" url="', insertXMLEnt(url),'" time="', 
                  timestamp(),'" support="',n_supp,'" title="',title,'">\n')))

      d_snippet = ''
      for q_id, b_rank in results[urls[url]]:
        sn_no = int(int(urls[url])/10000)
        #print(sn_no)
        snippet = snippets[sn_no][urls[url]+' '+q_id]
        if (not d_snippet) and snippet.strip():
          d_snippet = snippet
        #TODO take best ranked query snippet
        d.write(''.join(('\t\t\t<query id="', q_id,'" bing-rank="',str(b_rank),'"/>\n')))
      d.write(''.join(('\t<description>', d_snippet, '</description>\n',
                  '\t<body>\n\t\t',body,'\n\t</body>\n</document>\n')))
      
    if flag.startswith('mini'):
      print('mini, break')
      break
    else:
      print('not mini')
      break
    if (url_no)  % 1000 == 0:
      print(timestamp())
      print('no probs:',n_perf,'/',n_tot,float(n_perf)/n_tot)
      print('>20chars:',n_succ,'/',n_tot,float(n_succ)/n_tot)
      print('non-empty:',n_ish,'/',n_tot,float(n_ish)/n_tot)
      print(url_no)
      print('-------')
      #break
  #til here:
  #make_docs(urls,results,snippets,corpus_name, corpus_f,log_f)
  urls.close()
  results.close()
  for sn in snippets:
    sn.close()



  with open(corpus_f,'a') as c:
    c.write('\n</corpus>')

  #TODO score corpus documents




def get_all_corpora_gen(new_urls = True, new_qs = False, flag = 'mini1'):
  #TODO flags: mini+int, random urls, list url ids
              # scored best n
  shorts = ["fast_food","food_back","laundry","coffee","dog", "microwave",
                            "credit_card","vending_machine","letter","shower"]      
  ids = [2, 3 ,56, 111, 66 , 92, 11, 31, 101, 14]
  not_so_shorts = ["fast food restaurant", "send food back", "do laundry", 
                                     "make coffee", "feed a dog", #"phone", "iron",
                                    "heat sth in microwave", "pay w credit card", 
                                    "buy f vending machine", "mail a letter", "take a shower"]
  longs = ['eat_in_fast_food_restaurant_GOOD',#_filtered', 
              'send_food_back_filtered', 
              'do_laundry', 'make_coffee', 'feed_a_pet_dog', 'heat_food_in_microwave', 
              'pay_with_credit_card_filtered', 
              'buy_from_vending_machine', 
              'mail_a_letter', 'take_a_shower_filtered'] 
  scenarios = ['eat in fast food restaurant',# filtered', 
              'send food back', 
              'do laundry', 'make coffee', 'feed a pet dog', 'heat food in microwave', 
              'pay with credit card', 
              'buy from vending machine', 
              'mail a letter', 'take a shower'] 
  participants = ['fast food restaurant',
                  'food', 'laundry', 'coffee', 'dog', 'microwave', 
                  'credit card', 'vending machine', 
                  'letter', 'shower'] 


  for i in range(len(scenarios)):
    yield 'will create ' + scenarios[i]
    #print('name',scenarios[i] + '_eval', '; id',ids[i], '; scen',scenarios[i], '; short',shorts[i], '; par',participants[i])
    build_corpus(scenarios[i] + '_eval', ids[i],  scenarios[i], longs[i], shorts[i], 
                  participants[i], new_urls, new_qs, flag)
    yield 'created' + scenarios[i]

  yield 'created all ' + len(scenarios) + ' corpora'
  return







if __name__ == '__main__':
  nq = True if '-q' in argv else False
  nu = True if '-u' in argv else False
  if '-m' in argv:
    build_corpus('trial_muell_dog',  '66', 'feed a pet dog', 'feed_a_pet_dog', 
                  'feed_dog', 'dog', nu, nq, 'mini3')
  else:
    #build_corpus('dog_developing_corp_march_1', '66', 'feed_a_pet_dog', 
    #              'feed_dog', 'dog', nu, nq)
    for message in get_all_corpora_gen(nu,nq):
      if input(message + '\n') == 'stop':
        break


#TODO copy shelve!!!!!!!!

  
