from utilities import *

import os.path
import os
from shutil import rmtree
from random import sample


import createQueries as cQ
import scoreQueries as sQ
import scoreDocs as sD
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

def _make_id_to_urls(url_dir):
  with closing(shelve.open(url_dir + '/urls', 'r')) as urls:
    with closing(shelve.open(url_dir + '/id_to_urls')) as ids:
      for url in urls:
        ids[urls[url]] = url


def  _file_operations(corpus_f, corpus_name, doc_dir, new_qs, query_f, new_urls, url_dir, log_f):
  new_qs = False#new_qs or not os.path.isfile(query_f)
  new_urls = False#new_urls or new_qs or not (os.path.isfile(url_dir + '/urls.db') and
      #os.path.isfile(url_dir + '/results0.db') and os.path.isfile(url_dir + '/snippets0.db'))
  print('new queries:', new_qs, (' ' if new_qs and os.path.isfile(query_f) else 
        ' not ') + 'overwriting',query_f)
  print('new urlshelves:', new_urls, (' ' if new_urls and 
        os.path.exists(url_dir) else ' not ') + 'overwriting', url_dir)

  # make function _file_operations(..)
  if os.path.isfile(corpus_f) or os.path.exists(doc_dir):
    #TODO wieder hin: if not ask_yes_no('A corpus named ' + corpus_name + 
    #    ' already exists.\nDo you want to overwrite it? '):
    #  raise Exception('Cannot continue without overwriting an existing corpus file.')
    print('A corpus named ' + corpus_name + ' already exists.\nIt gets overwritten if you do not interrupt.')
    try:
      #time.sleep(5)
      countdown(5)
    except KeyboardInterrupt as e:
      print('interrupted.')
      raise e



    #corpus file will just be overwritten later
    #os.rmdir(doc_dir)
    if os.path.exists(doc_dir):
      rmtree(doc_dir)
  elif '/' in corpus_name:
    corp_dirs = [d for d in corpus_name.split('/')[:-1]]
    for i in range(len(corp_dirs)):
      nd = '../res/Corpora/' + '/'.join(corp_dirs[:i+1])
      if not os.path.exists(nd):
        os.mkdir(nd)

  with open(log_f, 'w') as log:
    log.write(timestamp() + ' \n\n')


  if new_urls:
    if os.path.exists(url_dir):
      rmtree(url_dir)
    if not os.path.exists(url_dir):
      os.mkdir(url_dir)
    else:
      raise Exception('Cannot continue without overwriting an existing url directory.')
    
  if not os.path.exists(doc_dir):
    os.mkdir(doc_dir)
  else:
    raise Exception('Cannot continue without overwriting an existing corpus directory.')
  return new_qs, new_urls


def  _get_url_shelves(new_qs, new_urls, url_dir, scen_long, scen_short, scen_par, 
                      query_f, log_f):
 # make function _get_url_shelves(args*)
  if new_qs:
    raise Exception('no new queries please')
    cQ.createQueries(scen_long, scen_short, query_f, scen_par)
  
  #TODO score queries
  scored_query_f = query_f[:-4] + '_scored' + query_f[-4:]
  if new_qs or not os.path.isfile(scored_query_f):
    if not scored_query_f == sQ.score_queries(query_f, scen_long):
      print('''something is wrong with the scored query file name 
              in buildCorpus vs scoreQueries''')
    scored_query_f  = sQ.score_queries(query_f, scen_long)

  #urls = bF.get_URL_dict(query_f, 10, log_f) 
  if new_urls:
    bF.make_URL_shelves(query_f, url_dir, 250, log_f)#250 

  #TODO score urls
  if new_urls or not os.path.isfile(url_dir + '/url_scores.db'):#or .db?
    sD.make_url_scores(url_dir, scored_query_f)


  urls = shelve.open(url_dir + '/urls', 'r') 
  results = [shelve.open(url_dir + '/results0', 'r')]
  rs_no = 0
  while True:
    #print(rs_no)
    rs_no += 1
    if os.path.isfile(url_dir + '/results'+str(rs_no)+'.db'):
      results.append(shelve.open(url_dir + '/results' + str(rs_no), 'r'))
    else:
      break
  snippets = [shelve.open(url_dir + '/snippets0', 'r')]
  sn_no = 0
  while True:
    #print(sn_no)
    sn_no += 1
    if os.path.isfile(url_dir + '/snippets'+str(sn_no)+'.db'):
      snippets.append(shelve.open(url_dir + '/snippets' + str(sn_no), 'r'))
    else:
      break

  try:
    with closing(shelve.open(url_dir + '/query_scores', 'r')) as q_scores:
      if len(q_scores) == 0:
        raise Exception
  except:
    #if not isfile(url_dir + '/query_scores.db'):
    with open(scored_query_f) as scored_queries:
      scored_queries.readline()
      with closing(shelve.open(url_dir + '/query_scores')) as q_scores:
        for line in scored_queries:
          q = line.split('\t')
          q_scores[q[0]] = float(q[1])

  return urls, results, snippets, scored_query_f


def _make_doc(counters, url, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f,log_f):
  doc_no, url_no, n_perf, n_succ,n_ish, n_tot = counters
  #print('doc no', doc_no, 'url_no', url_no)
  url_id = urls[url]
  sn_no = bF.get_sn_no(url_id, other_one = ('do_laundry' in corpus_name))#int(int(url_id)/10000)
  rs_no = bF.get_rs_no(url_id, other_one = ('do_laundry' in corpus_name))#int(int(url_id)/5000)#10000)#20000
  snippet_s = snippets[sn_no]
  result_s = results[rs_no]
  n_supp = str(len(result_s[url_id]))
  try:
    score = url_scores[url_id]
  except Exception as e:
    print('l.158 score=url_scores[url_id]', url_id)
    print(e)
    score = 0.0
  url_no += 1
  try:
    #only continues when internet connection is available (checks google)
    while check_connectivity('http://www.google.com') == False:
      print('Internet is off',timestamp())
      wait_a_bit()

    title, body, errors = wF.get_doc(url,log_f)
  except Exception as e:
    #raise e
    with open(log_f,'a') as log:
      log.write(''.join(('Document at URL: ',url,
          ' could not be retrieved due to ',type(e).__name__,' : ', str(e),
          '\nIt was found by these queries: \n  ', str(url_id),'\n\n')))
    #continue
    return doc_no, url_no, n_perf, n_succ,n_ish, n_tot

  bingtitle = titles[url_id]
  body =  insertXMLEnt(body.strip())
  title =  insertXMLEnt(title)
  bingtitle =  insertXMLEnt(bingtitle)
  if body:
    n_ish += 1
    if len(body) > 20:
      n_succ += 1
    if errors == '':
      n_perf += 1
  else:
    #continue
    return doc_no, url_no, n_perf, n_succ,n_ish, n_tot + 1
  n_tot += 1

  doc_no += 1
    
  doc_id = str(doc_no).zfill(7)
  doc_file = corpus_name + '_docs/' + doc_id + '.xml'
  with open(corpus_f,'a') as c:
    c.write(''.join(('\n\t\t<document id="', doc_id, '" url="', insertXMLEnt(url),
      '" time="', timestamp(), '" support="', n_supp,'" score="', str(score),
      '" bingtitle="', bingtitle, '" webtitle="', title, 
      '" file="', insertXMLEnt(doc_file),'">\n')))

    c.write('\t\t</document>\n')
  
  with open('../res/Corpora/' +  insertXMLEnt(doc_file), 'w') as d:
    d.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', 
      '\n<document id="doc', doc_id, '" url="', insertXMLEnt(url), '" time="', 
      timestamp(), '" support="', n_supp, '" score="', str(score), 
      '" bingtitle="', bingtitle, '" webtitle="', title, '">\n')))

    d_snippet = ('',0.0)
    for q_id, b_rank in result_s[url_id]:
      #print(sn_no)
      snippet = snippet_s[url_id + ' ' + q_id]
      if snippet.strip() and (not d_snippet[0]):#erase last part
        #todo take best ranked query snippet
        q_score = float(q_scores[q_id])
        if q_score > d_snippet[1]:
          d_snippet = (insertXMLEnt(snippet), q_score)
      d.write(''.join(('\t\t\t<query id="', q_id,'" bing-rank="',str(b_rank),'"/>\n')))
    d.write(''.join(('\t<description>', d_snippet[0], '</description>\n',
                '\t<body>\n\t\t',body,'\n\t</body>\n</document>\n')))
      

  return doc_no, url_no, n_perf, n_succ,n_ish, n_tot


#def _make_just_one_doc(url, url_id = '0', log_f = './make_just_one_doc.log.txt'):
#  snippet =
#  try:
#    title, body, errors = wF.get_doc(url,log_f)
#  except Exception as e:
#    #raise e
#    with open(log_f,'a') as log:
#      log.write(''.join(('Document at URL: ',url,
#          ' could not be retrieved due to ',type(e).__name__,' : ', str(e),
#          '\nIt was found by these queries: \n  ', str(url_id),'\n\n')))
#    #continue
#    return 
#
#  bingtitle = titles[url_id]
#  body =  insertXMLEnt(body.strip())
#  title =  insertXMLEnt(title)
#  bingtitle =  insertXMLEnt(bingtitle)
#  if not body:
#    return 
#    
#  doc_id = url_id
#  doc_file = corpus_name + '_docs/' + doc_id + '.xml'
#  with open(corpus_f,'a') as c:
#    c.write(''.join(('\n\t\t<document id="', doc_id, '" url="', insertXMLEnt(url),
#      '" time="', timestamp(), '" support="', n_supp,'" score="', str(score),
#      '" bingtitle="', bingtitle, '" webtitle="', title, 
#      '" file="', insertXMLEnt(doc_file),'">\n')))
#
#    c.write('\t\t</document>\n')
#  
#  with open('../res/Corpora/' +  insertXMLEnt(doc_file), 'w') as d:
#    d.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', 
#      '\n<document id="doc', doc_id, '" url="', insertXMLEnt(url), '" time="', 
#      timestamp(), '" support="', n_supp, '" score="', str(score), 
#      '" bingtitle="', bingtitle, '" webtitle="', title, '">\n')))
#
#    d_snippet = ('',0.0)
#    for q_id, b_rank in result_s[url_id]:
#      #print(sn_no)
#      snippet = snippet_s[url_id + ' ' + q_id]
#      if snippet.strip() and (not d_snippet[0]):#erase last part
#        #todo take best ranked query snippet
#        q_score = float(q_scores[q_id])
#        if q_score > d_snippet[1]:
#          d_snippet = (insertXMLEnt(snippet), q_score)
#      d.write(''.join(('\t\t\t<query id="', q_id,'" bing-rank="',str(b_rank),'"/>\n')))
#    d.write(''.join(('\t<description>', d_snippet[0], '</description>\n',
#                '\t<body>\n\t\t',body,'\n\t</body>\n</document>\n')))
#
#    return ???

#def _make_docs_full(urls,results,snippets,corpus_name, corpus_f,log_f):
def _make_docs_full(urls, results, snippets, titles, q_scores, url_scores, 
                    corpus_name, corpus_f, log_f):
  # make function _make_docs(urls,results,snippets,corpus_name, corpus_f,log_f)
  doc_no = 0
  url_no = 0
  n_succ = n_tot = n_ish = n_perf = 0
  for url in urls:
    counters = doc_no, url_no, n_perf, n_succ,n_ish, n_tot
    #nc = _make_doc(counters, url, urls,results,snippets,corpus_name, corpus_f,log_f)
    nc = _make_doc(counters, url, urls, results, snippets, titles, q_scores, 
                    url_scores, corpus_name, corpus_f,log_f)
    doc_no, url_no, n_perf, n_succ,n_ish, n_tot = nc

    if (url_no)  % 1000 == 0:
      print(timestamp())
      print(url_no)
      print('no probs:',n_perf,'/',n_tot,float(n_perf)/n_tot)
      print('>20chars:',n_succ,'/',n_tot,float(n_succ)/n_tot)
      print('non-empty:',n_ish,'/',n_tot,float(n_ish)/n_tot)
      print(url_no)
      print('-------')

  print(timestamp())
  print('no probs:',n_perf,'/',n_tot,float(n_perf)/n_tot)
  print('>20chars:',n_succ,'/',n_tot,float(n_succ)/n_tot)
  print('non-empty:',n_ish,'/',n_tot,float(n_ish)/n_tot)
  print(url_no)
  print('')



def _make_docs_mini(amount, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f, given_urls = None, skip = 0):
  # make function _make_docs(urls,results,snippets,corpus_name, corpus_f,log_f)
  doc_no = 0
  url_no = 0
  n_succ = n_tot = n_ish = n_perf = 0
  used_urls = []
  if given_urls is None:
    given_urls = urls
  for url in given_urls:
    counters = doc_no + skip, url_no, n_perf, n_succ,n_ish, n_tot
    old_doc_no = doc_no
    nc = _make_doc(counters, url, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f)
    doc_no_skip, url_no, n_perf, n_succ,n_ish, n_tot = nc
    doc_no = doc_no_skip - skip
    if old_doc_no + 1 == doc_no:
      used_urls.append(url)
    if (doc_no) == amount:
      break

  if used_urls:
    print('\n',timestamp())
    print('no probs:',n_perf,'/',n_tot,float(n_perf)/n_tot)
    print('>20chars:',n_succ,'/',n_tot,float(n_succ)/n_tot)
    print('non-empty:',n_ish,'/',n_tot,float(n_ish)/n_tot)
    print(url_no)
    print('')
  if not len(used_urls) == amount:
    print('something went wrong,', len(used_urls), '== len(used_urls) != amount ==',amount)
  return used_urls

def _make_docs_random(amount, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f, out_urls = None, skip = None):
  if out_urls is None:
    given_urls = sample([x for x in urls.keys()], 2 * amount)
  else:
  #random twice amount urls, so half of them can go wrong
    given_urls = sample([x for x in urls.keys() if not x in out_urls], 2 * amount)
  #print('given urls',given_urls)
  used_urls = _make_docs_mini(amount, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f, given_urls, skip)
  return used_urls

def _make_docs_best(amount, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f):
  given_urls = []
  # best 2*amount scored urls

  sorted_urls = sorted([(url_id,url_scores[url_id]) for url_id in url_scores], key = lambda x: -float(x[1]))
  #hopefully works, different if too big to sort that way

  try:
    id_urls = shelve.open('../res/Corpora/' + corpus_name + '_urls/id_to_urls','r')
    if len(id_urls) == 0:
      id_urls.close()
      raise Exception
  except:
    _make_id_to_urls('../res/Corpora/' + corpus_name + '_urls')
    id_urls = shelve.open('../res/Corpora/' + corpus_name + '_urls/id_to_urls','r')

  given_urls = [id_urls[p[0]] for p in sorted_urls[:2*amount]]
  id_urls.close()
  used_urls = _make_docs_mini(amount, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f, given_urls)
  return used_urls

def _make_docs_eval(urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f):
  out_urls =  _make_docs_best(12, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f)
  print('made best 12')
  random_urls =_make_docs_random(12, urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f, out_urls, skip = 12)
  print('made random 12')
  return out_urls + random_urls

def _make_mini_make_docs(amount):
  #print('mini',amount)
  def ret_func(*args):
    return _make_docs_mini(amount, *args)
  return ret_func

def _make_best_make_docs(amount):
  print('best',amount)
  def ret_func(*args):
    return _make_docs_best(amount, *args)
  return ret_func

def _make_random_make_docs(amount):
  print('random',amount)
  def ret_func(*args):
    return _make_docs_random(amount, *args)
  return ret_func



#def build_corpus(scen, corpus_name, new_urls = True, new_qs = False):
def build_corpus(corpus_name, scen_id, scen, scen_long, scen_short, scen_par = None, 
                                    new_urls = True, new_qs = False, flag = 'full'):

  print('Writing corpus named', corpus_name, 'for', scen, 'scenario; flag:', flag)

  if flag.startswith('mini'):
    make_docs = _make_mini_make_docs(int(flag[4:]))
  elif flag == 'full':
    make_docs = _make_docs_full
  elif flag == 'eval':
    make_docs = _make_docs_eval
  elif flag.startswith('best'):
    make_docs = _make_best_make_docs(int(flag[4:]))
  elif flag.startswith('random'):
    make_docs = _make_random_make_docs(int(flag[6:]))
  else:
    print('Did not recognize flag, will create mini corpus.')
    make_docs = _make_mini_make_docs(1)
  #scen = scen.replace(' ', '_')
  #scen_short = scen_short.replace(' ', '_')
  #scen_par = scen_par.replace(' ', '_')

  corpus_f = '../res/Corpora/' + corpus_name + '_corpus.xml'
  log_f = '../res/Corpora/' + corpus_name + '_log.txt'
  doc_dir = '../res/Corpora/' + corpus_name + '_docs'
  query_f = '../res/Queries/' + scen_long +'_queries.txt' 
  url_dir = '../res/Corpora/' + corpus_name + '_urls'

  
  #til here
  try:
    new_qs, new_urls = _file_operations(corpus_f, corpus_name, doc_dir, new_qs, query_f, new_urls, url_dir, log_f)
  except KeyboardInterrupt:
    return

  #til here 
  urls, results, snippets, scored_query_f =   _get_url_shelves(new_qs, new_urls, url_dir, 
                              scen_long, scen_short, scen_par, query_f, log_f)
  print(len(urls), 'URLs gefunden.\n\n')

  


  scored_query_f_from_corpus = '/'.join(['..','..'] + scored_query_f.split('/')[2:])
  #scored_query_f_from_corpus = '/'.join(scored_query_f.split('/')[3:]) #without prefix folders
  with open(corpus_f,'w') as c:
    c.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n\t',
        '<corpus eventid="', scen_id,
        #'" scenario="feed a pet dog" short="dog" time="', timestamp(), 
        '" scenario="' + scen + '" short="' + scen_short.replace('_',' ') +
        '" time="', timestamp(), '" potential_queries="', scored_query_f_from_corpus, '">\n')))

  q_scores = shelve.open(url_dir + '/query_scores','r')
  #try:
  #  url_scores = shelve.open('../res/Corpora/' + corpus_name + '_urls/url_scores','r')
  #  if len(url_scores) == 0:
  #    raise Exception
  #except:
  #  url_scores.close()
  #  sD.make_url_scores('../res/Corpora/' + corpus_name + '_urls', q_scores)
  #  url_scores = shelve.open('../res/Corpora/' + corpus_name + '_urls/url_scores','r')


  url_scores = shelve.open(url_dir + '/url_scores')
  titles = shelve.open(url_dir + '/bingtitles')
  
  #til here:
  make_docs(urls, results, snippets, titles, q_scores, url_scores, corpus_name, corpus_f, log_f)

  urls.close()
  q_scores.close()
  url_scores.close()
  for rs in results:
    rs.close()
  for sn in snippets:
    sn.close()



  with open(corpus_f,'a') as c:
    c.write('\n</corpus>')
  return
  #TODO? score corpus documents




def get_all_corpora_gen(new_urls = False, new_qs = False, flag = 'mini1', withExceptions = True,start=0,stop = 10):
  # flags: mini+int, random urls, list url ids -> mini mit given_urls
              # scored best n
  shorts = ["fast_food",
      "food_back",
      "laundry",
      "coffee",
      "dog", 
      "microwave",
      "credit_card",
      "vending_machine",
      "letter",
      "shower"]      
  ids = ['2', '3' , '56', '111', '66 ', '92', '11', '31', '101', '14']
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


  for i in range(start,stop):
    yield 'will create ' + scenarios[i]
    #print('name',scenarios[i] + '_eval', '; id',ids[i], '; scen',scenarios[i], '; short',shorts[i], '; par',participants[i])
    try:
      print(len(longs) , len(ids),  len(scenarios), len(shorts)) 
      build_corpus(flag + '-en-US/' + longs[i] , ids[i],  scenarios[i], longs[i], shorts[i], 
                  participants[i], new_urls, new_qs, flag)
      yield 'created ' + scenarios[i]
    except Exception as e:
      if withExceptions:
        raise e
      else:
        yield 'could not create ' + scenarios[i] + ' due to error:\n' + str(e)
  yield 'created all ' + str(len(scenarios)) + ' corpora'
  return







if __name__ == '__main__':
#  nq = True if '-q' in argv else False
#  nu = True if '-u' in argv else False
#  we = False if '-e' in argv else True
#
#  if True:
#    flag = 'eval'
#    build_corpus(flag + '-en-US/' + 'change_bed_sheets' , 'xxx',  'change bed sheets', 'change_bed_sheets', 'bed_sheets', 'bed sheets', nu, nq, flag)
#  else:

  #nq = True if '-q' in argv else False
  #nu = True if '-u' in argv else False
  #we = False if '-e' in argv else True
  #if '-m' in argv:
  #  build_corpus('trial_muell_dog',  '66', 'feed a pet dog', 'feed_a_pet_dog', 
  #                'feed_dog', 'dog', nu, nq, 'mini3')
  #else:
    #build_corpus('dog_developing_corp_march_1', '66', 'feed_a_pet_dog', 
    #              'feed_dog', 'dog', nu, nq)
  for message in get_all_corpora_gen(False, False, 'full', start = int(argv[1]), stop = int(argv[2])):
    #if input(message + '\n') == 'stop':
    #  break
    print('\n\n----\n', timestamp(), '\n', message)
    #wait_a_bit()
