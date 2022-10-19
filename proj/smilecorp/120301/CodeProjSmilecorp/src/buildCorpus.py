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

def build_corpus(scen, corpus_name, new_urls = True, new_qs = False):

  corpus_f = '../res/Corpora/' + corpus_name + '_corpus.xml'
  log_f = '../res/Corpora/' + corpus_name + '_log.txt'
  doc_dir = '../res/Corpora/' + corpus_name + '_docs'
  query_f = '../res/Queries/' + scen +'_queries.txt' 
  urlshelve_f = '../res/Corpora/' + corpus_name + '_urls_shelve'

  
  new_qs = new_qs or not os.path.isfile(query_f)
  new_urls = new_urls or new_qs or not os.path.isfile(urlshelve_f + '.db')
  print('new queries:', new_qs, (' ' if new_qs and os.path.isfile(query_f) else ' not ') + 'overwriting',query_f)
  print('new urlshelve:', new_urls, (' ' if new_urls and os.path.isfile(urlshelve_f + '.db')
 else ' not ') + 'overwriting', corpus_name + '_urls_shelve.db')


  if os.path.isfile(corpus_f) or os.path.exists(doc_dir):
    if not input('A corpus named ' + corpus_name + 
        ' already exists.\nDo you want to overwrite it?\n') == 'yes':
      raise Exception('Cannot continue without overwriting an existing corpus file.')

    #corpus file will just be overwritten later
    #os.rmdir(doc_dir)
    if os.path.exists(doc_dir):
      rmtree(doc_dir)

  if  os.path.isfile(urlshelve_f + '.db') and new_urls:
    os.remove(urlshelve_f + '.db')


  with open(log_f, 'w') as log:
    log.write(timestamp() + ' \n\n')

  if not os.path.exists(doc_dir):
    os.mkdir(doc_dir)
  else:
    raise Exception('Cannot continue without overwriting an existing corpus directory.')
    
  if new_qs:
    cQ.createQueries(scen, query_f)


  #urls = bF.get_URL_dict(query_f, 10, log_f) 
  if new_urls:
    bF.make_URL_shelve(query_f, urlshelve_f, 250, log_f)#TODO 250 
  urls = shelve.open(urlshelve_f) 

  print(len(urls), 'URLs gefunden.\n\n')
  #with open(scen + '_urls.txt','w') as uf:
  #  for u in urls:
  #    uf.write('\t'.join([str(len(urls[u])), u] + [q for q in urls[u]]) + '\n')



  #with open(comp_f,'w') as c:
    #c.write('doc\tHTMLParser\tohne Script and Style\tgetidied\ttidied xhtml\tlxml parser\t beautiful soup\n\n')
  with open(corpus_f,'w') as c:
    c.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n\t',
        '<corpus eventid="', '1234', #TODO how get eventid, as function param
        '" scenario="feed a pet dog" short="dog" time="', timestamp(), 
        '" potential_queries="', query_f, '">\n')))
  #TODO get scenario names from function parameters

  doc_no = 0
  url_no = 0
  n_succ = n_tot = n_ish = n_perf = 0
  for url in urls:
    n_supp = str(len(urls[url]))
    #if True:#int(n_supp) > 30: #TODO remove this limitation
    url_no += 1
    try:
      if url_no == 4982: 
        #print(url_no)
        continue
      title, body, errors = wF.get_doc(url,log_f)#, doc_no >= 0)
      #body = '\n\n--------------\n\n'.join(body)
    except Exception as e:
      raise e
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
        #n_ish += 1
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
      c.write(''.join(('\n\t\t<document id="doc', doc_id,'" url="', insertXMLEnt(url),'" time="',
                  timestamp(),'" support="',n_supp,'" title="', title, '" file="',
                    insertXMLEnt(doc_file),'">\n')))

      c.write('\t\t</document>\n')
    
    with open('../res/Corpora/' +  insertXMLEnt(doc_file),'w') as d:
      d.write(''.join(('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                  '\n<document id="doc', doc_id,'" url="', insertXMLEnt(url),'" time="', 
                  timestamp(),'" support="',n_supp,'" title="',title,'">\n')))
      for q_id, b_rank in urls[url]:
        #print('q, b_r:', q_id, b_rank)
        #print('q_id:', q_id)
        #print('type:',type(q_id))
        d.write(''.join(('\t\t\t<query id="', q_id,'" bing-rank="',str(b_rank),'"/>\n')))

      d.write(''.join(('\t<description> ist noch leer </description>\n',
                  '\t<body>\n\t\t',body,'\n\t</body>\n</document>\n')))
    #with open('../res/Corpora/' + doc_file[:-3] + 'html', 'w') as dh:
    #  dh.write(str(xhtml_tidied))
      

    if (url_no)  % 500 == 0:
      print('no probs:',n_perf,'/',n_tot,float(n_perf)/n_tot)
      print('>20chars:',n_succ,'/',n_tot,float(n_succ)/n_tot)
      print('non-empty:',n_ish,'/',n_tot,float(n_ish)/n_tot)
      #break

  urls.close()


  with open(corpus_f,'a') as c:
    c.write('\n</corpus>')






if __name__ == '__main__':
  nq = True if '-q' in argv else False
  nu = True if '-u' in argv else False
  if '-m' in argv:
    build_corpus('dog','trial_muell', new_urls = nu, new_qs = nq)
  else:
    build_corpus('dog','dog_developing_corp_22', new_urls = nu, new_qs = nq)
    

#TODO copy shelve!!!!!!!!

  
